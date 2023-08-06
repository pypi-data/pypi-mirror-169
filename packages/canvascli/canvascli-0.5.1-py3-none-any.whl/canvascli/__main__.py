"""A CLI to reformat and review Canvas grades.
See the README and class docstrings for more info.
"""
import getpass
import json
import os
from collections import defaultdict
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP
from importlib.metadata import version
from requests.exceptions import MissingSchema
from urllib.error import URLError

import altair as alt
import click
import pandas as pd
from appdirs import user_data_dir
from canvasapi import Canvas
from canvasapi.exceptions import InvalidAccessToken, Unauthorized
from luddite import get_version_pypi
from tqdm import tqdm
# Using https://github.com/biqqles/dataclassy instead of dataclasses from
# stdlibto allow for dataclass inheritance when there are default values. Could
# use a custom init but it gets messy and the advantage of using dataclasses is
# lost. Dataclass inheritance might be fixed in 3.10
# https://bugs.python.org/issue36077
from dataclassy import dataclass
from . import __version__


# Using this as a first try, might have to use an external file instead
alt.data_transformers.disable_max_rows()

@click.group()
@click.version_option(version=__version__, prog_name='canvascli')
def cli():
    """A CLI to reformat and review Canvas grades.

    \b
    Examples:
        # Download grades from canvas and convert them to FSC format
        canvascli prepare-fsc-grades --course-id 53665
        \b
        # Show courses accessible by the given API token
        canvascli show-courses

    See the --help for each subcommand for more options.

    If you don't want to be prompted for your Canvas API token,
    you can save it to an environmental variable named CANVAS_PAT.
    """
    # Since canvascli might be useful for people who don't use Python
    # frequently, I have chosen to always print the program version and to
    # occasionally check for newer versions of canvascli online and to note if
    # one is found.
    canvascli_version = version('canvascli')
    click.echo(f'\ncanvascli version {canvascli_version}')

    if 'canvascli_prevent_update' in os.environ:
        pass
    else:
        data_dir = user_data_dir('canvascli')
        data_file = os.path.join(data_dir, 'data.json')
        try:
            # If the config file exists
            with open(data_file) as f:
                stored_data = json.load(f)
        except (FileNotFoundError, OSError, PermissionError):
            # Generate a default config when no file is found
            stored_data = {}
            stored_data['last_update_check'] = '2001-01-01'

        last_update_check = datetime.strptime(
            stored_data['last_update_check'],
            '%Y-%m-%d'
        )
        # Run a check online and update the config file if the last check was a long time ago
        if (datetime.now() - last_update_check) > pd.Timedelta(weeks=4):
            try:
                latest_version = get_version_pypi("canvascli")
                # Update `last_update_check` in the config if the update check is succesful
                if canvascli_version == latest_version:
                    os.makedirs(data_dir, exist_ok=True)
                    with open(data_file, 'w', encoding='utf-8') as f:
                        json.dump(
                            {'last_update_check': datetime.now().strftime('%Y-%m-%d')},
                            f,
                            ensure_ascii=False,
                            indent=4
                        )
                    # If no update was found, don't check again untill the env variables are cleared
                    # This avoids reading the settings file unnecessarily
                    # since the result will likely be the same in the same session anyways.
                    os.environ['canvascli_prevent_update'] = 'True'
                else:
                    click.secho('\nNOTE', fg='yellow', bold=True)
                    click.echo(
                        f'A new version ({latest_version}) is available'
                        '\nRead the release notes at https://github.com/joelostblom/canvascli/releases'
                        '\nand download it via `python -m pip install -U canvascli`.'
                    )
            except URLError:
                # If there is no connectivity
                pass
    return


@cli.command()
@click.option('--course-id', default=None, required=True, type=int, help='Canvas id'
              ' of the course to download grades from, e.g. 53665. This id'
              ' can be found by running `canvascli show-courses`'
              "(and in the course's canvas page URL). Default: None")
@click.option('--filename', default=None, help='Name of the saved file and chart'
              ' (without file extension). Default: Automatic based on the course.')
@click.option('--api-url', default='https://canvas.ubc.ca', help='Base canvas URL.'
              ' Default: https://canvas.ubc.ca')
@click.option('--student-status', default='active', help='Which types of students'
              ' to download grades for. Default: active')
@click.option('--drop-students', default=None, help='Student numbers to drop,'
              ' in quotes separated by spaces, e.g. "14391238 30329123".'
              ' Useful for removing specific students. Default: None')
