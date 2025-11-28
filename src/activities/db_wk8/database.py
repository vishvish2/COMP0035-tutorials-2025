""" Creates the database file with tables

Note:
    The models import is required for the create_all to create the tables.

    from activities.starter.db_wk8 import models

    """
from importlib import resources
from pathlib import Path

from sqlmodel import SQLModel, create_engine, text, Session

from activities import db_wk8
from activities.db_wk8 import models

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
        record = models.Teacher(**row.to_dict())
        teachers.append(record)

    # 3. Insert into database
    with Session(engine) as session:
        session.add_all(teachers)
        session.commit()


def drop_db_and_tables():
    SQLModel.metadata.drop_all(engine)
