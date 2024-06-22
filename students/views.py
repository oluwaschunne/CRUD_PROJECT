from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentForm

#function to view all students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'student': students})
