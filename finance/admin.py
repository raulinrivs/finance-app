from django.contrib import admin

from finance.models import Company, Employee
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Expense

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email', 'company')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Expense)
# Register your models here.
