from django.urls import path
from . import views
from .views import add_employee, manager_login, view_employees, update_employee

urlpatterns = [
    path('', views.home, name='home'),
    path('add_employee/', add_employee, name='add_employee'),
    path('manager_login/', manager_login, name='manager_login'),
    path('view_employees/', view_employees, name='view_employees'),
    path('update_employee/<int:employee_id>/', update_employee, name='update_employee'),
    path('add_manager/', views.add_manager, name='add_manager'),
]
