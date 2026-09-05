from django.db import models
from semesters.models import Semester


class Subject(models.Model):

    semester = models.ForeignKey(
        Semester,
        on_delete=models.CASCADE
    )

    subject_code = models.CharField(
        max_length=20,
        unique=True
    )

    subject_name = models.CharField(
        max_length=200
    )

    credits = models.IntegerField(
        default=3
    )

    subject_type = models.CharField(
        max_length=20,
        choices=[
            ("Theory", "Theory"),
            ("Practical", "Practical"),
            ("Project", "Project")
        ]
    )

    maximum_mark = models.IntegerField(
        default=100
    )

    pass_mark = models.IntegerField(
        default=40
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.subject_code} - {self.subject_name}"