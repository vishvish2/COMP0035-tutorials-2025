```mermaid
erDiagram
    Games {
        int type
        int year
        list[string] country
        list[string] host
        date start
        date end
        list[string] disabilities_included
        int countries
        int events
        int sports
        int participants_m
        int participants_f
        int participants
        string highlights
        string URL
    }

    Team {
        string code
        string name
        string region
        string sub_region
        string member_type
        string notes
    }

    Games }|--o{ Team: "A team competes in none or many games, a Games has 2 or more Teams competing in it"
```