from django.shortcuts import render, redirect
from .models import Student


def student_list(request):
    students = Student.objects.all()
    return render(request, "students/student_list.html", {
        "students": students
    })


def add_student(request):

    if request.method == "POST":

        Student.objects.create(
            full_name=request.POST.get("full_name"),
            register_number=request.POST.get("register_number"),
            email=request.POST.get("email"),
            department=request.POST.get("department"),
            year=request.POST.get("year"),
            semester=request.POST.get("semester"),
            section=request.POST.get("section"),
            gender=request.POST.get("gender"),
            date_of_birth=request.POST.get("date_of_birth"),
            phone=request.POST.get("phone"),
            address=request.POST.get("address"),
        )

        return redirect("student_list")

    return render(request, "students/add_student.html")

def edit_student(request, id):

    student = Student.objects.get(id=id)

    if request.method == "POST":

        student.full_name = request.POST.get("full_name")
        student.register_number = request.POST.get("register_number")
        student.email = request.POST.get("email")
        student.department = request.POST.get("department")
        student.year = request.POST.get("year")
        student.semester = request.POST.get("semester")
        student.section = request.POST.get("section")
        student.gender = request.POST.get("gender")
        student.date_of_birth = request.POST.get("date_of_birth")
        student.phone = request.POST.get("phone")
        student.address = request.POST.get("address")

        student.save()

        return redirect("student_list")

    return render(request, "students/edit_student.html", {
        "student": student
    })


def delete_student(request, id):

    student = Student.objects.get(id=id)
    student.delete()

    return redirect("student_list")