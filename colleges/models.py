from django.db import models
from university.models import University


class College(models.Model):

    university = models.ForeignKey(
        University,
        on_delete=models.CASCADE,
        related_name="colleges"
    )

    name = models.CharField(max_length=200)

    code = models.CharField(
        max_length=20,
        unique=True
    )

    college_type = models.CharField(
        max_length=50
    )

    address = models.TextField()

    phone = models.CharField(
        max_length=15
    )

    email = models.EmailField()

    website = models.URLField(
        blank=True,
        null=True
    )

    principal_name = models.CharField(
        max_length=100
    )

    established_year = models.IntegerField()

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