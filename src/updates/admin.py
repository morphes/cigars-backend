from django.contrib import admin
from .models import Update


@admin.register(Update)
class NotificationAdmin(admin.ModelAdmin):
    pass
