from django.contrib import admin
from .models import AccessKey

# Register your models here.
class AccessKeyAdmin(admin.ModelAdmin):
    list_display = ['user', 'key', 'status', 'date_procured', 'expiry_date']


admin.site.register(AccessKey,AccessKeyAdmin)