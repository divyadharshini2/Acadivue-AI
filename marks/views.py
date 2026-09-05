from django.shortcuts import render, redirect
from .models import Mark
from students.models import Student


def mark_list(request):

    marks = Mark.objects.all()

    return render(request, "marks/mark_list.html", {
        "marks": marks
    })


def add_mark(request):

    students = Student.objects.all()

    if request.method == "POST":

        student = Student.objects.get(id=request.POST.get("student"))

        subject = request.POST.get("subject")
        internal = int(request.POST.get("internal_mark"))
        assignment = int(request.POST.get("assignment_mark"))
        attendance = int(request.POST.get("attendance_mark"))
        semester = int(request.POST.get("semester_exam_mark"))

        total = internal + assignment + attendance + semester
        percentage = total

        Mark.objects.create(
            student=student,
            subject=subject,
            internal_mark=internal,
            assignment_mark=assignment,
            attendance_mark=attendance,
            semester_exam_mark=semester,
            total=total,
            percentage=percentage
        )

        return redirect("mark_list")

    return render(request, "marks/add_mark.html", {
        "students": students
    })