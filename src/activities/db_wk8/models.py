""" SQLModel classes for the students database. """
from sqlmodel import Field, Relationship, SQLModel


class Location(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    room: str

    courses: list["Course"] = Relationship(back_populates="location")


class Student(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    student_name: str
    student_email: str

    enrollments: list["Enrollment"] = Relationship(back_populates="student")


class Teacher(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    teacher_name: str
    teacher_email: str

    enrollments: list["Enrollment"] = Relationship(back_populates="teacher")


class Course(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    course_name: str
    course_code: int
    course_schedule: str | None = None
    location_id: int | None = Field(foreign_key="location.id")
    location: Location | None = Relationship(back_populates="courses")

    enrollments: list["Enrollment"] = Relationship(back_populates="course")


class Enrollment(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    student_id: int | None = Field(foreign_key="student.id")
    course_id: int | None = Field(foreign_key="course.id")
    teacher_id: int | None = Field(foreign_key="teacher.id")

    student: Student = Relationship(back_populates="enrollments")
    course: Course = Relationship(back_populates="enrollments")
    teacher: Teacher = Relationship(back_populates="enrollments")
