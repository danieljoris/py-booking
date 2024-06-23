from dataclasses import dataclass


@dataclass(frozen=True)
class Address:
    street: str
    city: str
    state: str
    country: str
    zip_code: str

    def __post_init__(self):
        if not self._is_valid(self.street, self.city, self.state, self.country, self.zip_code):
            raise ValueError("Invalid address")

    @staticmethod
    def _is_valid(street: str, city: str, state: str, country: str, zip_code: str) -> bool:
        # Simplistic validation, can be improved
        return all([street, city, state, country, zip_code])

    def __eq__(self, other):
        if not isinstance(other, Address):
            return False
        return (
            self.street == other.street
            and self.city == other.city
            and self.state == other.state
            and self.country == other.country
            and self.zip_code == other.zip_code
        )

    def __hash__(self):
        return hash((self.street, self.city, self.state, self.country, self.zip_code))

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.country}, {self.zip_code}"
