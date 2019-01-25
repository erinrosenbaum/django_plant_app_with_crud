from django.contrib import admin

from . import models

admin.site.register(models.Plant)
admin.site.register(models.Use)
admin.site.register(models.Genus)
