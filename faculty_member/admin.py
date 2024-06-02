from django.contrib import admin

# Register your models here.
from . import models
admin.site.register(models.Teacher)
admin.site.register(models.OfficeStaff)
admin.site.register(models.Education)
admin.site.register(models.Experience)
admin.site.register(models.Publication)