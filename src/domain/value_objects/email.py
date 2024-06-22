import re


class Email:
    def __init__(self, address: str):
        if not self._is_valid(address):
            raise ValueError(f"Invalid email address: {address}")
        self.address = address

    @staticmethod
    def _is_valid(address: str) -> bool:
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, address) is not None

    def __eq__(self, other):
        if not isinstance(other, Email):
            return False
        return self.address == other.address

    def __hash__(self):
        return hash(self.address)

    def __str__(self):
        return self.address
