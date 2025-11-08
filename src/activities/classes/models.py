from datetime import date

from sqlmodel import Field, SQLModel


class Games(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    type: str = Field()
    year: int
    start: date
    end: date
    countries: int
    events: int
    sports: int
    participants_m: int
    participants_f: int
    participants: int
    highlights: str
    URL: str


class Country(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    country: str


class Disability(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    description: str


class Team(SQLModel, table=True):
    code: str | None = Field(default=None, primary_key=True)
    name: str
    region: str = Field()
    sub_region: str
    member_type: str = Field()
    notes: str | None
    country_id: int = Field(foreign_key=True)
