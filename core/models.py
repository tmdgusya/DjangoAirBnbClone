from django.db import models


class TimeStampModel(models.Model):

    """TimeStampModel Definition"""

    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        abstract: True