@click.option('--drop-threshold', default=0, help='Students with grades <='
              ' this threshold are dropped. Useful for removing test students'
              ' and students that dropped the course after completing some work.'
              ' Default: 0')
@click.option('--drop-na', default=True, help='Whether to drop students'
              ' that are missing info such as student number.'
              ' Useful for only removing test students. Default: True')
@click.option('--open-chart', default=None, type=bool, help='Whether to open'
              ' the grade distribution chart automatically.'
              ' Default: Ask at the end')
@click.option('--override-campus', default=None, help='Override the automatically'
              ' detected course campus in the CSV file with this text. Default: None')
@click.option('--override-course', default=None, help='Override the automatically'
              ' detected course title in the CSV file with this text. Default: None')
@click.option('--override-section', default=None, help='Override the automatically'
              ' detected course section in the CSV file with this text. Default: None')
@click.option('--override-session', default=None, help='Override the automatically'
              ' detected course session in the CSV file with this text. Default: None')
@click.option('--override-subject', default=None, help='Override the automatically'
              ' detected course subject in the CSV file with this text. Default: None')
def prepare_fsc_grades(course_id, filename, api_url, student_status,
                       drop_students, drop_threshold, drop_na,
                       open_chart, override_campus, override_course,
                       override_section, override_session, override_subject):
    """Prepare course grades for FSC submission.
    \b
    Download grades from a canvas course and convert them to the format
    required by the FSC for submission of final grades.

    Grades are rounded to whole percentages and capped at 100.
    Students with missing info or 0 grade are dropped by default.

    A CSV file is saved in the current directory,
    which can be uploaded directly to FSC.
    A grade distribution chart is saved in the current directory.

    \b
    Examples:
        # Download grades from canvas and convert them to FSC format
        canvascli prepare_fsc_grades --course-id 53665
        \b
        # Give a custom file name and drop a specific student
        canvascli prepare_fsc_grades --course-id 53665 --drop-students "43659202"
    """
    fsc_grades = FscGrades(
        course_id, filename, api_url, student_status, drop_students,
        drop_threshold, drop_na, open_chart, override_campus,
        override_course, override_section, override_session, override_subject)
    fsc_grades.connect_to_canvas()
    fsc_grades.connect_to_course()
    fsc_grades.get_canvas_grades()
    fsc_grades.drop_student_entries()
    fsc_grades.convert_grades_to_fsc_format()
    if fsc_grades.fsc_grades.empty:
        click.echo('Did not find any assigned grades, exiting.')
    else:
        fsc_grades.save_fsc_grades_to_file()
        fsc_grades.plot_assignment_scores()
        fsc_grades.plot_fsc_grade_distribution()
        fsc_grades.show_manual_grade_entry_note()
    return


@cli.command()
@click.option('--api-url', default='https://canvas.ubc.ca', help='Base canvas URL.'
              ' Default: https://canvas.ubc.ca')
@click.option('--filter', 'filter_', default='', help='Only show courses including'
              ' this string (case insensitve). Useful to narrow down the displayed'
              ' results. Default: "" (matches all courses)')
@click.option('--start-date', 'start_date_', default=None, help='Show courses'
              ' starting at or after this date. Courses without a start date are'
              ' always shown. Format "YYYY-MM-DD". Default: Show all courses'
              ' starting within a year from today.')
def show_courses(api_url, filter_, start_date_):
    """Show courses accessible by the given API token.

    Examples:
        \b
        # Show all courses
        canvascli show-courses
        \b
        # Show only courses including the string "541"
        canvascli show-courses --filter 541
    """
    accessible_courses = AccessibleCourses(api_url, filter_, start_date_)
    accessible_courses.connect_to_canvas()
    accessible_courses.download_courses()
    accessible_courses.filter_and_show_courses()
    return


@cli.command()
def z_compare_TA_grading():
    """**Not yet implemented**"""
    return


@cli.command()
def z_review_student_grades():
    """**Not yet implemented**"""
    return


