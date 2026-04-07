# from models.student import Student
# from models.professor import Professor
# from models.classes import Classes
# from typing import List, Optional

# class EnrollmentService:
#     def __init__(self):
#         # List of (student, class) pairs
#         # self.enrollments = []

#     def is_enrolled(self, student: Student, class_obj: Classes) -> bool:
#         return (student, class_obj) in self.enrollments

#     def enroll(self, student: Student, class_obj: Classes):
#         if not self.is_enrolled(student, class_obj):
#             self.enrollments.append((student, class_obj))

#     def drop(self, student: Student, class_obj: Classes):
#         if self.is_enrolled(student, class_obj):
#             self.enrollments.remove((student, class_obj))

#     # ---- New Methods for Reports ----

#     def get_student_classes(self, student: Student) -> List[Classes]:
#         """
#         Return a list of Classes the student is enrolled in.
#         """
#         return [class_obj for s, class_obj in self.enrollments if s.id == student.id]

#     def get_professor_classes(self, professor: Professor) -> List[Classes]:
#         """
#         Return a list of Classes taught by the professor.
#         Assumes each class has a .professor attribute (optional for now)
#         """
#         # Only include classes that actually have this professor assigned
#         classes_taught = []
#         for _, class_obj in self.enrollments:
#             if hasattr(class_obj, "professor") and class_obj.professor is not None:
#                 if class_obj.professor.id == professor.id and class_obj not in classes_taught:
#                     classes_taught.append(class_obj)
#         return classes_taught
from models.student import Student
from models.professor import Professor
from models.classes import Classes
from typing import List


class EnrollmentService:
    def __init__(self, connection):
        """
        connection: a MySQL connection object
        """
        self.connection = connection

    # -----------------------------
    # Core Enrollment Operations
    # -----------------------------
    def enroll(self, student: Student, class_obj: Classes):
        if self.is_enrolled(student, class_obj):
            return

        query = """
        INSERT INTO enrollments (student_id, class_id)
        VALUES (%s, %s)
        """
        cursor = self.connection.cursor()
        cursor.execute(query, (student.student_id, class_obj.class_id))
        self.connection.commit()
        cursor.close()
        
    def is_enrolled(self, student: Student, class_obj: Classes) -> bool:
        query = """
        SELECT 1 FROM enrollments
        WHERE student_id = %s AND class_id = %s
        """
        cursor = self.connection.cursor()
        cursor.execute(query, (student.student_id, class_obj.class_id))
        result = cursor.fetchone()
        cursor.close()
        return result is not None

    

    def drop(self, student: Student, class_obj: Classes):
        query = """
        DELETE FROM enrollments
        WHERE student_id = %s AND class_id = %s
        """
        cursor = self.connection.cursor()
        cursor.execute(query, (student.student_id, class_obj.class_id))
        self.connection.commit()
        cursor.close()

    # -----------------------------
    # Query Methods (USED BY MENUS)
    # -----------------------------

    def get_classes_by_student(self, student_id: int) -> List[Classes]:
        """
        Returns all classes a student is enrolled in
        """
        query = """
        SELECT c.class_id, c.class_name, c.professor_id
        FROM classes c
        JOIN enrollments e ON c.class_id = e.class_id
        WHERE e.student_id = %s
        """
        cursor = self.connection.cursor()
        cursor.execute(query, (student_id,))
        results = cursor.fetchall()
        cursor.close()

        return [Classes(*row) for row in results]

    def get_students_by_class(self, class_id: int) -> List[Student]:
        """
        Returns all students enrolled in a class
        """
        query = """
        SELECT s.student_id, s.first_name, s.last_name, s.major, s.email, s.year
        FROM students s
        JOIN enrollments e ON s.student_id = e.student_id
        WHERE e.class_id = %s
        """
        cursor = self.connection.cursor()
        cursor.execute(query, (class_id,))
        results = cursor.fetchall()
        cursor.close()

        return [Student(*row) for row in results]

    # -----------------------------
    # Optional: Professor View
    # -----------------------------

    def get_professor_classes(self, professor: Professor) -> List[Classes]:
        """
        Returns all classes taught by a professor
        """
        query = """
        SELECT class_id, class_name, professor_id
        FROM classes
        WHERE professor_id = %s
        """
        cursor = self.connection.cursor()
        cursor.execute(query, (professor.professor_id,))
        results = cursor.fetchall()
        cursor.close()

        return [Classes(*row) for row in results]