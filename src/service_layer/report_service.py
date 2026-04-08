# # service_layer/report_service.py
# from models.student import Student
# from models.professor import Professor

# class ReportService:
#     def generate_student_report(self, student: Student):
#         # For now, just print a simple report to the console
#         print(f"--- Student Report for {student.first_name} {student.last_name} ---")
#         print("Classes enrolled:")
#         # Ideally, this would get the classes from EnrollmentService
#         # Here we leave it as a placeholder

#     def generate_professor_report(self, professor: Professor):
#         print(f"--- Professor Report for {professor.first_name} {professor.last_name} ---")
#         print("Classes taught:")
#         # Placeholder for future implementation
from models.student import Student
from models.professor import Professor
from models.classes import Classes
import os

class ReportService:
    def __init__(self, enrollment_service):
        self.enrollment_service = enrollment_service
        # Folder to save reports
        self.report_dir = "reports"
        if not os.path.exists(self.report_dir):
            os.makedirs(self.report_dir)

    def generate_student_report(self, student: Student):
        """
        Generate an HTML report for a student listing all classes they are enrolled in.
        """
        # Get classes from EnrollmentService
        classes = self.enrollment_service.get_classes_by_student(student.student_id)

        # Build HTML content
        html_content = f"""
        <html>
        <head>
            <title>Student Report - {student.first_name} {student.last_name}</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                h1 {{ color: #2c3e50; }}
                table {{ border-collapse: collapse; width: 50%; }}
                th, td {{ border: 1px solid #ddd; padding: 8px; }}
                th {{ background-color: #f2f2f2; }}
            </style>
        </head>
        <body>
            <h1>Student Report: {student.first_name} {student.last_name}</h1>
            <p><strong>Major:</strong> {student.major}</p>
            <p><strong>Year:</strong> {student.year}</p>
            <h2>Enrolled Classes</h2>
            <table>
                <tr>
                    <th>Class ID</th>
                    <th>Class Name</th>
                </tr>
        """

        if classes:
            for cls in classes:
                html_content += f"""
                <tr>
                    <td>{cls.class_id}</td>
                    <td>{cls.class_name}</td>
                </tr>
                """
        else:
            html_content += """
                <tr>
                    <td colspan="2">No classes enrolled</td>
                </tr>
            """

        html_content += """
            </table>
        </body>
        </html>
        """

        # Save to file
        file_path = os.path.join(self.report_dir, f"student_{student.student_id}.html")
        with open(file_path, "w") as f:
            f.write(html_content)

        print(f"Student report generated: {file_path}")


    def generate_professor_report(self, professor: Professor):
        """
        Generate an HTML report for a professor listing all classes they teach.
        """
        classes = self.enrollment_service.get_professor_classes(professor)

        html_content = f"""
        <html>
        <head>
            <title>Professor Report - {professor.first_name} {professor.last_name}</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                h1 {{ color: #2c3e50; }}
                table {{ border-collapse: collapse; width: 50%; }}
                th, td {{ border: 1px solid #ddd; padding: 8px; }}
                th {{ background-color: #f2f2f2; }}
            </style>
        </head>
        <body>
            <h1>Professor Report: {professor.first_name} {professor.last_name}</h1>
            <p><strong>Department:</strong> {professor.department}</p>
            <h2>Classes Taught</h2>
            <table>
                <tr>
                    <th>Class ID</th>
                    <th>Class Name</th>
                </tr>
        """

        if classes:
            for cls in classes:
                html_content += f"""
                <tr>
                    <td>{cls.class_id}</td>
                    <td>{cls.class_name}</td>
                </tr>
                """
        else:
            html_content += """
                <tr>
                    <td colspan="2">No classes assigned</td>
                </tr>
            """

        html_content += """
            </table>
        </body>
        </html>
        """

        # Save to file
        file_path = os.path.join(self.report_dir, f"professor_{professor.professor_id}.html")
        with open(file_path, "w") as f:
            f.write(html_content)

        print(f"Professor report generated: {file_path}")