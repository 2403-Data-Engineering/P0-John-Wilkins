from models.student import Student
import data_layer.student_dao as student_dao

VALID_YEARS = {"Freshman", "Sophomore", "Junior", "Senior"}

class StudentService:
   
    def __init__(self, student_dao):
        self.student_dao = student_dao
# View all students
    def get_all(self) -> list[Student]:
        return self.student_dao.get_all()
# Get a student by ID
    def get_by_id(self, student_id: int) -> Student | None:
        return self.student_dao.get_by_id(student_id)
# Create a new student, with validation for the year field
    def save(self, student: Student) -> Student:
        if student.year not in VALID_YEARS:
            raise ValueError(f"Invalid year '{student.year}'. Must be one of: {', '.join(VALID_YEARS)}")
        return self.student_dao.save(student)
     

# Update the student, with validation for the year field
    def update(self, student: Student) -> None:
        if student.year not in VALID_YEARS:
            raise ValueError(f"Invalid year '{student.year}'. Must be one of: {', '.join(VALID_YEARS)}")
        self.student_dao.update(student)
# Delete a student by ID
    def delete(self, student_id: int) -> None:
        self.student_dao.delete(student_id)