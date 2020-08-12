# Generated by Django 3.0.7 on 2020-08-12 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sekolah', '0005_auto_20200812_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kirimpesan',
            name='penerima',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='spenerima', to='sekolah.Student'),
        ),
        migrations.AlterField(
            model_name='kirimpesan',
            name='pengirim',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pengirim', to='sekolah.Student'),
        ),
    ]
