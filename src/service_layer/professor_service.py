from models.professor import Professor
import data_layer.professor_dao as professor_dao

class ProfessorService:
    def __init__(self, professor_dao):
        self.professor_dao = professor_dao

    def get_all(self) -> list[Professor]:
        return self.professor_dao.get_all()

    def get_by_id(self, professor_id: int) -> Professor | None:
        return self.professor_dao.get_by_id(professor_id)

    def save(self, professor: Professor) -> Professor:
        return self.professor_dao.save(professor)

    def update(self, professor: Professor) -> None:
        self.professor_dao.update(professor)

    def delete(self, professor_id: int) -> None:
        self.professor_dao.delete(professor_id)