from dataclasses import dataclass


@dataclass
# class Student:
#     #add an id field to uniquely identify students
#     id: int
#     first_name: str
#     last_name: str
#     major: str
#     email: str
#     year: str
class Student:
    def __init__(self, id: int, first_name: str, last_name: str, major: str, email: str, year: str):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.email = email
        self.year = year