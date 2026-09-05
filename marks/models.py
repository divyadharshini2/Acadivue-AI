from django.db import models
from students.models import Student


class Mark(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    subject = models.CharField(max_length=100)

    internal_mark = models.IntegerField()

    assignment_mark = models.IntegerField()

    attendance_mark = models.IntegerField()

    semester_exam_mark = models.IntegerField()

    total = models.IntegerField()

    percentage = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.full_name} - {self.subject}"