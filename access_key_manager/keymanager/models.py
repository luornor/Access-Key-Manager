# Create your models here.
from django.db import models
from accounts.models import CustomUser    
    
class AccessKey(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    key = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('expired', 'Expired'), ('revoked', 'Revoked')])
    date_procured = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField()

    def __str__(self):
        return f"{self.user.email} - {self.key}"