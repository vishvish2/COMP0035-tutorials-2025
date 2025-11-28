""" Mimics a typical file structure when using models classes and database witin an app

See https://sqlmodel.tiangolo.com/tutorial/code-structure/
There is no actual app code yet though!
"""
from activities.db_wk8.database import create_db_and_tables, add_teacher_data


def main():
    create_db_and_tables()
    add_teacher_data()


if __name__ == '__main__':
    main()
