from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from custom_users.models import CustomUser, Company, Employee

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'User Viewable Details',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'role',
                ),
            },
        ),
    )




admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Company)
admin.site.register(Employee)

