from models.classes import Classes


class ClassService:
    def __init__(self):
        self.classes = [
            Classes(101, "Algorithms", 1),
            Classes(102, "Databases", 2),
            Classes(103, "Operating Systems", 1),
        ]

    def get_by_id(self, class_id: int):
        for c in self.classes:
            if c.id == class_id:
                return c
        return None
    def save(self, classes: Classes) -> Classes:
        print("TODO: Implement the class service save method....")
        print("...for now pretend that worked.")
        print("CLASS SAVED!")