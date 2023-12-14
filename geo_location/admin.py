from django.contrib import admin
from .models import GeoLocation

# @admin.site.register(GeoLocation)
class GeoLocationAdmin(admin.ModelAdmin):
    list_display = ("id","organization","longitude","latitude","country_name" ,"locality","address" )
    list_filter = ("longitude","latitude","country_name" ,"locality","address" ,"organization")
    search_fields = ("longitude","latitude","country_name" ,"locality","address" ,"organization")


admin.site.register(GeoLocation,GeoLocationAdmin)