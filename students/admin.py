from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "first_name",
        "last_name",
        "roll_number",
        "email",
        "phone",
        "course",
        "age",
        "user",
    )

    search_fields = (
        "first_name",
        "last_name",
        "roll_number",
        "email",
        "phone",
        "course",
    )

    list_filter = (
        "course",
        "age",
    )

    ordering = (
        "-id",
    )
    
    readonly_fields = (
    "user",
    )
