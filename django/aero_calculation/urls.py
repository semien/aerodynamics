from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing, name='landing'),
    path('add', views.add_section, name='add'),
    path('delete_all', views.delete_all, name='delete_all'),
    path('calc', views.calc, name="calc")
]