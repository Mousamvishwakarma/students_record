from django.shortcuts import render, get_object_or_404, redirect
from .models import Student


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_records/student_list.html', {'students': students})


def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'student_records/student_detail.html', {'student': student})


def student_add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        course = request.POST.get('course')
        admission_date = request.POST.get('admission_date')

        Student.objects.create(name=name, age=age, gender=gender, email=email, phone=phone, address=address, course=course, admission_date=admission_date)
        return redirect('student_list')

    return render(request, 'student_records/student_form.html')


def student_edit(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        student.gender = request.POST.get('gender')
        student.email = request.POST.get('email')
        student.phone = request.POST.get('phone')
        student.address = request.POST.get('address')
        student.course = request.POST.get('course')
        student.admission_date = request.POST.get('admission_date')
        student.save()
        return redirect('student_list')

    return render(request, 'student_records/student_form.html', {'student': student})


def student_delete(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('student_list')

