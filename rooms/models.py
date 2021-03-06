from django.db import models
from django_countries.fields import CountryField
from core import models as core_model
from users import models as user_model


class AbstractItem(core_model.TimeStampModel):
    """Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract: True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    """RoomType Model Definition"""

    class Meta:
        verbose_name_plural = "Room Types"

    pass


class Amenity(AbstractItem):
    """Amenity Model Definition"""

    class Meta:
        verbose_name_plural = "Amenities"

    pass


class Facility(AbstractItem):
    """Facility Model Definition"""

    class Meta:
        verbose_name_plural = "Facilities"

    pass


class HouseRule(AbstractItem):
    """HouseRule Model Definition"""

    class Meta:
        verbose_name_plural = "House Rules"

    pass


class Rooms(core_model.TimeStampModel):
    """Room Model Definition"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    bath = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(user_model.User, related_name="rooms", on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, related_name="rooms", on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField(Amenity, related_name="rooms", blank=True)
    facilities = models.ManyToManyField(Facility, related_name="rooms", blank=True)
    house_rules = models.ManyToManyField(HouseRule, related_name="rooms", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Rooms"


class Photo(core_model.TimeStampModel):
    """Photo Model Definition"""

    caption = models.CharField(max_length=255)
    file = models.ImageField()
    room = models.ForeignKey(Rooms, related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
