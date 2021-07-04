from django.db import models
from core import models as core_model


class Rooms(core_model.TimeStampModel):

    """Room Model Definition"""

    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
