from activities.starter.starter_db import read_data_to_df
from pathlib import Path
import sqlite3


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


def main():

    # paralympics_all_raw.xlsx filepath
    xlsx_file = Path(__file__).parent.parent. \
        joinpath('data', 'paralympics_all_raw.xlsx')

    sql_file_para = Path(__file__).parent.parent. \
        joinpath('db', 'paralympics_schema_starter.sql')

    db_para_file_path = "src/activities/db/paralympics.db"

    sql_file_courses = Path(__file__).parent.parent. \
        joinpath('db', 'courses.sql')

    db_courses_file_path = "src/activities/db/courses.db"

    # Creating dataframes from excel file
    df_games, df_country_codes = read_data_to_df(xlsx_file)

    # Describing dataframes
    describe_df(df_games)
    describe_df(df_country_codes)

    # Create database
    create_db(sql_file_para, db_para_file_path)
    create_db(sql_file_courses, db_courses_file_path)

    # Inserting a single row
    cols_to_insert = ['student_name', 'student_email']
    vals_to_insert = ['Alice Brown', 'alice.brown@school.com']
    insert_row(db_courses_file_path, "students", cols_to_insert,
               vals_to_insert)


if __name__ == "__main__":
    main()
