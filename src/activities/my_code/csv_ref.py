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
        start (str): which column for x axis data (usually time)
        participants (str): which columns for y axis data

        Returns:
        None

    """
    df.plot(start, participants)
    plt.show()


def identify_categorical(df, col):
    """Identifies categorical data in a specified column of a dataframe

        Parameters:
        df (DataFrame): pandas dataframe to analyse
        col (str): which column of the dataframe to analyse

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
        cols (list): list of columns to remove

        Returns:
        df_prepared (DataFrame): new dataframe with specified columns removed

    """

    df_prepared = df.drop(columns=cols)

    return df_prepared


def remove_df_rows(df, rows):
    """Plots a removes specified rows from a dataframe

        Parameters:
        df (DataFrame): pandas dataframe to analyse
        rows (list): list of rows to remove

        Returns:
        df_prepared_2 (DataFrame): new dataframe with specified columns removed

    """
    df = df.reset_index(drop=True)
    df_prepared_2 = df.drop(index=rows)

    return df_prepared_2


def decapitalise(df, col, data):
    """Decapitalise specified string entries in specified column

        Parameters:
        df (DataFrame): pandas dataframe to analyse
        col (str): column to analyse
        data (str): specific data entry to decapitalise

        Returns:
        None

    """
    index = df.query(f"{col} == @data").index[0]
    df.at[index, col] = data.lower()


def remove_whitespace(df, col, data):
    """Remove whitespaces in specified string entries in specified column

        Parameters:
        df (DataFrame): pandas dataframe to analyse
        col (str): column to analyse
        data (str): specific data entry to remove whtiespaces from

        Returns:
        None

    """
    index = df.query(f"{col} == @data").index[0]
    df.at[index, col] = data.strip()


def change_cols_dtype(df, cols, d_type):
    """Applies a fixed data type to specified columns

        Parameters:
        df (DataFrame): pandas dataframe to analyse
        cols (list): list of cols to modify
        d_type (str): data type to change the column to

        Returns:
        None

    """
    for col in cols:
        df[col] = df[col].astype(d_type)


def object_to_date(df, cols):
    """Changes object data type to datetime

        Parameters:
        df (DataFrame): pandas dataframe to analyse
        cols (list): list of columns to modify

        Returns:
        None

    """
    for col in cols:
        df[col] = pd.to_datetime(df[col], format='%d/%m/%Y')    # DD/MM/YYY


def prep_data(df, cols, rows, col_1, data_1, col_2, data_2, cols_2, d_type,
              cols_3):
    """Cleaning a dataframe for analysis

        Parameters:
        df (DataFrame): pandas dataframe to analyse
        cols (list): columns to remove
        rows (list): rows to remove
        col_1 (str): column to decapitalise entries of
        data_1 (str): data entries to decapitalise
        col_2 (str): column to remove whitespaces from entries of
        data_2 (str): data entries to remove whitespaces from
        cols_2 (list): columns to modify data type of
        d_type (str): data type to change the columns to cols_2 to
        cols_3 (list): columns to change from `object` data type to datetime

        Returns:
        prepped_df (DataFrame): refined dataframe

    """
    # Remove specified columns
    prepped_df = remove_df_cols(df, cols)

    # Remove specified rows
    prepped_df = remove_df_rows(df, rows)

    # Decapitalise specified column for consistency
    try:
        decapitalise(prepped_df, col_1, data_1)
    except IndexError:
        pass
    # ^ Index 0 had 'Summer' in type and was removed before hence causes error

    # Remove whitespaces in specified column for consistency
    remove_whitespace(prepped_df, col_2, data_2)

    # Change data type of specified columns
    change_cols_dtype(prepped_df, cols_2, d_type)

    # Make columns with date datetime datatype instead of object
    object_to_date(prepped_df, cols_3)

    # Change remaining object data type columns to string data type
    new_cols = []

    for col in prepped_df:
        if str(prepped_df[col].dtype) == 'object':
            new_cols.append(col)

    change_cols_dtype(prepped_df, [new_cols], 'str')

    return prepped_df


def add_col_subtraction(df, col_name, col_1, col_2):
    duration_values = (df[col_2] - df[col_1]).dt.days.astype('Int64')
    df.insert(df.columns.get_loc(col_2) + 1, col_name, duration_values)


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

    # for frame in dataframes:
    #     describe_df(frame)

    # print("No. of missing values in each dataframe:")
    # for frame2 in dataframes:
    #     print(missing_vals(frame2))
    # print(missing_vals(df_csv))

    # for frame3 in dataframes:   # Histograms
    #     plot_hist(frame3)

    # plot_boxplot(df_csv)        # Boxplots

    # # Line charts
    # plot_time_series(df_csv, "year", "participants_m")
    # plot_time_series(df_csv, "year", "participants_f")

    # Finding categorical data based on columns
    # identify_categorical(df_csv, 'type')
    # identify_categorical(df_csv, 'disabilities_included')

    df_csv_prepared = prep_data(df_csv,
                                ['URL', 'disabilities_included', 'highlights'],
                                [0, 17, 31],
                                'type', 'Summer', 'type', 'winter ',
                                ['countries', 'events', 'participants_m',
                                 'participants_f', 'participants'], 'int',
                                ['start', 'end'])

    # print(df_csv.columns)
    # print(df_csv_prepared.columns)

    # print(df_csv_prepared.head(3))  # Double checking drop worked
    # missing_vals(df_csv_prepared)   # Double checking rows with NaN are gone

    # Double checking decapitalising and whitespace removal
    # print(df_csv['type'].unique())
    # print(df_csv_prepared['type'].unique())

    # Double checking data type modification worked
    # print(df_csv.dtypes)
    # print(df_csv_prepared.dtypes)

    # print(df_csv['start'])
    # print(df_csv_prepared['start'])

    # print(df_csv['end'])
    # print(df_csv_prepared['end'])

    add_col_subtraction(df_csv_prepared, 'duration', 'start', 'end')

    # print(df_csv.columns)
    # print(df_csv_prepared.columns)
