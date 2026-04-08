from models.classes import Classes
import data_layer.class_dao as class_dao

class ClassService:
    def __init__(self, class_dao):
        self.class_dao = class_dao
    def get_all(self) -> list[Classes]:
        return self.class_dao.get_all()

    def get_by_id(self, class_id: int) -> Classes | None:
        return self.class_dao.get_by_id(class_id)

    def get_by_professor(self, professor_id: int) -> list[Classes]:
        return self.class_dao.get_by_professor(professor_id)

    def save(self, classes: Classes) -> Classes:
        return self.class_dao.save(classes)

    def update(self, classes: Classes) -> None:
        self.class_dao.update(classes)

    def delete(self, class_id: int) -> None:
        self.class_dao.delete(class_id)