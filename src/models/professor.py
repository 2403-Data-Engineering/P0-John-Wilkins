from dataclasses import dataclass


@dataclass
class Professor:
    #add an id field to uniquely identify professors
    first_name: str
    last_name: str
    department: str
    email: str
  