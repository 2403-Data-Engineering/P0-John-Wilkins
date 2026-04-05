# Import the dataclass decorator from the dataclasses module
# This helps automatically generate common methods like __init__, __repr__, etc.
from dataclasses import dataclass


# The @dataclass decorator tells Python to treat this class as a data container
# It automatically creates an __init__ method and other useful methods for you
@dataclass
class Classes:
    def __init__(self, id: int, class_name: str, professor_id: int):
        self.id = id
        self.class_name = class_name
        self.professor_id = professor_id
        self.students = []