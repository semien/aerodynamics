from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.add_section, name='add'),
    path('delete_all', views.delete_all, name='delete_all'),
    path('calc', views.calc, name="calc"),
    path('project_form', views.project_form, name="project_form"),
]