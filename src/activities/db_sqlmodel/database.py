from __future__ import annotations
from pathlib import Path
from sqlmodel import Session, SQLModel, create_engine
from activities.db_sqlmodel.models import Games, Country, Disability, Team, \
    Host, GamesTeam, GamesDisability, GamesHost

import pandas as pd

engine = create_engine("sqlite:///paralympics_sqlmodel.db")

SQLModel.metadata.create_all(engine)

# 1. Read Excel file
csv_file = Path(__file__).parent.parent.joinpath('data', 'paralympics_raw.csv')
df = pd.read_csv(csv_file)

# 2. Convert DataFrame rows of values to SQLModel instances
records = []
classes = [Games, Country, Disability, Team, Host, GamesTeam, GamesDisability,
           GamesHost]
for table in classes:
    for _, row in df.iterrows():
        record = table(**row.to_dict())
        records.append(record)

    # 3. Insert into database
    engine = create_engine("sqlite:///paralympics_sqlmodel.db")
    with Session(engine) as session:
        session.add_all(records)
        session.commit()
