from data_layer.db_connection_manager import get_connection
from models.student import Student

class StudentDAO:
    def __init__(self, connection):
        # pass Connection is handled inside each function
        pass
    def get_all(self) -> list[Student]:
        with get_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM student")
            rows = cursor.fetchall()
            return [Student(r["student_id"], r["first_name"], r["last_name"], r["major"], r["email"], r["year"]) for r in rows]


    def get_by_id(self, student_id: int) -> Student | None:
        with get_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM student WHERE student_id = %s", [student_id])
            row = cursor.fetchone()
            if row is None:
                return None
            return Student(row["student_id"], row["first_name"], row["last_name"], row["major"], row["email"], row["year"])


    def save(self, student: Student) -> Student:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO student (first_name, last_name, major, email, year) VALUES (%s, %s, %s, %s, %s)",
                [student.first_name, student.last_name, student.major, student.email, student.year]
                )
            conn.commit()
            student.student_id = cursor.lastrowid
            return student


    def update(self, student: Student) -> None:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE student SET first_name=%s, last_name=%s, major=%s, email=%s, year=%s WHERE student_id=%s",
                [student.first_name, student.last_name, student.major, student.email, student.year, student.student_id]
                )
            conn.commit()


    def delete(self, student_id: int) -> None:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM student WHERE student_id = %s", [student_id])
            conn.commit()