from django.contrib import admin
from .models import User, UserRole, Employee, Manager

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'is_active', 'is_staff', 'role')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'manager', 'confirmation_state')

class ManagerAdmin(admin.ModelAdmin):
    list_display = ('user',)


admin.site.register(User, CustomUserAdmin)
admin.site.register(UserRole)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Manager, ManagerAdmin)
