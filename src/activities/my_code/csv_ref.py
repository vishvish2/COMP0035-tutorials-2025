from pathlib import Path
import pandas as pd


def describe_df(df):
    """Summary or description of the function

        Parameters:
        df (DataFrame): pandas dataframe to describe

        Returns:
        None

    """
    pd.set_option("display.max_columns", None)

    print(df.shape)     # No. of rows and cols
    print(df.head(5))   # First 5 rows
    print(df.tail(5))   # Last 5 rows
    print(df.columns)   # Column labels
    print(df.dtypes)    # Column data types
    print(df.info)      # Info about dataframe
    print(df.describe)  # Descriptive statistics


# This script is located in a subfolder so you need to navigate up to the
# parent (src) and then its parent (project root), then down to the 'data'
# directory and finally the .csv file
# paralympics_raw.csv filepath
csv_file = Path(__file__).parent.parent.joinpath('data', 'paralympics_raw.csv')

# also works
csv_file_v2 = Path(__file__).parent.parent / 'data' / 'paralympics_raw.csv'

# paralympics_all_raw.xlsx filepath
xlsx_file = Path(__file__).parent.parent. \
    joinpath('data', 'paralympics_all_raw.xlsx')

# Check if the file exists
# if csv_file.exists():
#     print(f"CSV file found: {csv_file}")
# else:
#     print("CSV file not found.")


# if xlsx_file.exists():
#     print(f"CSV file found: {xlsx_file}")
# else:
#     print("CSV file not found.")

# Dataframes (xlsx file has multiple sheets)

# csv file
df_csv = pd.read_csv(csv_file)

# games sheet
df_xlsx_games = pd.read_excel(xlsx_file)

# team codes sheet
df_xlsx_codes = pd.read_excel(xlsx_file, sheet_name="team_codes")

# standings sheet
df_xlsx_standings = pd.read_excel(xlsx_file, sheet_name="medal_standings")

# summer sheet
df_xlsx_summer = pd.read_excel(xlsx_file, sheet_name="games-team-summer")

# winter sheet
df_xlsx_winter = pd.read_excel(xlsx_file, sheet_name="games-team-winter")

# List of dataframes
dataframes = [df_csv, df_xlsx_games, df_xlsx_codes, df_xlsx_standings,
              df_xlsx_summer, df_xlsx_winter]

if __name__ == "__main__":

    # describe_df(df_csv)

    for frame in dataframes:
        describe_df(frame)
