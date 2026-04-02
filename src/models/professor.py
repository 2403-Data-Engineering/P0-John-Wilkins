from dataclasses import dataclass


@dataclass
# class Professor:
#     #add an id field to uniquely identify professors
#     id: int
#     first_name: str
#     last_name: str
#     department: str
#     email: str
class Professor:
    def __init__(self, id: int, first_name: str, last_name: str, department: str, email: str):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.email = email