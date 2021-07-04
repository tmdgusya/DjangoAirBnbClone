from django.db import models
from core import models as core_models
from users import models as user_models
from rooms import models as room_models


class Reviews(core_models.TimeStampModel):
    """Reviews Model Definition"""

    review = models.TextField()
    Accuracy = models.IntegerField()
    Communication = models.IntegerField()
    Cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    users = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    room = models.ForeignKey(room_models.Rooms, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Reviews"

    def __str__(self):
        return f'{self.review} - {self.room}'
