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


def main():

    # paralympics_all_raw.xlsx filepath
    xlsx_file = Path(__file__).parent.parent. \
        joinpath('data', 'paralympics_all_raw.xlsx')

    sql_file = Path(__file__).parent.parent. \
        joinpath('db', 'paralympics_schema_starter.sql')

    db_file_path = "src/activities/db/paralympics.db"

    # Creating dataframes from excel file
    df_games, df_country_codes = read_data_to_df(xlsx_file)

    # Describing dataframes
    describe_df(df_games)
    describe_df(df_country_codes)

    # Create database
    create_db(sql_file, db_file_path)


if __name__ == "__main__":
    main()
