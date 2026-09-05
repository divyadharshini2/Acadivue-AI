from django.db import models
from departments.models import Department


class Semester(models.Model):

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )

    semester_number = models.IntegerField()

    academic_year = models.CharField(
        max_length=20
    )

    regulation = models.CharField(
        max_length=20,
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.department.name} - Semester {self.semester_number}"