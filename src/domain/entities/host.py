from datetime import UTC, datetime

from src.seedwork.domain.entities import Entity
from src.domain.enums.account_status import EAccountStatus
from src.domain.value_objects.address import Address
from src.domain.value_objects.email import Email
from src.domain.value_objects.phone import Phone


class Host(Entity):
    def __init__(
        self,
        name: str,
        email: Email,
        phone_number: Phone,
        address: Address,
        bio: str = "",
        profile_picture: str = "",
    ):
        super().__init__()
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.registered_at = datetime.now(UTC)
        self.bio = bio
        self.profile_picture = profile_picture
        self.account_status = EAccountStatus.Active

    def update_rating(self, new_rating: float):
        if not new_rating > 0 or not new_rating <= 5:
            raise ValueError("Rating must be between 0 and 5")
        self.rating = new_rating

    def deactivate(self):
        self.account_status = EAccountStatus.Deactivated

    def activate(self):
        if self.account_status is EAccountStatus.PermanentlyBanned:
            raise ValueError("A permanently banned user cannot be activated.")

        self.account_status = EAccountStatus.Active

    def ban(self):
        self.account_status = EAccountStatus.PermanentlyBanned
