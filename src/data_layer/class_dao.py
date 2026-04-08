from data_layer.db_connection_manager import get_connection
from models.classes import Classes

class ClassDAO:
    def __init__(self, connection):
        # pass Connection is handled inside each function
        pass
    def get_all(self) -> list[Classes]:
        with get_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM class")
            rows = cursor.fetchall()
            return [Classes(r["class_id"], r["class_name"], r["professor_id"]) for r in rows]


    def get_by_id(self, class_id: int) -> Classes | None:
        with get_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM class WHERE class_id = %s", [class_id])
            row = cursor.fetchone()
            if row is None:
                return None
            return Classes(row["class_id"], row["class_name"], row["professor_id"])


    def get_by_professor(self, professor_id: int) -> list[Classes]:
        with get_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM class WHERE professor_id = %s", [professor_id])
            rows = cursor.fetchall()
            return [Classes(r["class_id"], r["class_name"], r["professor_id"]) for r in rows]


    def save(self, classes: Classes) -> Classes:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO class (class_name, professor_id) VALUES (%s, %s)",
                [classes.class_name, classes.professor_id]
            )
            conn.commit()
            classes.class_id = cursor.lastrowid
            return classes


    def update(self, classes: Classes) -> None:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE class SET class_name=%s, professor_id=%s WHERE class_id=%s",
                [classes.class_name, classes.professor_id, classes.class_id]
            )
            conn.commit()


    def delete(self, class_id: int) -> None:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM class WHERE class_id = %s", [class_id])
            conn.commit()