from django.contrib import admin
from .models import University


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "code",
        "university_type",
        "total_semesters",
        "cgpa_scale",
        "is_active",
    )

    list_filter = (
        "university_type",
        "cgpa_scale",
        "is_active",
    )

    search_fields = (
        "name",
        "code",
        "email",
    )