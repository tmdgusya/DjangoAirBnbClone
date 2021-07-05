from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """Item Admin Definition"""
    pass


@admin.register(models.Rooms)
class RoomAdmin(admin.ModelAdmin):
    """Room Admin Definition"""

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        (
            "Times",
            {"fields": ("check_in", "check_out", "instant_book")}
        ),
        (
            "Spaces",
            {"fields": ("room_type", "amenities", "facilities", "house_rules")}
        ),
        (
            "More About The Space",
            {"fields": ("guests", "beds", "bedrooms", "bath")}
        ),
        (
            "Details",
            {"fields": ("host",)}
        )
    )

    list_display = (
        "name",
        "description",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "bath",
        "check_in",
        "check_out",
        "instant_book",
    )

    list_filter = (
        "city",
        "instant_book",
        "country",
        "room_type"
    )

    search_fields = ["name", "^host__username"]

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Photo Admin Definition"""
    pass
