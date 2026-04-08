from data_layer.db_connection_manager import get_connection
from models.student import Student
from models.classes import Classes

class EnrollmentDAO:
    def __init__(self, connection):
        # pass Connection is handled inside each function
        pass
    def is_enrolled(student_id: int, class_id: int) -> bool:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT 1 FROM enrollment WHERE student_id = %s AND class_id = %s",
                [student_id, class_id]
            )
            return cursor.fetchone() is not None


    def enroll(student_id: int, class_id: int) -> None:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO enrollment (student_id, class_id) VALUES (%s, %s)",
                [student_id, class_id]
            )
            conn.commit()


    def drop(student_id: int, class_id: int) -> None:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM enrollment WHERE student_id = %s AND class_id = %s",
                [student_id, class_id]
            )
            conn.commit()


    def get_classes_for_student(student_id: int) -> list[Classes]:
        with get_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(
                """
                SELECT c.class_id, c.class_name, c.professor_id
                FROM class c
                JOIN enrollment e ON c.class_id = e.class_id
                WHERE e.student_id = %s
                """,
                [student_id]
            )
            rows = cursor.fetchall()
            return [Classes(r["class_id"], r["class_name"], r["professor_id"]) for r in rows]


    def get_students_in_class(class_id: int) -> list[Student]:
        with get_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(
                """
                SELECT s.student_id, s.first_name, s.last_name, s.major, s.email, s.year
                FROM student s
                JOIN enrollment e ON s.student_id = e.student_id
                WHERE e.class_id = %s
                """,
                [class_id]
            )
            rows = cursor.fetchall()
            return [Student(r["student_id"], r["first_name"], r["last_name"], r["major"], r["email"], r["year"]) for r in rows]