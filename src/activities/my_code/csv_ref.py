from pathlib import Path
import pandas as pd

# This script is located in a subfolder so you need to navigate up to the
# parent (src) and then its parent (project root), then down to the 'data'
# directory and finally the .csv file
# paralympics_raw.csv filepath
csv_file = Path(__file__).parent.parent.joinpath('data', 'paralympics_raw.csv')
# also works
csv_file_v2 = Path(__file__).parent.parent / 'data' / 'paralympics_raw.csv'

# paralympics_all_raw.xlsx filepath
xlsx_file = Path(__file__).parent.parent.joinpath('data', 'paralympics_all_raw.xlsx')

# Check if the file exists
# if csv_file.exists():
#     print(f"CSV file found: {csv_file}")
# else:
#     print("CSV file not found.")


# if xlsx_file.exists():
#     print(f"CSV file found: {xlsx_file}")
# else:
#     print("CSV file not found.")

# Dataframes
df_csv = pd.read_csv(csv_file)
df_xlsx_games = pd.read_excel(xlsx_file)
df_xlsx_codes = pd.read_excel(xlsx_file, sheet_name="team_codes")
df_xlsx_standings = pd.read_excel(xlsx_file, sheet_name="medal_standings")
df_xlsx_summer = pd.read_excel(xlsx_file, sheet_name="games-team-summer")
df_xlsx_winter = pd.read_excel(xlsx_file, sheet_name="games-team-winter")
