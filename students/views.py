from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentForm

# function to view all students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'student': students})

# function to get student info
def student_info(request, pk): # pk (primary key; a unique identifier for students)
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_info.html', {'stuent': student})

# function to create new student
def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})

# function to update student info
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(isinstance=student)
    return render(request, 'students/student_form.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(student, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})