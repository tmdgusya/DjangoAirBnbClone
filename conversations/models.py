from django.db import models
from core import models as core_models
from users import models as user_models


class Conversation(core_models.TimeStampModel):
    """Conversation Model Definition"""

    participants = models.ManyToManyField(user_models.User, blank=True)

    def __str__(self):
        return self.created_at


class Message(core_models.TimeStampModel):
    text = models.TextField()
    sender = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    conversations = models.ForeignKey(Conversation, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.sender} : {self.text}'
