
from .models import Teacher
from . import models
from django.shortcuts import render, get_object_or_404
from .models import Teacher, Education, Experience, Publication
def OfficeStaff(request):
    OfficeStaff=models.OfficeStaff.objects.all()
    return render(request,'OfficeStaff.html',{"data":OfficeStaff})


def teacherdetails(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    educations = Education.objects.filter(teacher=teacher)
    experiences = Experience.objects.filter(teacher=teacher)
    publications = Publication.objects.filter(teacher=teacher)
    return render(request, 'details.html', {'teacher': teacher, 'educations': educations, 'experiences': experiences, 'publications': publications})
def teacher(request):
    teachers = Teacher.objects.all()
    total_teachers = teachers.count()  
    return render(request, 'teacher.html', {"teachers": teachers, "total_teachers": total_teachers})
