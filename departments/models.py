from django.db import models
from colleges.models import College


class Department(models.Model):

    college = models.ForeignKey(
        College,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=100)

    code = models.CharField(max_length=20)

    hod_name = models.CharField(
        max_length=100,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.college.name} - {self.name}"