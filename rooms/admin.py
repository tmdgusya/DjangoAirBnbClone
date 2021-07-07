from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """Item Admin Definition"""

    list_display = (
        "name",
        "used_by"
    )

    def used_by(self, obj):
        return obj.rooms.count()

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

    ordering = ('name', 'price')

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
        "count_amenities",
        "count_photos"
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

    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Photo Admin Definition"""
    pass
