from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.add_section, name='add'),
    path('delete_all', views.delete_all, name='delete_all'),
    path('calc', views.calc, name="calc"),
    path('project_form', views.project_add_form, name="project_form"),
    path('add_project', views.add_project, name="add_project"),
    path('projects', views.projects_page, name="projects"),
    path('project', views.project_page, name="project"),
]