@dataclass
class CanvasConnection():
    """Parent class for initializing attributes shared between child classes."""
    invalid_canvas_url_msg: str = (
        '\nThe canvas URL you specified is invalid,'
        ' Please supply a URL in the folowing format: https://canvas.ubc.ca')
    invalid_canvas_api_token_msg: str = (
        '\nYour API token is invalid. The token you tried is:\n{}'
        '\n\nSee this canvas help page for how to setup up API tokens:'
        '\nhttps://community.canvaslms.com/t5/Instructor-Guide/How-do-I-manage-API-access-tokens-as-an-instructor/ta-p/1177')

    def connect_to_canvas(self):
        """Connect to a canvas instance."""
        click.echo('\nConnecting to canvas...')
        self.api_token = os.environ.get("CANVAS_PAT")
        if self.api_token is None:
            self.api_token = getpass.getpass(
                'Paste your canvas API token and press enter:')
        self.canvas = Canvas(self.api_url, self.api_token)
        return


@dataclass
class AccessibleCourses(CanvasConnection):
    """Show all courses accessible from a specific API token."""
    api_url: str
    filter_: str
    start_date_: str

    def download_courses(self):
        """Download all courses accessible from a specific API token."""
        self.courses = defaultdict(list)
        try:
            for course in self.canvas.get_courses():

                # Return a default value ('N/A') if the attribute is not found
                self.courses['id'].append(getattr(course, 'id', 'N/A'))
                self.courses['name'].append(getattr(course, 'name', 'N/A'))
                self.courses['end_date'].append(getattr(course, 'end_at', 'N/A'))
                self.courses['start_at'].append(getattr(course, 'start_at', 'N/A'))
        # Show common exceptions in a way that is easy to understand
        except MissingSchema:
            raise SystemExit(self.invalid_canvas_url_msg)
        except InvalidAccessToken:
            raise SystemExit(self.invalid_canvas_api_token_msg.format(self.api_token))
        return

    def filter_and_show_courses(self):
        """Filter and show downloaded courses."""
        # The default is to include courses starting in the past year
        start_date = pd.to_datetime(
            self.start_date_ or datetime.now() - pd.DateOffset(months=12),
            utc=True
        ).date()
        click.echo("Your API token has access to the following courses:\n")
        click.echo(
            pd.DataFrame(
                self.courses
            ).assign(
                start_at = lambda df: pd.to_datetime(df['start_at']).dt.date
            ).query(
                'start_at > @start_date'
            ).query(
                'name.str.contains(@self.filter_, case=False)',
                engine='python'
            ).sort_values(
                'start_at'
            ).drop(
                columns=['end_date']
            ).rename(
                columns={'id': 'ID', 'name': 'Name', 'start_at': 'Start Date'}
            ).to_markdown(
                index=False
            )
        )
        return


