from django.contrib import admin
from .models import User, UserRole, Employee, Manager

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'is_active', 'is_staff', 'role')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'manager', 'confirmation_state')

class ManagerAdmin(admin.ModelAdmin):
    list_display = ('user',)

# Register the User and UserRole models with the custom admin class
admin.site.register(User, CustomUserAdmin)
admin.site.register(UserRole)
# Register the Employee and Manager models with the custom admin classes
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Manager, ManagerAdmin)
