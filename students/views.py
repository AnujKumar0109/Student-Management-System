from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, Avg
from django.http import HttpResponse
from django.contrib.auth.models import User

from openpyxl import Workbook

from .models import Student


@login_required
def student_list(request):

    # HOST / ADMIN USER
    if request.user.is_staff:

        users = User.objects.filter(
            is_staff=False
        ).order_by("-date_joined")

        query = request.GET.get("q", "").strip()

        if query:
            users = users.filter(
                Q(username__icontains=query) |
                Q(email__icontains=query)
            )

        paginator = Paginator(users, 10)

        page_obj = paginator.get_page(
            request.GET.get("page")
        )

        return render(
            request,
            "students/student_list.html",
            {
                "users": page_obj,
                "page_obj": page_obj,
                "current_query": query,
                "is_host": True,
            }
        )

    # NORMAL USER
    students = Student.objects.filter(
        user=request.user
    )

    query = request.GET.get("q", "").strip()

    if query:
        students = students.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(roll_number__icontains=query) |
            Q(email__icontains=query) |
            Q(phone__icontains=query) |
            Q(course__icontains=query)
        )

    course = request.GET.get("course", "").strip()

    if course:
        students = students.filter(
            course=course
        )

    sort = request.GET.get(
        "sort",
        "-id"
    )

    allowed_sort = [
        "id",
        "-id",
        "first_name",
        "-first_name",
        "roll_number",
        "-roll_number",
        "age",
        "-age",
    ]

    if sort not in allowed_sort:
        sort = "-id"

    students = students.order_by(sort)

    courses = (
        Student.objects
        .filter(user=request.user)
        .values_list("course", flat=True)
        .distinct()
        .order_by("course")
    )

    paginator = Paginator(
        students,
        10
    )

    page_obj = paginator.get_page(
        request.GET.get("page")
    )

    return render(
        request,
        "students/student_list.html",
        {
            "students": page_obj,
            "page_obj": page_obj,
            "courses": courses,
            "current_query": query,
            "current_course": course,
            "current_sort": sort,
            "is_host": False,
        }
    )


@login_required
def profile(request):

    return render(
        request,
        "students/profile.html"
    )


@login_required
def dashboard(request):

    if request.user.is_staff:
        return redirect(
            "host_dashboard"
        )

    students = Student.objects.filter(
        user=request.user
    )

    total_students = students.count()

    total_courses = (
        students
        .values("course")
        .distinct()
        .count()
    )

    average_age = (
        students.aggregate(
            Avg("age")
        )["age__avg"] or 0
    )

    latest_students = students.order_by(
        "-id"
    )[:5]

    return render(
        request,
        "students/dashboard.html",
        {
            "total_students": total_students,
            "total_courses": total_courses,
            "average_age": average_age,
            "latest_students": latest_students,
        }
    )


@login_required
def student_add(request):

    # Host cannot add students
    if request.user.is_staff:
        messages.error(
            request,
            "Host cannot add students."
        )

        return redirect(
            "student_list"
        )

    if request.method == "POST":

        roll_number = request.POST.get(
            "roll_number",
            ""
        ).strip()

        email = request.POST.get(
            "email",
            ""
        ).strip()

        # Duplicate Roll Number
        if Student.objects.filter(
            roll_number=roll_number
        ).exists():

            messages.error(
                request,
                "Roll number already exists."
            )

            return redirect(
                "student_add"
            )

        # Duplicate Email
        if Student.objects.filter(
            email=email
        ).exists():

            messages.error(
                request,
                "Email already exists."
            )

            return redirect(
                "student_add"
            )

        Student.objects.create(
            user=request.user,
            first_name=request.POST.get(
                "first_name",
                ""
            ).strip(),
            last_name=request.POST.get(
                "last_name",
                ""
            ).strip(),
            roll_number=roll_number,
            email=email,
            phone=request.POST.get(
                "phone",
                ""
            ).strip(),
            course=request.POST.get(
                "course",
                ""
            ).strip(),
            age=request.POST.get(
                "age",
                ""
            ).strip(),
            address=request.POST.get(
                "address",
                ""
            ).strip(),
            date_of_birth=request.POST.get(
                "date_of_birth",
                ""
            ).strip(),
            image=request.FILES.get(
                "image"
            )
        )

        messages.success(
            request,
            "Student added successfully."
        )

        return redirect(
            "student_list"
        )

    return render(
        request,
        "students/student_form.html",
        {
            "student": None,
            "is_edit": False,
        }
    )


@login_required
def student_detail(request, pk):

    student = get_object_or_404(
        Student,
        pk=pk,
        user=request.user
    )

    return render(
        request,
        "students/student_detail.html",
        {
            "student": student
        }
    )


