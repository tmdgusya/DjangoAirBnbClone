from django.db import models
from core import models as core_models
from users import models as user_models
from rooms import models as room_models


class Reservation(core_models.TimeStampModel):
    """Reservation Model Definition"""

    STATUS_PENDING = "PENDING"
    STATUS_CONFIRM = "CONFIRM"
    STATUS_CANCELED = "CANCELED"

    STATUS_CHOICES = (
        (STATUS_PENDING, "PENDING"),
        (STATUS_CONFIRM, "CONFIRM"),
        (STATUS_CANCELED, "CANCELED")
    )

    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDING)
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    room = models.ForeignKey(room_models.Rooms, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.room} - {self.check_in}'
