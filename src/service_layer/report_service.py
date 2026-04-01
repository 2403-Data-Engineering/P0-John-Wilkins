# service_layer/report_service.py
from models.student import Student
from models.professor import Professor

class ReportService:
    def generate_student_report(self, student: Student):
        # For now, just print a simple report to the console
        print(f"--- Student Report for {student.first_name} {student.last_name} ---")
        print("Classes enrolled:")
        # Ideally, this would get the classes from EnrollmentService
        # Here we leave it as a placeholder

    def generate_professor_report(self, professor: Professor):
        print(f"--- Professor Report for {professor.first_name} {professor.last_name} ---")
        print("Classes taught:")
        # Placeholder for future implementation