from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import User, Employee, Manager,UserRole
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect

def add_manager(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Create user with role as 'Manager'
        user = User.objects.create_user(
            email=email,
            password=password,
            name=name,
        )
        
        manager_role = UserRole.objects.get(role_name="Manager")

        # Assign the 'Manager' role to the user
        user.role = manager_role
        user.save()

        Manager.objects.create(user=user)

        
        return redirect('home')  

    return render(request, 'accounts/add_manager.html')


def home(request):
    employees = Employee.objects.all()
    return render(request, 'accounts/home.html', {'employees': employees})


def manager_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, email=username, password=password)
        if user is not None:
            if user.is_staff:
                if user.role.role_name == "Manager":
                    login(request, user)
                    return redirect('view_employees')
                elif user.role.role_name == "admin":
                    return render(request, 'accounts/add_manager.html')
            else:
                return render(request, 'accounts/manager_login.html', {'error_message': 'Invalid credentials'})
    return render(request, 'accounts/manager_login.html')

# @login_required
def view_employees(request):
    employees = Employee.objects.all()
    return render(request, 'accounts/view_employees.html', {'employees': employees})


def add_employee(request):
    if request.method == 'POST':
        user_email = request.POST.get('user_email')
        manager_email = request.POST.get('manager_email')
        
        user, created = User.objects.get_or_create(email=user_email)
        
        manager = None
        if manager_email:
            manager, _ = Manager.objects.get_or_create(user__email=manager_email)
        
        # Create employee
        Employee.objects.create(user=user, manager=manager)
        
        return redirect('add_employee') 
        
    return render(request, 'accounts/add_employee.html')

def update_employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    if request.method == 'POST':
        # Update employee information
        name = request.POST.get('name')
        status = request.POST.get('status')
        print(name)
        print(status)
        
        employee.user.name = name
        # Update user's status
        if status == "on":
            employee.confirmation_state = True
            employee.save()
        
        return redirect('view_employees')
    
    return render(request, 'accounts/update_employee.html', {'employee': employee})