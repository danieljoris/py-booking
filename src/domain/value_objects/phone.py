import re

from src.seedwork.domain.value_objects import ValueObject


class Phone(ValueObject):
    value: str

    def __init__(self, value: str):
        if not self._is_valid(value):
            raise ValueError(f"Invalid phone number: {value}")
        object.__setattr__(self, "value", value)

    @staticmethod
    def _is_valid(value: str) -> bool:
        pattern = r"^\+?[1-9]\d{1,14}$"
        return re.match(pattern, value) is not None

    def __eq__(self, other):
        if not isinstance(other, Phone):
            return False
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __str__(self):
        return self.value
