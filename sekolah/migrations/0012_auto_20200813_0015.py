# Generated by Django 3.0.7 on 2020-08-12 17:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sekolah', '0011_auto_20200813_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kirimpesan',
            name='penerima',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='penerima', to=settings.AUTH_USER_MODEL),
        ),
    ]
