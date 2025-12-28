""" Creates the database file with tables

Note:
    The models import is required for the create_all to create the tables.

    from activities.starter.db_wk8 import models

    """
from importlib import resources
from pathlib import Path

from sqlmodel import SQLModel, create_engine, select, text, Session

from activities import db_wk8
from activities.db_wk8.models import Location, Enrollment, Student, Teacher, Course

import pandas as pd

student_db = resources.files(db_wk8).joinpath("students.sqlite")
sqlite_url = f"sqlite:///{str(student_db)}"
# echo=True means the SQL executed by SQLModel will be output to the terminal when the code is run.
# This can be useful for debugging.
engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    with engine.connect() as connection:
        connection.execute(text("PRAGMA foreign_keys=ON"))  # for SQLite foreign key support
        SQLModel.metadata.create_all(engine)


def add_teacher_data():
    data_path = Path(__file__).parent.parent.joinpath('data', 'student_data.csv')
    cols = ["teacher_name", "teacher_email"]
    df = pd.read_csv(data_path, usecols=cols)

    # 2. Convert DataFrame rows to SQLModel instances
    teachers = []
    for _, row in df.iterrows():
        record = Teacher(**row.to_dict())
        teachers.append(record)

    # 3. Insert into database
    with Session(engine) as session:
        session.add_all(teachers)
        session.commit()


def add_all_data():
    """Adds data from CSV to each table using pandas DataFrame to filter the data. """
    df = pd.read_csv("src/activities/data/student_data.csv")

    # Find the unique location rows then create Location objects from these
    locations = df["course_location"].unique()
    loc_objects = []
    for loc in locations:
        location = Location(room=loc)
        loc_objects.append(location)

    # Find the unique student rows then create Student objects from these
    rows = df.drop_duplicates(subset=['student_name'])
    stu_objects = []
    for _, row in rows.iterrows():
        student = Student(student_name=row["student_name"], student_email=row["student_email"])
        stu_objects.append(student)

    # Find the unique teacher rows then create Teacher objects from these
    # You may have already added teacher data, in which case exclude this section
    rows = df.drop_duplicates(subset=['teacher_name'])
    teacher_objects = []
    for _, row in rows.iterrows():
        teacher = Teacher(teacher_name=row.teacher_name, teacher_email=row.teacher_email)
        teacher_objects.append(teacher)

    # Find the unique coutse rows then create Course objects from these
    rows = df.drop_duplicates(subset=['course_name'])
    course_objects = []
    for _, row in rows.iterrows():
        course = Course(course_name=row.course_name, course_code=row.course_code, course_schedule=row.course_schedule)
        course_objects.append(course)

    with Session(engine) as session:
        # Add the objects to the individual tables. Note there are no primary or foreign key values at this stage.
        # Once the objects are added to the database, the primary key value will be created 
        session.add_all(loc_objects)
        session.add_all(stu_objects)
        session.add_all(teacher_objects)
        session.add_all(course_objects)
        session.commit()

        # Create and add the enrollment objects and add the location FK to the courses
        for _, row in df.iterrows():
            # Find the ids of the rows
            location = session.exec(select(Location).where(Location.room == row["course_location"])).first()
            s_id = session.exec(select(Student.id).where(Student.student_email == row["student_email"])).first()
            c_id = session.exec(select(Course.id).where(Course.course_code == row["course_code"])).first()
            t_id = session.exec(select(Teacher.id).where(Teacher.teacher_email == row["teacher_email"])).first()
            # Update the course with the location using the relationship attribute
            course.location = location
            # Create the new enrollment for the row
            enrollment = Enrollment(student_id=s_id, course_id=c_id, teacher_id=t_id)
            session.add_all([course, enrollment])
            session.commit()


def drop_db_and_tables():
    SQLModel.metadata.drop_all(engine)


def get_teacher():
    with Session(engine) as session:
        results = session.exec(select(Teacher).where(Teacher.teacher_name == "Mark Taylor")).all()
        for teacher in results:
            print(teacher)


def get_students():
    with Session(engine) as session:
        results = session.exec(select(Student.student_name)).all()
        for student in results:
            print(student)

def get_physics_students():
    with Session(engine) as session:
        results = session.exec(select(Student.student_name, Student.student_email)
                               .join(Enrollment).join(Course)
                               .where(Course.course_name == "Physics")
                               .order_by(Student.student_name)).all()
        for student in results:
            print(student)

def get_courses():
    with Session(engine) as session:
        results = session.exec(select(Course)
                               .join(Enrollment).join(Student)
                               .where(Student.id == 1)).all()
        for student in results:
            print(student)
