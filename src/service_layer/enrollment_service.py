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
    from models.student import Student
from models.professor import Professor
from models.classes import Classes
from typing import List, Optional

class EnrollmentService:
    def __init__(self):
        # List of (student, class) pairs
        self.enrollments = []

    def is_enrolled(self, student: Student, class_obj: Classes) -> bool:
        return (student, class_obj) in self.enrollments

    def enroll(self, student: Student, class_obj: Classes):
        if not self.is_enrolled(student, class_obj):
            self.enrollments.append((student, class_obj))

    def drop(self, student: Student, class_obj: Classes):
        if self.is_enrolled(student, class_obj):
            self.enrollments.remove((student, class_obj))

    # ---- New Methods for Reports ----

    def get_student_classes(self, student: Student) -> List[Classes]:
        """
        Return a list of Classes the student is enrolled in.
        """
        return [class_obj for s, class_obj in self.enrollments if s.id == student.id]

    def get_professor_classes(self, professor: Professor) -> List[Classes]:
        """
        Return a list of Classes taught by the professor.
        Assumes each class has a .professor attribute (optional for now)
        """
        # Only include classes that actually have this professor assigned
        classes_taught = []
        for _, class_obj in self.enrollments:
            if hasattr(class_obj, "professor") and class_obj.professor is not None:
                if class_obj.professor.id == professor.id and class_obj not in classes_taught:
                    classes_taught.append(class_obj)
        return classes_taught