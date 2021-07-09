from django.contrib import admin
from .models import Area, Coordinate, CropManagement, Field, GrowingCrop, ManagementGroup, Vegetable, Varietie

# Register your models here.
admin.site.register(Vegetable)
admin.site.register(Varietie)
admin.site.register(GrowingCrop)
admin.site.register(Coordinate)
admin.site.register(Field)
admin.site.register(Area)
admin.site.register(ManagementGroup)
admin.site.register(CropManagement)



