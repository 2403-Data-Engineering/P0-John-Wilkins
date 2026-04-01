# service_layer/enrollment_service.py
from models.student import Student
from models.classes import Classes

class EnrollmentService:
    def __init__(self):
        # Keep a simple in-memory list of (student, class) pairs
        self.enrollments = []

    def is_enrolled(self, student: Student, class_obj: Classes) -> bool:
        return (student, class_obj) in self.enrollments

    def enroll(self, student: Student, class_obj: Classes):
        if not self.is_enrolled(student, class_obj):
            self.enrollments.append((student, class_obj))

    def drop(self, student: Student, class_obj: Classes):
        if self.is_enrolled(student, class_obj):
            self.enrollments.remove((student, class_obj))