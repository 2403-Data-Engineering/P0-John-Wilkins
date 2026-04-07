from models.classes import Classes
import data_layer.class_dao as class_dao

class ClassService:

    def get_all(self) -> list[Classes]:
        return class_dao.get_all()

    def get_by_id(self, class_id: int) -> Classes | None:
        return class_dao.get_by_id(class_id)

    def get_by_professor(self, professor_id: int) -> list[Classes]:
        return class_dao.get_by_professor(professor_id)

    def save(self, classes: Classes) -> Classes:
        return class_dao.save(classes)

    def update(self, classes: Classes) -> None:
        class_dao.update(classes)

    def delete(self, class_id: int) -> None:
        class_dao.delete(class_id)