# Generated by Django 3.0.7 on 2020-07-20 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sekolah', '0002_angkatan'),
    ]

    operations = [
        migrations.AddField(
            model_name='angkatan',
            name='angkatan',
            field=models.CharField(default='', max_length=20),
        ),
    ]
