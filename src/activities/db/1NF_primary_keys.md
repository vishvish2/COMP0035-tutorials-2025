```mermaid
erDiagram
    Games {
        int games_id PK
    }
    Team {
        string code PK
    }
    Games }|--o{ Team: ""

```
