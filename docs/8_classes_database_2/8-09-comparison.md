# Optional: Query complexity comparisons

Over the last few weeks in the tutorial sessions, students have asked about the impact of normalisation when it comes to
programming queries. This activity uses two extreme versions of the paralympics database to allow you to experience
the differences.

Using a database that is **not** normalised **not recommended**, please do not do this in your coursework. Normalisation
aims to reduce redundancy and increase data integrity.

## Databases

### Un-normalised ERD

[para-not-normalised.sqlite](../../src/activities/data/para-not-normalised.sqlite)

```mermaid
erDiagram
    Games {
        integer id PK
        text type
        integer year
        text country
        text host
        timestamp start
        timestamp end
        text disabilities_included
        real countries
        real events
        real sports
        real participants_m
        real participants_f
        real participants
        text highlights
        text URL
    }
    NPCCodes {
        text Code PK
        text Name
        text Region
        text SubRegion
        text MemberType
        text Notes
    }
```

### Normalised ERD

[para-normalised.db](../../src/activities/data/para-normalised.db)

```mermaid
erDiagram
    Country {
        text country
        integer id PK
    }
    Disability {
        text description
        integer id PK
    }
    Games {
        text type
        integer year
        text start
        text end
        integer countries
        integer events
        integer sports
        integer participants_m
        integer participants_f
        integer participants
        text highlights
        text URL
        integer id PK
    }
    GamesDisability {
        integer games_id
        integer disability_id
        integer id PK
    }
    GamesHost {
        integer games_id
        integer host_id
        integer id PK
    }
    GamesTeam {
        integer games_id
        text team_id
        integer id PK
    }
    Host {
        text place_name
        integer country_id
        integer id PK
    }
    Team {
        text name
        text region
        text sub_region
        text member_type
        text notes
        integer country_id
        text code PK
    }

    GamesDisability }|--|| Disability: "disability_id:id"
    GamesDisability }|--|| Games: "games_id:id"
    GamesHost }|--|| Games: "games_id:id"
    GamesHost }|--|| Host: "host_id:id"
    GamesTeam }|--|| Games: "games_id:id"
    GamesTeam }|--|| Team: "team_id:code"
    Host }|--|| Country: "country_id:id"
    Team }|--|| Country: "country_id:id"
```

## Activity

Try to write solutions to each of the following using both versions of the database.

Use SQLModel to write the queries. Please try at least 1 select and 1 update query.

Reflect on the implications for query complexity and data integrity.

1. List all Paralympics (games) with their year and type.
2. List all winter Paralympics (games) and include: host, year, number of participants.
3. Find all disabilities recorded in the database.
4. Get all Paralympics (Games) that took place after the year 2000.
5. Find all teams from a specific country (e.g. Canada).
6. List all hosts located in a specific country (e.g., 'Japan') and the year they held the Paralympics.
7. Show all Paralympics (games) along with their host city and host country.
8. List all disabilities associated with each Paralympics (games).
9. Find all teams that participated in a specific Paralympics (game) (e.g., Tokyo 2016).
10. Find all the Paralympics that have competitors who are 'Amputees'
11. **Update** all instances of the disability 'Les Autres' to 'Other'

NB: Normalisation aims to reduce redundancy and increase data integrity. Queries in this exercise may seem quicker and
simpler using the database that has not been normalised, however, using a database that is not normalised is
**not recommended**, so please do not do this in your coursework.