@dataclass
class FscGrades(CanvasConnection):
    """Prepare FSC grades for a specific course."""
    course_id: int
    filename: str
    api_url: str
    student_status: str
    drop_students: str
    drop_threshold: int
    drop_na: bool
    open_chart: bool
    override_campus: str
    override_course: str
    override_section: str
    override_session: str
    override_subject: str
    unauthorized_course_access_msg: str = (
        '\nYour API token is not authorized to access course {}.'
        '\nRun `canvascli show-courses` to see all courses you can access.')

    def plot_assignment_scores(self):
        # import ipdb; ipdb.set_trace()
        assignments = [a for a in self.course.get_assignments() if a.points_possible > 0]
        assignment_scores_dfs = []
        click.echo("Downloading assignment scores...")
        assignment_progress_bar = tqdm(assignments)
        for assignment in assignment_progress_bar:
            assignment_progress_bar.set_description(assignment.name)
            submissions = assignment.get_submissions()
            assignment_scores = defaultdict(list)
            for submission in submissions:
                assignment_scores['User ID'].append(submission.user_id)
                assignment_scores[f'Grader ID'].append(submission.grader_id)
                assignment_scores[f'Score'].append(100 * submission.score / assignment.points_possible if submission.score is not None else None)
                assignment_scores[f'Assignment'].append(assignment.name)
                # assignment_scores['Grade'].append(submission.grade)
            assignment_scores_dfs.append(pd.DataFrame(assignment_scores))
        assignment_score_df = pd.concat(assignment_scores_dfs)
        # Sometime a negative number is returned for the grader, which does not make sense, maybe from gradescope?
        assignment_score_df.loc[assignment_score_df['Grader ID'] < 0, 'Grader ID']  = pd.NA
        # grader_id_and_names = {grader_id: self.course.get_user(grader_id).name for grader_id in tqdm(assignment_score_df['Grader ID'].dropna().unique().astype(int))}
        # student_id_and_names = {student_id: self.course.get_user(student_id).name for student_id in tqdm(assignment_score_df['User ID'].dropna().unique().astype(int))}
        user_ids_and_names = {user.id: user.name for user in self.course.get_users()}
        assignment_score_df['Grader'] = assignment_score_df['Grader ID'].map(user_ids_and_names)
        assignment_score_df['Student'] = assignment_score_df['User ID'].map(user_ids_and_names)
        assignment_score_df['Score'] = assignment_score_df['Score'].apply(
            lambda x: Decimal(x).quantize(2, rounding=ROUND_HALF_UP))
        # assignment_score_df.to_csv('assignment_scores_long.csv', index=False)
            # for submission in submissions:
            #     assignment_scores['User ID'].append(submission.user_id)
            #     assignment_scores[f'Grader ID {assignment.name}'].append(submission.grader_id)
            #     assignment_scores[f'Score {assignment.name}'].append(submission.score)
            #     # assignment_scores['Grade'].append(submission.grade)
            # assignment_scores_dfs.append(pd.DataFrame(assignment_scores).set_index('User ID'))
        # assignment_score_df = pd.concat(assignment_scores_dfs, axis=1).reset_index()

        grader_order = assignment_score_df.groupby('Grader')['Score'].mean().sort_values().index.tolist()
        height = max(80, len(grader_order) * 20) # Min height=80 for histograms to look nice
        # 20 is the default step size for categorical values such as the boxplor
        self.assignment_distributions = alt.Chart(assignment_score_df, height=height, title='Assignment scores distribution').mark_bar().encode(
            x=alt.X('Score', bin=alt.Bin(step=5)), 
            y=alt.Y('count()', title='Student count'),
            row=alt.Row('Assignment', title='', header=alt.Header(labelFontSize=13))
        ) | alt.Chart(assignment_score_df.reset_index(), height=height, title='Score comparison between graders').mark_boxplot().encode(
            x=alt.X('Score').scale(zero=False),
            y=alt.Y('Grader:N', sort=grader_order, title=''),
            row=alt.Row('Assignment', title='', header=alt.Header(labels=False)),
            color=alt.Color('Grader:N', legend=None)
        )

        assignment_score_df['Assignment scores stdev'] = assignment_score_df['User ID'].map(
            assignment_score_df.groupby('User ID')['Score'].std())

        hover = alt.selection_point(fields=['User ID'], on='mouseover', nearest=True, empty=False)
        base = alt.Chart(assignment_score_df).mark_point(opacity=0).encode(
            y=alt.Y('Score').scale(zero=False).title('Score (%)'),
            detail='User ID',
            x='Assignment'
        )

        width = min(1500, max(500, 80 * assignment_score_df['Assignment'].nunique()))
        self.assignment_scores = (base.add_parameter(
            hover
        ) + base.mark_line(opacity=0.5).encode(
            color=alt.Color('Assignment scores stdev').scale(scheme='cividis', reverse=True)
        ) + base.mark_line(size=3, point=True).encode(
            color=alt.value('maroon'),  # required to color points
            tooltip=alt.Tooltip(['Student', 'Score']),
        ).transform_filter(
            hover
        )).properties(
            width=width, #alt.Step(100),
            height=400,
            # padding=0
        ).interactive()
                # import ipdb; ipdb.set_trace()
        return

    def connect_to_course(self):
        """Connect to as specific canvas course."""
        try:
            self.course = self.canvas.get_course(self.course_id)
        # Show common exceptions in a way that is easy to understand
        except MissingSchema:
            raise SystemExit(self.invalid_canvas_url_msg)
        except InvalidAccessToken:
            raise SystemExit(self.invalid_canvas_api_token_msg.format(self.api_token))
        except Unauthorized:
            raise SystemExit(self.unauthorized_course_access_msg.format(self.course_id))
        if self.filename is None:
            self.filename = (f'fsc-grades_{self.course.course_code.replace(" ", "-")}'
                             .replace('/', '-'))
        return

    def get_canvas_grades(self):
        """Download grades from a canvas course."""
        click.echo('Downloading student grades...')
        enrollments = self.course.get_enrollments(
            type=['StudentEnrollment'], state=[self.student_status]
        )
        canvas_grades = defaultdict(list)
        for enrollment in enrollments:
            canvas_grades['Student Number'].append(enrollment.user['sis_user_id'])
            surname, preferred_name = enrollment.user['sortable_name'].split(', ')
            canvas_grades['Surname'].append(surname)
            canvas_grades['Preferred Name'].append(preferred_name)

            # A warning message is later displayed for these students
            if 'override_score' in enrollment.grades:
                canvas_grades['Percent Grade'].append(enrollment.grades['override_score'])
                canvas_grades['override_final_score'].append(enrollment.grades['final_score'])
            else:
                canvas_grades['Percent Grade'].append(enrollment.grades['final_score'])
                canvas_grades['override_final_score'].append(0)

            # A warning message is later displayed for these students
            if 'unposted_final_score' in enrollment.grades:
                canvas_grades['Unposted Percent Grade'].append(enrollment.grades['unposted_final_score'])
                if enrollment.grades['unposted_final_score'] != enrollment.grades['final_score']:
                    canvas_grades['different_unposted_score'].append(True)
                else:
                    canvas_grades['different_unposted_score'].append(False)

        self.canvas_grades = pd.DataFrame(canvas_grades)
        different_unposted_score = self.canvas_grades.pop('different_unposted_score')
        override_final_score = self.canvas_grades.pop('override_final_score')

        # Display a note that some student grade are manually overridden
        if override_final_score.sum() > 0:
            click.secho('\nNOTE', fg='yellow', bold=True)
            click.echo(
                'You have used the "Overide" column on Canvas'
                '\nto change the final score for the following students:\n'
            )
            click.echo(
                self.canvas_grades
                    .query(
                        '@override_final_score > 0'
                    ).assign(
                        **{'Percent Grade Before Override': override_final_score}
                    ).drop(
                        columns='Unposted Percent Grade'
                    ).to_markdown(
                        index=False
                    )
                )
            click.echo()

        # Warn about students with unposted grades that change their final scores
        if different_unposted_score.sum() > 0:
            click.secho('\nWARNING', fg='red', bold=True)
            click.echo(
                'Remember to post all assignments on Canvas'
                '\nbefore creating the CSV-file to upload to the FSC.'
                '\nThere are currently unposted Canvas assignments'
                '\nthat would change the final score of the following students:\n'
            )
            click.echo(
                self.canvas_grades
                    .query(
                        '@different_unposted_score == True'
                    )
                    .to_markdown(
                        index=False
                    )
                )
            click.echo()
        return

    def drop_student_entries(self):
        """Drop unwanted students entries such as test students and dropouts."""
        # Drop students under the grade thresholds
        # Test accounts and students who dropped the course often have a grade of zero
        dropped_students = self.canvas_grades.query(
            '`Unposted Percent Grade` <= @self.drop_threshold')
        self.canvas_grades = self.canvas_grades.query(
            '`Unposted Percent Grade` > @self.drop_threshold').copy()

        # Drop students that have missing info in any field
        # These are also printed so that it is clear to the user what has happened
        # and they need to be explicit in disabling the beahvior instead of
        # accidentally uploading empty fields to FSC.
        if self.drop_na:
            dropped_students = dropped_students.append(
                self.canvas_grades[self.canvas_grades.isna().any(axis=1)])
            self.canvas_grades = self.canvas_grades.dropna()

        # Drop students explicitly
        if self.drop_students is not None:
            dropped_students = dropped_students.append(
                self.canvas_grades.query(
                    '`Student Number` in @self.drop_students.split()'))
            self.canvas_grades = self.canvas_grades.query(
                '`Student Number` not in @self.drop_students.split()').copy()

        # Display the dropped students so the user can catch errors easily
        if dropped_students.shape[0] > 0:
            click.secho('\nNOTE', fg='yellow', bold=True)
            click.echo(
                f'Dropping {dropped_students.shape[0]}'
                f" {'students' if dropped_students.shape[0] > 1 else 'student'}"
                f' with missing information, a grade <= {self.drop_threshold},'
                '\nor that was explicitly dropped by student number:\n'
            )
            click.echo(dropped_students.to_markdown(index=False))
            click.echo()
        return

    def convert_grades_to_fsc_format(self):
        """Convert grades to FSC format."""
        # Extract FSC info from canvas
        # LT hub mentioned that these fields should be safe to extract from the
        # canvas course code (for UBC courses in general), but there is an override
        # option just in case
        self.campus = 'UBC'
        self.subject, self.course_name, self.section, self.session = self.course.course_code.split()
        if self.override_campus is not None:
            self.campus = self.override_campus
        if self.override_course is not None:
            self.course_name = self.override_course
        if self.override_section is not None:
            self.section = self.override_section
        if self.override_session is not None:
            self.session = self.override_session
        if self.override_subject is not None:
            self.subject = self.override_subject
        # Add FSC info to the dataframe, standing and standing reason are
        # blank by default and filled out manually when needed
        self.fsc_grades = self.canvas_grades.copy()
        additional_fsc_fields = ['Campus', 'Course', 'Section', 'Session', 'Subject',
                      'Standing', 'Standing Reason']
        # Remove the session number which is only present on Canvas but not FSC
        self.session = self.session[:-1]
        self.fsc_grades[additional_fsc_fields] = (
            self.campus, self.course_name, self.section, self.session, self.subject, '', '')

        # Round to whole percentage format since FSC requires that
        # Using Decimal to always round up .5 instead of rounding to even,
        # which is the default in numpy but could seem unfair to individual students.
        # The Decimal type is not json serializable (issue for altair) so changing to int.
        self.fsc_grades['Exact Percent Grade'] = self.fsc_grades['Percent Grade']
        self.fsc_grades['Percent Grade'] = self.fsc_grades['Percent Grade'].apply(
            lambda x: Decimal(x).quantize(0, rounding=ROUND_HALF_UP)).astype(int)

        self.fsc_grades['Unposted Exact Percent Grade'] = self.fsc_grades['Unposted Percent Grade']
        self.fsc_grades['Unposted Percent Grade'] = self.fsc_grades['Unposted Percent Grade'].apply(
            lambda x: Decimal(x).quantize(0, rounding=ROUND_HALF_UP)).astype(int)

        # Cap grades at 100
        self.fsc_grades.loc[self.fsc_grades['Percent Grade'] > 100, 'Percent Grade'] = 100

        return

    def save_fsc_grades_to_file(self):
        """Write a CSV file that can be uploaded to FSC."""
        # Reorder columns to match the required FSC format
        self.fsc_grades[[
            'Session', 'Campus', 'Student Number', 'Subject', 'Course', 'Section',
            'Surname', 'Preferred Name', 'Standing', 'Standing Reason', 'Percent Grade'
        ]].to_csv(
            self.filename + '.csv',
            index=False
        )
        click.echo(f'Grades saved to {self.filename}.csv.')
        return

    def plot_fsc_grade_distribution(self):
        # Prepare dataframe for filtering via Altair selection elements
        # First the rounded and raw scores are melted together separately for posted and unposted scores
        # Then they are merged into one frame and the posted and unposted score are melted together
        self.fsc_grades_for_viz = pd.merge(
            # Frame 1
            self.fsc_grades.rename(
                columns={
                    'Unposted Percent Grade': 'FSC Rounded',
                    'Unposted Exact Percent Grade': 'Exact'
                }
            # Combine the rounded and raw *unposted* scores 
            ).melt(
                id_vars=['Preferred Name', 'Surname', 'Student Number'],
                value_vars=['FSC Rounded', 'Exact'],
                value_name='Unposted Grade',
                var_name='Percent Type'
            ),
            # Frame 2
            self.fsc_grades.rename(
                columns={
                    'Percent Grade': 'FSC Rounded',
                    'Exact Percent Grade': 'Exact'
                }
            # Combine the rounded and raw *posted* scores 
            ).melt(
                id_vars=['Preferred Name', 'Surname', 'Student Number'],
                value_vars=['FSC Rounded', 'Exact'],
                value_name='Posted Grade',
                var_name='Percent Type'
            )
        # Combine the posted and unposted scores
        ).melt(
            id_vars=['Preferred Name', 'Surname', 'Student Number', 'Percent Type'],
            value_vars=['Unposted Grade', 'Posted Grade'],
            value_name='Percent Grade',
            var_name='Grade Status'
        )

        # Set up selection elements
        grade_status_dropdown = alt.binding_select(
            options=['Posted Grade', 'Unposted Grade'],
            name='Grade Status '
        )
        grade_status_selection = alt.selection_single(
            fields=['Grade Status'],
            bind=grade_status_dropdown,
            init={'Grade Status': 'Posted Grade'}
        )
        percent_type_dropdown = alt.binding_select(
            options=['FSC Rounded', 'Exact'],
            name='Percent Type '
        )
        percent_type_selection = alt.selection_single(
            fields=['Percent Type'],
            bind=percent_type_dropdown,
            init={'Percent Type': 'FSC Rounded'}
        )

        # Plot distribution
        hist = alt.Chart(self.fsc_grades_for_viz, height=200).mark_bar().encode(
            alt.X('Percent Grade', bin=alt.Bin(maxbins=15), title='', axis=alt.Axis(labels=False)),
            alt.Y('count()', title='Number of students')
        )

        # Plot all observations
        strip = alt.Chart(self.fsc_grades_for_viz, height=70).mark_point(
            size=20
        ).transform_calculate(
            # Generate Gaussian jitter with a Box-Muller transform
            jitter='sqrt(-2*log(random()))*cos(2*PI*random())',
            Name='datum["Preferred Name"] + " " + datum["Surname"]'
        ).encode(
            alt.X('Percent Grade',
                title='Percent Grade',
                scale=alt.Scale(
                    zero=False,
                    nice=False,
                    padding=5
                )
            ),
            alt.Y('jitter:Q',
                scale=alt.Scale(padding=2),
                axis=alt.Axis(
                    domain=False,
                    title='',
                    labels=False,
                    ticks=False,
                    grid=False
                )
            ),
            alt.Tooltip(['Name:N', 'Student Number', 'Percent Grade'])
        ).interactive()

        # Plot central tendencies
        central_tendencies = alt.Chart(
                self.fsc_grades_for_viz
            ).transform_aggregate(
                Mean='mean(Percent Grade)',
                Median='median(Percent Grade)',
            ).transform_fold(
                fold=['Mean', 'Median'],
                as_=['Type', 'Percent Grade']
            ).transform_calculate(
                y='-3.05',
            ).mark_point(
            size=65,
            shape='diamond'
        ).encode(
            x='Percent Grade:Q',
            y='y:Q',
            color=alt.Color(
                'Type:N',
                title='',
                scale=alt.Scale(range=['coral', 'rebeccapurple']),
                legend=alt.Legend(legendY=225, legendX=415, orient='none')
            ),
            tooltip=['Type:N', alt.Tooltip('Percent Grade:Q', format='.3g')]
        )

        # Add instructions
        title = alt.TitleParams(
            text=f'Grade distribution {self.subject} {self.course_name}',
            subtitle=[
                'Hover over the points to see the student name and grade.',
                'Zoom with the mouse wheel and double click to reset the view.',
                'Click the three dots button to the right to save the plot.']
        )

        # Concatenate, add filters, and save the chart
        chart_filename = self.filename + '.html'
        ((alt.vconcat(
            hist,
            # strip on top so that individual observations are always visible
            central_tendencies + strip,
            spacing=0
        ).properties(
            title=title
        ).resolve_scale(
            x='shared'
        # ).configure_view(
        #     strokeWidth=0
        ).transform_filter(
                percent_type_selection & grade_status_selection
        ).add_selection(
            percent_type_selection, grade_status_selection
        ) & self.assignment_scores) | self.assignment_distributions).save(
            chart_filename
        )
        # The label names are styled in serif by default for some reason
        with open(chart_filename, 'a') as chart_file:
            chart_file.write(
                '\n<style>'
                '\n    form.vega-bindings {'
                '\n        font-family: sans-serif;'
                '\n    }'
                '\n</style>'
            )
        click.echo(f'Grade distribution chart saved to {chart_filename}.')
        if self.open_chart or self.open_chart is None and click.confirm(
                'Open grade distribution chart?', default=True):
            click.launch(chart_filename)
        return

    def show_manual_grade_entry_note(self):
        """Show disclaimer and note about manual grade entry of student standings."""
        click.secho('\nNOTE', fg='yellow', bold=True)
        click.echo(
            '1. Make sure to check the output above for any warning and notes.'
            '\n2. The saved CSV file should automatically be correctly formatted,'
            '\n   but it is ' + click.style('your responsibility', bold=True) + ' to double check in case there are unexpected changes'
            '\n   to how UBC inputs course info on Canvas.'
            '\n3. If you have students that did not take the final exam'
            '\n   or with a thesis in progress, you will need to enter this info manually.'
            '\n   Please see https://facultystaff.students.ubc.ca/files/FSCUserGuide.pdf'
            '\n   under "Acceptable Values for Grades Entry" for how to modify the CSV file.')
        return

cli()