@login_required
def student_edit(request, pk):

    student = get_object_or_404(
        Student,
        pk=pk,
        user=request.user
    )

    if request.method == "POST":

        new_roll_number = request.POST.get(
            "roll_number",
            ""
        ).strip()

        new_email = request.POST.get(
            "email",
            ""
        ).strip()

        # Check duplicate roll number
        if Student.objects.filter(
            roll_number=new_roll_number
        ).exclude(
            pk=student.pk
        ).exists():

            messages.error(
                request,
                "Roll number already exists."
            )

            return redirect(
                "student_edit",
                pk=pk
            )

        # Check duplicate email
        if Student.objects.filter(
            email=new_email
        ).exclude(
            pk=student.pk
        ).exists():

            messages.error(
                request,
                "Email already exists."
            )

            return redirect(
                "student_edit",
                pk=pk
            )

        student.first_name = request.POST.get(
            "first_name",
            ""
        ).strip()

        student.last_name = request.POST.get(
            "last_name",
            ""
        ).strip()

        student.roll_number = new_roll_number

        student.email = new_email

        student.phone = request.POST.get(
            "phone",
            ""
        ).strip()

        student.course = request.POST.get(
            "course",
            ""
        ).strip()

        student.age = request.POST.get(
            "age",
            ""
        ).strip()

        student.address = request.POST.get(
            "address",
            ""
        ).strip()

        student.date_of_birth = request.POST.get(
            "date_of_birth",
            ""
        ).strip()

        new_image = request.FILES.get(
            "image"
        )

        if new_image:
            student.image = new_image

        student.save()

        messages.success(
            request,
            "Student updated successfully."
        )

        return redirect(
            "student_list"
        )

    return render(
        request,
        "students/student_form.html",
        {
            "student": student,
            "is_edit": True,
        }
    )


@login_required
def student_delete(request, pk):

    student = get_object_or_404(
        Student,
        pk=pk,
        user=request.user
    )

    if request.method == "POST":

        student.delete()

        messages.success(
            request,
            "Student deleted successfully."
        )

    return redirect(
        "student_list"
    )
@login_required
def export_students_excel(request):

    workbook = Workbook()
    worksheet = workbook.active

    # HOST / ADMIN
    if request.user.is_staff:

        users = User.objects.filter(
            is_staff=False
        ).order_by("-date_joined")

        worksheet.title = "Registered Users"

        worksheet.append([
            "Username",
            "Email",
            "Date Joined",
            "Last Login",
            "Status",
        ])

        for user in users:

            date_joined = user.date_joined

            if date_joined:
                date_joined = date_joined.replace(
                    tzinfo=None
                )

            last_login = user.last_login

            if last_login:
                last_login = last_login.replace(
                    tzinfo=None
                )

            status = (
                "Active"
                if user.is_active
                else "Inactive"
            )

            worksheet.append([
                user.username,
                user.email,
                date_joined,
                last_login,
                status,
            ])

        filename = "registered_users.xlsx"

    # NORMAL USER
    else:

        students = Student.objects.filter(
            user=request.user
        ).order_by("-id")

        worksheet.title = "Students"

        worksheet.append([
            "First Name",
            "Last Name",
            "Roll Number",
            "Email",
            "Phone",
            "Course",
            "Age",
            "Address",
            "Date of Birth",
        ])

        for student in students:

            worksheet.append([
                student.first_name,
                student.last_name,
                student.roll_number,
                student.email,
                student.phone,
                student.course,
                student.age,
                student.address,
                student.date_of_birth,
            ])

        filename = "students.xlsx"

    response = HttpResponse(
        content_type=(
            "application/vnd.openxmlformats-officedocument."
            "spreadsheetml.sheet"
        )
    )

    response["Content-Disposition"] = (
        f'attachment; filename="{filename}"'
    )

    workbook.save(response)

    return response


@login_required
def student_id_card(request, pk):

    student = get_object_or_404(
        Student,
        pk=pk,
        user=request.user
    )

    return render(
        request,
        "students/student_id_card.html",
        {
            "student": student
        }
    )


@login_required
def student_id_card_pdf(request, pk):

    student = get_object_or_404(
        Student,
        pk=pk,
        user=request.user
    )

    response = HttpResponse(
        content_type="application/pdf"
    )

    response["Content-Disposition"] = (
        f'attachment; filename="student_id_card_{student.roll_number}.pdf"'
    )

    return response


@login_required
def host_dashboard(request):

    if not request.user.is_staff:
        return redirect("student_list")

    total_users = User.objects.filter(
        is_staff=False
    ).count()

    total_students = Student.objects.count()

    total_courses = (
        Student.objects
        .values("course")
        .distinct()
        .count()
    )

    average_age = (
        Student.objects.aggregate(
            Avg("age")
        )["age__avg"] or 0
    )

    return render(
        request,
        "students/host_dashboard.html",
        {
            "total_users": total_users,
            "total_students": total_students,
            "total_courses": total_courses,
            "average_age": round(
                average_age,
                1
            ),
        }
    )