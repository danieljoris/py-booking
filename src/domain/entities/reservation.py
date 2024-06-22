from datetime import datetime


class Reservation:

    def __init__(
        self,
        user_id: int,
        host_id: int,
        property_id: int,
        start_date: datetime,
        end_date: datetime,
        guests: int,
        total_price: float,
        status: str,
        user_comments: str = "",
        host_comments: str = "",
        payment_method: str = "",
    ):
        self.user_id = user_id
        self.host_id = host_id
        self.property_id = property_id
        self.start_date = start_date
        self.end_date = end_date
        self.guests = guests
        self.total_price = total_price
        self.status = status
        self.user_comments = user_comments
        self.host_comments = host_comments
        self.payment_method = payment_method
