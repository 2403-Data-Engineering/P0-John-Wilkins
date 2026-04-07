from data_layer.db_connection_manager import get_connection
from models.professor import Professor

class ProfessorDAO:
    def __init__(self, connection):
        # pass Connection is handled inside each function
    def get_all() -> list[Professor]:
        with get_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM professor")
            rows = cursor.fetchall()
            return [Professor(r["professor_id"], r["first_name"], r["last_name"], r["department"], r["email"]) for r in rows]


    def get_by_id(professor_id: int) -> Professor | None:
        with get_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM professor WHERE professor_id = %s", [professor_id])
            row = cursor.fetchone()
            if row is None:
                return None
            return Professor(row["professor_id"], row["first_name"], row["last_name"], row["department"], row["email"])


    def save(professor: Professor) -> Professor:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO professor (first_name, last_name, department, email) VALUES (%s, %s, %s, %s)",
                [professor.first_name, professor.last_name, professor.department, professor.email]
            )
            conn.commit()
            professor.id = cursor.lastrowid
            return professor


    def update(professor: Professor) -> None:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE professor SET first_name=%s, last_name=%s, department=%s, email=%s WHERE professor_id=%s",
                [professor.first_name, professor.last_name, professor.department, professor.email, professor.id]
            )
            conn.commit()


    def delete(professor_id: int) -> None:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM professor WHERE professor_id = %s", [professor_id])
            conn.commit()