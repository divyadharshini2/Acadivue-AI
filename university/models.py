from django.db import models


class University(models.Model):

    UNIVERSITY_TYPES = [
        ("State", "State"),
        ("Central", "Central"),
        ("Autonomous", "Autonomous"),
        ("Deemed", "Deemed"),
        ("Private", "Private"),
    ]

    CGPA_SCALES = [
        ("10", "10 Point"),
        ("4", "4 Point"),
    ]

    name = models.CharField(max_length=200)

    code = models.CharField(
        max_length=20,
        unique=True
    )

    university_type = models.CharField(
        max_length=20,
        choices=UNIVERSITY_TYPES
    )

    total_semesters = models.IntegerField()

    cgpa_scale = models.CharField(
        max_length=5,
        choices=CGPA_SCALES
    )

    website = models.URLField(
        blank=True,
        null=True
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=15
    )

    address = models.TextField()

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name