from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import FieldOffice, RegionalOffice, HeadOffice, Issues


@admin.register(FieldOffice)
class FieldOfficeAdmin(OSMGeoAdmin):
    list_display = ('number_of_staff', 'tag', 'location')


@admin.register(RegionalOffice)
class RegionalOfficeAdmin(OSMGeoAdmin):
    list_display = ('number_of_staff', 'tag', 'location')


@admin.register(Issues)
class Issues(OSMGeoAdmin):
    list_display = ('issue', 'description')


@admin.register(HeadOffice)
class HeadOfficeAdmin(OSMGeoAdmin):
    list_display = ('number_of_staff', 'tag', 'location')