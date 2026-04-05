# from models.student import Student


# class StudentService:
    
# #add dummy data for testing purposes
#     def __init__(self):
#         self.students = [
#                 Student(1, "Alice", "Johnson", "CS", "alice@email.com", "Senior"),
#                 Student(2, "Bob", "Smith", "Math", "bob@email.com", "Junior"),
#                 Student(3, "Charlie", "Brown", "Physics", "charlie@email.com", "Sophomore")
#             ]
#     def get_by_id(self, student_id: int):
#             for student in self.students:
#                 if student.id == student_id:   
#                     return student
#             return None
# # This method is a placeholder for saving a student to the database.
# # In a real implementation, this would involve database operations.
#     def save(self, student: Student) -> Student:
#         print("TODO: Implement the student service save method....")
#         print("...for now pretend that worked.")
#         print("STUDENT SAVED!")
from models.student import Student
import data_layer.student_dao as student_dao

VALID_YEARS = {"Freshman", "Sophomore", "Junior", "Senior"}

class StudentService:

    def get_all(self) -> list[Student]:
        return student_dao.get_all()

    def get_by_id(self, student_id: int) -> Student | None:
        return student_dao.get_by_id(student_id)

    def save(self, student: Student) -> Student:
        if student.year not in VALID_YEARS:
            raise ValueError(f"Invalid year '{student.year}'. Must be one of: {', '.join(VALID_YEARS)}")
        return student_dao.save(student)

    def update(self, student: Student) -> None:
        if student.year not in VALID_YEARS:
            raise ValueError(f"Invalid year '{student.year}'. Must be one of: {', '.join(VALID_YEARS)}")
        student_dao.update(student)

    def delete(self, student_id: int) -> None:
        student_dao.delete(student_id)