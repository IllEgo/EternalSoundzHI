from django.contrib import admin
from .models import Booking, LightPackage, SoundPackage, AddOn


# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    pass


@admin.register(LightPackage)
class LightPackageAdmin(admin.ModelAdmin):
    pass


@admin.register(SoundPackage)
class SoundPackageAdmin(admin.ModelAdmin):
    pass


@admin.register(AddOn)
class AddOnAdmin(admin.ModelAdmin):
    pass