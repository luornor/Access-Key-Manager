# Generated by Django 5.0.6 on 2024-06-30 16:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_emailverification_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverification',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 1, 16, 31, 10, 475509, tzinfo=datetime.timezone.utc)),
        ),
    ]
