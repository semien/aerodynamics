from django.shortcuts import render, redirect
from .forms import AddForm, ProjectForm
from .algo.sector_calculation import calculate
from .algo.email_sender import send_message

from .models import Section, Project

from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

import logging

# @login_required
def home(request):
    section_form = AddForm()
    sections = Section.objects.all()
    return render(request, 'home.html', locals())


@require_POST
def add_section(request):
    form = AddForm(request.POST)

    if form.is_valid():
        new_section = Section()
        new_section.set(request.POST['section'])
        new_section.save()

    return redirect('home')

@login_required
def project_add_form(request):
    form = ProjectForm()
    return render(request, 'project_add.html', locals())

@login_required
def add_project(request):
    form = ProjectForm(request.POST)
    print(form)
    if form.is_valid():
        new_project = Project()
        new_project.user = request.user
        new_project.project_name = request.POST['project_name']
        new_project.type = request.POST['type']
        new_project.save()

    return redirect('home')

@login_required
def projects_page(request):
    projects = Project.objects.filter(user=request.user).order_by('update_time')
    return render(request, 'projects_page.html', locals())

def delete_all(request):
    Section.objects.all().delete()
    return redirect('home')


def calc(request):
    filename = 'answer.xlsx'
    calculate(Section.objects.all(), filename)
    send_message(filename)
    return redirect('home')

def project_page(request):
    return render(request, 'project_page.html', locals())
