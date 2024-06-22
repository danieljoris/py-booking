from enum import Enum


class EAccountStatus(str, Enum):
    Active = "active"
    Deactivated = "deactivated"
    PermanentlyBanned = "permanently_banned"
