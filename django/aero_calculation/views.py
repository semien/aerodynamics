from django.shortcuts import render, redirect
from .forms import AddForm
from .algo.sector_calculation import calculate
from .algo.email_sender import send_message

from .models import Section

from django.views.decorators.http import require_POST


def landing(request):
    section_form = AddForm()
    sections = Section.objects.all()
    return render(request, 'landing.html', locals())


@require_POST
def add_section(request):
    form = AddForm(request.POST)

    if form.is_valid():
        new_section = Section()
        new_section.set(request.POST['section'])
        new_section.save()

    return redirect('landing')


def delete_all(request):
    Section.objects.all().delete()
    return redirect('landing')


def calc(request):
    filename = 'answer.xlsx'
    calculate(Section.objects.all(), filename)
    send_message(filename)
    return redirect('landing')
