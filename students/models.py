from django.db import models


class Student(models.Model):

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    YEAR_CHOICES = [
        ("I", "I"),
        ("II", "II"),
        ("III", "III"),
        ("IV", "IV"),
    ]

    SEMESTER_CHOICES = [
        ("1", "Semester 1"),
        ("2", "Semester 2"),
        ("3", "Semester 3"),
        ("4", "Semester 4"),
        ("5", "Semester 5"),
        ("6", "Semester 6"),
        ("7", "Semester 7"),
        ("8", "Semester 8"),
    ]

    full_name = models.CharField(max_length=100)
    register_number = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    year = models.CharField(max_length=5, choices=YEAR_CHOICES)
    semester = models.CharField(max_length=5, choices=SEMESTER_CHOICES)
    section = models.CharField(max_length=5)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name