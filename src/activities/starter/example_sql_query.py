import sqlite3
from importlib import resources

from activities import data


def sample_select_queries(db_path):
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    # Select all rows and columns from the student table
    cur.execute('SELECT * FROM student')
    rows = cur.fetchall()  # Fetches more than 1 row
    print("\nAll rows and columns from the student table\n")
    for row in rows:
        print(row)

    # Select the student_id column
    cur.execute('SELECT student_id FROM student WHERE student_name="Alice Brown"')
    row = cur.fetchone()  # Fetches the first result
    print("\nSelect the student_id: \n", row[0])

    cur.execute('SELECT teacher_name, teacher_email FROM teacher WHERE teacher_id in (1, 2)')
    rows = cur.fetchall()  # Fetches all rows from the result
    print("\nTeacher name and email where the teacher is id 1 or 2\n")
    for row in rows:
        print(row)

    # All rows and columns from course table
    print("")
    cur.execute('SELECT * FROM course')
    rows_2 = cur.fetchall()
    for row_2 in rows_2:
        print(row_2)

    # Course code for chemistry course
    print("")
    cur.execute('SELECT course_code FROM course WHERE course_name="Chemistry"')
    print(cur.fetchall())

    # Courses with monday in their schedule
    print("")
    cur.execute('SELECT * FROM course WHERE course_schedule LIKE "%Mon%"')
    print(cur.fetchall())

    con.close()


def main():
    db_path = resources.files(data).joinpath("sample.db")
    sample_select_queries(db_path)


if __name__ == "__main__":
    main()
