from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


def describe_df(df):
    """Outputs information about a pandas dataframe

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


def missing_vals(df):
    """Outputs number of missing values in a pandas dataframe
        Create new dataframe with missing values

        Parameters:
        df (DataFrame): pandas dataframe to search

        Returns:
        missing (DataFrame): pandas dataframe with rows which have
                                missing values

    """
    nan_count = 0                   # Null value counter
    for item in df:                 # Iterate through columns
        for entry in df.isna()[item]:
            if entry:               # Iterate through each row in column
                nan_count += 1      # True = null value
    print(nan_count)

    missing_rows = df[df.isna().any(axis=1)]
    return missing_rows


def plot_hist(df):
    """Plots a histogram of numerical data in the dataframe

        Parameters:
        df (DataFrame): pandas dataframe to analyse

        Returns:
        None

    """
    columns = ["participants_m", "participants_f"]
    df[columns].hist()
    plt.show()


def plot_boxplot(df):
    """Plots a boxplot of numerical data in the dataframe

        Parameters:
        df (DataFrame): pandas dataframe to analyse

        Returns:
        None

    """
    # columns = ["participants_m", "participants_f"]
    df.boxplot()
    plt.show()


def plot_time_series(df, start, participants):
    """Plots a line chart of numerical data against time in a dataframe

        Parameters:
        df (DataFrame): pandas dataframe to analyse
        start (str): Which column for x axis data (usually time)
        participants (str): Which columns for y axis data

        Returns:
        None

    """
    df.plot(start, participants)
    plt.show()


def identify_categorical(df, col):
    """Identifies categorical data in a specified column of a dataframe

        Parameters:
        df (DataFrame): pandas dataframe to analyse
        col (str): Which column of the dataframe to analyse

        Returns:
        None

    """
    print(f"Distinct categorical values in the event '{col}' column")
    print(f"{df[col].unique()}")    # Unique categories in the column

    print(f"\nCount of each distinct categorical value in the event '{col}' \
column")
    print(f"{df[col].value_counts()}")
    # Count of each unique category in the columns


def remove_df_cols(df, cols):
    """Plots a removes specified columns from a dataframe

        Parameters:
        df (DataFrame): pandas dataframe to analyse
        cols (list): List of columns to remove

        Returns:
        df_prepared (DataFrame): New dataframe with specified columns removed

    """

    df_prepared = df.drop(columns=cols)
    return df_prepared


def remove_df_rows(df, rows):
    """Plots a removes specified rows from a dataframe

        Parameters:
        df (DataFrame): pandas dataframe to analyse
        rows (list): List of rowes to remove

        Returns:
        df_prepared_2 (DataFrame): New dataframe with specified columns removed

    """
    df = df.reset_index(drop=True)
    df_prepared_2 = df.drop(index=rows)
    return df_prepared_2


def prep_data(df):
    """Plots a line chart of numerical data against time in a dataframe

        Parameters:
        df (DataFrame): pandas dataframe to analyse

        Returns:
        prepped_df (DataFrame): Refined dataframe (e.g. no missing columns)

    """
    pass


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
dataframes = [df_csv, df_xlsx_games]

if __name__ == "__main__":

    for frame in dataframes:
        describe_df(frame)

    print("No. of missing values in each dataframe:")
    for frame2 in dataframes:
        print(missing_vals(frame2))
    print(missing_vals(df_csv))

    for frame3 in dataframes:   # Histograms
        plot_hist(frame3)

    plot_boxplot(df_csv)        # Boxplots

    # Line charts
    plot_time_series(df_csv, "year", "participants_m")
    plot_time_series(df_csv, "year", "participants_f")

    # Finding categorical data based on columns
    identify_categorical(df_csv, 'type')
    identify_categorical(df_csv, 'disabilities_included')

    # Removing unwanted columns
    df_csv_prepared = \
        remove_df_cols(df_csv, ['URL', 'disabilities_included', 'highlights'])

    # print(df_csv.columns)
    # print(df_csv_prepared.columns)

    print(df_csv_prepared.head(3))
    df_csv_prepared = remove_df_rows(df_csv_prepared, [0, 17, 31])
    print(df_csv_prepared.head(3))  # Double checking drop worked
    missing_vals(df_csv_prepared)   # Double checking rows with NaN are gone
