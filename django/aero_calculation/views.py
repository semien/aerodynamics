from django.shortcuts import render, redirect
from .forms import AddForm, ProjectForm
from .algo.sector_calculation import calculate
from .algo.email_sender import send_message

from .models import Section

from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

import logging

# @login_required
def home(request):
    section_form = AddForm()
    sections = Section.objects.all()
    return render(request, 'home.html', locals())


# def registration(request):
#     objs = User.objects.all()
#     registration_form = RegistrationForm()
#     return render(request, 'registration.html', locals())
#


@require_POST
def add_section(request):
    form = AddForm(request.POST)

    if form.is_valid():
        new_section = Section()
        new_section.set(request.POST['section'])
        new_section.save()

    return redirect('home')


def delete_all(request):
    Section.objects.all().delete()
    return redirect('home')


def calc(request):
    filename = 'answer.xlsx'
    calculate(Section.objects.all(), filename)
    send_message(filename)
    return redirect('home')

def project_form(request):
    form = ProjectForm
    return render(request, 'project_form.html', locals())
