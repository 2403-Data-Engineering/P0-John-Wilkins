from dataclasses import dataclass


@dataclass
class Student:
    #add an id field to uniquely identify students
    first_name: str
    last_name: str
    major: str
    email: str
    year: str