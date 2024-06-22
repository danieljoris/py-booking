import uuid


class Entity:
    __id: str

    def __init__(self):
        self.__id = str(uuid.uuid4())

    def __eq__(self, other):
        if not isinstance(other, Entity):
            return False
        return self.__id == other.id

    def __hash__(self):
        return hash(self.__id)

    @property
    def id(self) -> str:
        return self.__id
