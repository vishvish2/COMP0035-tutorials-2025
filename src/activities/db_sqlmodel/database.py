from __future__ import annotations
from sqlmodel import SQLModel, create_engine
from activities.db_sqlmodel.models import Games, Country, Disability, Team,\
    Host, GamesTeam, GamesDisability, GamesHost

engine = create_engine("sqlite:///paralympics_sqlmodel.db")

SQLModel.metadata.create_all(engine)
