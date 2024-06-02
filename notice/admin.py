from django.contrib import admin

# Register your models here.
from . import models
admin.site.register(models.notice)
admin.site.register(models.event)
admin.site.register(models.AdmissionNotice)
admin.site.register(models.Research)