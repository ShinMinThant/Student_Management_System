from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Student
from .forms import StudentForm


@login_required
def student_list(request):
    query = request.GET.get('q', '')

    if query:
        students = Student.objects.filter(
            name__icontains=query
        ) | Student.objects.filter(
            student_id__icontains=query
        )
    else:
        students = Student.objects.all()

    total_students = students.count()

    paginator = Paginator(students, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'students/student_list.html', {
        'students': page_obj,
        'page_obj': page_obj,
        'query': query,
        'total_students': total_students
    })


@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Student added successfully!'
            )

            return redirect('student_list')

    else:
        form = StudentForm()

    return render(request, 'students/add_student.html', {
        'form': form
    })


@login_required
def student_detail(request, id):
    student = get_object_or_404(Student, id=id)

    return render(request, 'students/student_detail.html', {
        'student': student
    })


@login_required
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = StudentForm(
            request.POST,
            instance=student
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Student updated successfully!'
            )

            return redirect(
                'student_detail',
                id=student.id
            )

    else:
        form = StudentForm(instance=student)

    return render(request, 'students/edit_student.html', {
        'form': form,
        'student': student
    })


@login_required
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()

        messages.success(
            request,
            'Student deleted successfully!'
        )

        return redirect('student_list')

    return render(request, 'students/delete_student.html', {
        'student': student
    })


def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            messages.success(
                request,
                'Login successful!'
            )

            return redirect('dashboard')

        else:

            messages.error(
                request,
                'Invalid username or password.'
            )

    return render(
        request,
        'students/login.html'
    )


def logout_view(request):

    logout(request)

    messages.success(
        request,
        'You have been logged out.'
    )

    return redirect('login')


@login_required
def dashboard(request):
    total_students = Student.objects.count()

    recent_students = Student.objects.order_by(
        '-id'
    )[:5]

    latest_student = Student.objects.order_by(
        '-id'
    ).first()

    return render(request, 'students/dashboard.html', {
        'total_students': total_students,
        'recent_students': recent_students,
        'latest_student': latest_student,
    })