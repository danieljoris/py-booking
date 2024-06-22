import re

from domain.value_objects.value_object import ValueObject


class Phone(ValueObject):
    def __init__(self, number: str):
        if not self._is_valid(number):
            raise ValueError(f"Invalid phone number: {number}")
        self.number = number

    @staticmethod
    def _is_valid(number: str) -> bool:
        pattern = r"^\+?[1-9]\d{1,14}$"
        return re.match(pattern, number) is not None

    def __eq__(self, other):
        if not isinstance(other, Phone):
            return False
        return self.number == other.number

    def __hash__(self):
        return hash(self.number)

    def __str__(self):
        return self.number
