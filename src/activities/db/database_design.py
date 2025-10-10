from activities.starter.starter_db import read_data_to_df
from pathlib import Path

# paralympics_all_raw.xlsx filepath
xlsx_file = Path(__file__).parent.parent. \
    joinpath('data', 'paralympics_all_raw.xlsx')


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


def main():

    # Creating dataframes from excel file
    df_games, df_country_codes = read_data_to_df(xlsx_file)

    # Describing dataframes
    describe_df(df_games)
    describe_df(df_country_codes)


if __name__ == "__main__":
    main()
