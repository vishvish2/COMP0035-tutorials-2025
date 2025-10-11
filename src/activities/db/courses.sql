-- courses
PRAGMA foreign_keys = ON;
/*
```mermaid
    erDiagram
        Teachers{
            int id PK
            string teacher_name
            string teacher_email
        }
*/
CREATE TABLE teacher
(
    id INTEGER PRIMARY KEY,
    teacher_name TEXT,
    teacher_email TEXT
);
/*

        Students{
            int id PK
            string student_name
            string student_email
        }
*/
CREATE TABLE student
(
    id INTEGER PRIMARY KEY,
    student_name TEXT,
    student_email TEXT
);
/*
        Courses{
            int id PK
            string course_name
            string course_code
            string course_schedule
            string course_location
            int teacher_id FK
        }
*/
CREATE TABLE course
(
    id INTEGER PRIMARY KEY,
    course_name TEXT,
    course_code TEXT,
    course_schedule TEXT,
    course_location TEXT,
    teacher_id INTEGER, FOREIGN KEY (teacher_id) REFERENCES teacher
);
/*
        Classes{
            int id PK
            int student_id FK
            int course_id FK
        }
*/
CREATE TABLE enrollment
(
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course_id INTEGER,
    teacher_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES student,
    FOREIGN KEY (course_id) REFERENCES course,
    FOREIGN KEY (teacher_id) REFERENCES teacher
);
