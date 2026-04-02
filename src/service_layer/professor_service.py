from models.professor import Professor


class ProfessorService:
#add dummy data for testing purposes
    def __init__(self):
            self.professors = [
                Professor(1, "John", "Doe", "Computer Science", "jdoe@email.com"),
                Professor(2, "Jane", "Smith", "Mathematics", "jsmith@email.com")
            ]

    def get_by_id(self, professor_id: int):
        for professor in self.professors:
            if professor.id == professor_id:
                return professor
        return None

    def save(self, professor: Professor) -> Professor:
        print("TODO: Implement the professor service save method....")
        print("...for now pretend that worked.")
        print("PROFESSOR SAVED!")