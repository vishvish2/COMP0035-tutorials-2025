from activities.starter.starter_db import read_data_to_df
from pathlib import Path
import sqlite3
import pandas as pd
import os


def describe_df(df):
    """Outputs information about a pandas dataframe

        Parameters:
        df (DataFrame): pandas dataframe to describe

        Returns:
        None

    """
    # Column labels
    cols_str = "Columns labels are "
    for i in range(len(df.columns)):
        if i == (len(df.columns) - 1):
            cols_str += f"and {df.columns[i]}."
        else:
            cols_str += f"{df.columns[i]}, "
    print(cols_str)
    print("")

    # Column data types
    print("Column data types: ")
    print(df.dtypes)
    print("")

    # Unique values
    for col in df:
        print(df[col].unique())


def create_db(sql_script_path, db_path):
    """Creates a database based on an sql script in the specified file path

        Parameters:
        sql_scipt_path (str): File path to sql script
        db_path (str): File path to store the database

        Returns:
        None

    """

    # Creating cursor
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    # Reading SQL file
    with open(sql_script_path, "r", encoding="utf-8") as f:
        sql_script = f.read()

    # Executing SQL file
    cursor.executescript(sql_script)
    connection.commit()
    connection.close()


def insert_row(db_path, table_name, cols, vals):
    """Inserts specified values in the specified columns of single row of a
        specified database file

            Parameters:
            db_path (str): File path of the database
            table_name (str): Name of table in the db to insert into
            cols (list): list of columns to insert data into
            vals (list): list of values to insert into respective columns
                in cols

            Returns:
            None
    """

    # Create a connection to the database using sqlite3
    connection = sqlite3.connect(db_path)

    # Cursor object to execute SQL commands
    cursor = connection.cursor()

    # Enable foreign key constraints for sqlite
    cursor.execute('PRAGMA foreign_keys = ON;')

    # Define the SQL INSERT query
    cols_str = ""
    for i in range(len(cols)):
        if i == (len(cols) - 1):
            cols_str += f'{cols[i]}'
        else:
            cols_str += f'{cols[i]}, '

    vals_str = ""
    for i in range(len(vals)):
        if i == (len(vals) - 1):
            vals_str += f'"{vals[i]}"'
        else:
            vals_str += f'"{vals[i]}", '

    insert_sql = f'INSERT INTO {table_name} ({cols_str}) VALUES ({vals_str})'

    cursor.execute(insert_sql)  # Execute the insert query
    connection.commit()  # Commit the changes
    connection.close()  # Close the connection


def insert_multiple_rows(db_path, table_name, cols, data_df):
    """Inserts specified values in the specified columns of multiple rows of a
        specified database file from data in another file

            Parameters:
            db_path (str): File path of the database
            data_df (dataframe): pandas dataframe of data to insert
            table_name (str): Name of table in the db to insert into
            cols (list): list of columns to insert data into
            vals (list): list of values to insert into respective columns
                in cols

            Returns:
            None
    """
# Create a connection to the database using sqlite3
    connection = sqlite3.connect(db_path)

    # Cursor object to execute SQL commands
    cursor = connection.cursor()
    # Enable foreign key constraints for sqlite
    cursor.execute('PRAGMA foreign_keys = ON;')

    # Define the SQL insert statements for the parameterised queries
    cols_str = ""
    for i in range(len(cols)):
        if i == (len(cols) - 1):
            cols_str += f'{cols[i]}'
        else:
            cols_str += f'{cols[i]}, '

    vals_str = ""
    for i in range(len(cols)):
        if i == (len(cols) - 1):
            vals_str += '?'
        else:
            vals_str += '?, '

    student_sql = f'INSERT INTO {table_name} ({cols_str}) \
        VALUES ({vals_str})'

    # Create dataframe with the unique values for the columns needed for the
    # student table (database add the PK automatically)
    student_df = pd.DataFrame(data_df[cols].drop_duplicates())

    # Get the values as a list rather than pandas Series.
    # The parameterised query expects a list.
    student_data = student_df.values.tolist()

    # Use `executemany()` with a parameterised query to add values to table.
    cursor.executemany(student_sql, student_data)

    connection.commit()  # Commit the changes
    connection.close()  # Close the connection


def delete_rows(db_path):
    """Empties a database in specified path

            Parameters:
            db_path (str): file path to the database

            Returns:
            None
    """
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name"
                " NOT LIKE 'sqlite_%';")
    table_names = [row[0] for row in cur.fetchall()]
    for table_name in table_names:
        cur.execute(f"DELETE FROM {table_name}")
    conn.commit()
    conn.close()


def main():

    # File paths
    xlsx_file = Path(__file__).parent.parent. \
        joinpath('data', 'paralympics_all_raw.xlsx')

    sql_file_para = Path(__file__).parent.parent. \
        joinpath('db', 'paralympics_schema_starter.sql')

    db_para_file_path = "src/activities/db/paralympics.db"

    sql_file_courses = Path(__file__).parent.parent. \
        joinpath('db', 'courses.sql')

    db_courses_file_path = "src/activities/db/courses.db"

    student_data_file = Path(__file__).parent.parent. \
        joinpath('data', 'student_data.csv')

    # Creating dataframes from file paths
    df_games, df_country_codes = read_data_to_df(xlsx_file)
    df_students = pd.read_csv(student_data_file)

    # Describing dataframes
    describe_df(df_games)
    describe_df(df_country_codes)

    # Create databases or clear them if existing
    if not os.path.exists(db_para_file_path):
        create_db(sql_file_para, db_para_file_path)
    else:
        delete_rows(db_para_file_path)

    if not os.path.exists(db_courses_file_path):
        create_db(sql_file_courses, db_courses_file_path)
    else:
        delete_rows(db_courses_file_path)

    # Inserting rows
    cols_to_insert_s = ['student_name', 'student_email']
    cols_to_insert_t = ['teacher_name', 'teacher_email']
    cols_to_insert_c = ["course_name", "course_code", "course_schedule",
                        "course_location"]
    # Single row
    # vals_to_insert = ['Alice Brown', 'alice.brown@school.com']
    # insert_row(db_courses_file_path, "students", cols_to_insert,
    #            vals_to_insert)

    # Multiple rows
    insert_multiple_rows(db_courses_file_path, "student", cols_to_insert_s,
                         df_students)
    insert_multiple_rows(db_courses_file_path, "teacher", cols_to_insert_t,
                         df_students)
    insert_multiple_rows(db_courses_file_path, "course", cols_to_insert_c,
                         df_students)

    connection = sqlite3.connect(db_courses_file_path)
    cursor = connection.cursor()

    enrollment_sql = """
    INSERT INTO enrollment (student_id, course_id, teacher_id)
    VALUES ((SELECT id FROM student WHERE student_email = ?), \
            (SELECT id FROM course WHERE course_name = ? AND course_code = ?),\
            (SELECT id FROM teacher WHERE teacher_email = ?)) \
    """
    for _, row in df_students.iterrows():
        cursor.execute(
            enrollment_sql,
            (
                row['student_email'],
                row['course_name'],
                row['course_code'],
                row['teacher_email'],
            )
        )
    connection.commit()
    connection.close()


if __name__ == "__main__":
    main()
