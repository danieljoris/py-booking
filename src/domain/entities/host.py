from datetime import datetime

from domain.entities.entity import Entity
from domain.enums.account_status import EAccountStatus
from domain.value_objects.address import Address
from domain.value_objects.email import Email
from domain.value_objects.phone import Phone


class Host(Entity):
    def __init__(
        self,
        name: str,
        email: Email,
        phone_number: Phone,
        address: Address,
        registered_at: datetime,
        account_status: EAccountStatus,
        bio: str = "",
        rating: float = 0.0,
        profile_picture: str = "",
    ):
        super().__init__()
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.registered_at = registered_at
        self.bio = bio
        self.rating = rating
        self.profile_picture = profile_picture
        self.account_status = account_status

    def update_rating(self, new_rating: float):
        if new_rating < 0 or new_rating > 5:
            raise ValueError("Rating must be between 0 and 5")
        self.rating = new_rating

    def deactivate(self):
        self.account_status = EAccountStatus.Deactivated

    def activate(self):
        self.account_status = EAccountStatus.Active

    def ban(self):
        self.account_status = EAccountStatus.PermanentlyBanned
