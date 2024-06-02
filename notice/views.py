from django.shortcuts import render, redirect,HttpResponse
from django.urls import reverse_lazy
from . import forms 
from .models import event,notice,AdmissionNotice,Research
from . import models
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def admissionnotice(request):
    admission=models.AdmissionNotice.objects.all()
    return render(request,'admission.html',{"data":admission})

def programoffered(request):
    return render(request,'programoffered.html')

@login_required
def notice(request):
    notice=models.notice.objects.all()
    return render(request,'notice.html',{"data":notice})

@login_required
def event(request):
    event=models.event.objects.all()
    return render(request,'event.html',{"data":event})

@login_required
def research(request):
    research=models.Research.objects.all()
    return render(request,'research.html',{"data":research})

