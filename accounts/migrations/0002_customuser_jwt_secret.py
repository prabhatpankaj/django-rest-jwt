# Generated by Django 2.1.4 on 2018-12-24 01:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='jwt_secret',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
