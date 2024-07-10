# Generated by Django 5.0.6 on 2024-07-10 15:28

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_emailverification_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverification',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 11, 15, 28, 27, 957425, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='emailverification',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email_verification', to=settings.AUTH_USER_MODEL),
        ),
    ]