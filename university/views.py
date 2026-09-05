from django.shortcuts import render, redirect, get_object_or_404
from .models import University


def university_list(request):

    universities = University.objects.all()

    return render(request, "university/university_list.html", {
        "universities": universities
    })


def add_university(request):

    if request.method == "POST":

        University.objects.create(

            name=request.POST.get("name"),
            code=request.POST.get("code"),
            university_type=request.POST.get("university_type"),
            total_semesters=request.POST.get("total_semesters"),
            cgpa_scale=request.POST.get("cgpa_scale"),
            website=request.POST.get("website"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            address=request.POST.get("address"),
            is_active=True

        )

        return redirect("university_list")

    return render(request, "university/add_university.html")


def edit_university(request, id):

    university = get_object_or_404(University, id=id)

    if request.method == "POST":

        university.name = request.POST.get("name")
        university.code = request.POST.get("code")
        university.university_type = request.POST.get("university_type")
        university.total_semesters = request.POST.get("total_semesters")
        university.cgpa_scale = request.POST.get("cgpa_scale")
        university.website = request.POST.get("website")
        university.email = request.POST.get("email")
        university.phone = request.POST.get("phone")
        university.address = request.POST.get("address")

        university.save()

        return redirect("university_list")

    return render(request, "university/edit_university.html", {
        "university": university
    })


def delete_university(request, id):

    university = get_object_or_404(University, id=id)

    university.delete()

    return redirect("university_list")