from django.contrib import admin
from .models import Contact, ContactStatus


@admin.register(ContactStatus)
class ContactStatusAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "city", "status", "created_at")
    list_filter = ("status", "city")
    search_fields = ("first_name", "last_name", "email", "city")
