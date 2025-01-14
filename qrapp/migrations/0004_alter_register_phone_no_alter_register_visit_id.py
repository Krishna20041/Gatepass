# Generated by Django 5.0.7 on 2024-08-06 14:24

import qrapp.models
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrapp', '0003_alter_register_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='phone_no',
            field=qrapp.models.PhoneNumberField(max_length=10, null=True, region='IN'),
        ),
        migrations.AlterField(
            model_name='register',
            name='visit_id',
            field=models.CharField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
