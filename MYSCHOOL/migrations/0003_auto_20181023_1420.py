# Generated by Django 2.1.2 on 2018-10-23 07:20

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MYSCHOOL', '0002_auto_20181023_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='tblstudent',
            name='create_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tblstudent',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 23, 7, 20, 56, 740964, tzinfo=utc)),
        ),
    ]