from django.contrib import admin
from .models import User,Message

class UserAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'email', 'name', 'is_active', 'is_admin', 'is_staff', 'is_superuser', 'is_client')
    search_fields = ('phone_number', 'email', 'name')
    list_filter = ('is_active', 'is_admin', 'is_staff', 'is_superuser', 'is_client')
    list_editable = ('is_active', 'is_admin', 'is_staff', 'is_superuser', 'is_client')


    fieldsets = (
        (None, {
            'fields': ('phone_number', 'email', 'name', 'password')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_admin', 'is_staff', 'is_superuser', 'is_client')
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'email', 'name', 'password', 'is_active', 'is_admin', 'is_staff', 'is_superuser', 'is_client')
        }),
    )

admin.site.register(User, UserAdmin)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'created_at')
admin.site.register(Message,MessageAdmin)

