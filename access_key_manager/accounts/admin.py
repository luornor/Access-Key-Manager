from django.contrib import admin
from .models import CustomUser,EmailVerification
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    list_display = ('email', 'is_active', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)

@admin.register(EmailVerification)
class EmailVerificationModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'code', 'created_at','expiry_date')
    search_fields = ('user',)
    list_filter = ('created_at',)


admin.site.site_header = _('Access Key Administration')
admin.site.site_title = _('Access Key Admin Portal')
admin.site.index_title = _('Welcome to Access Key Admin Portal')