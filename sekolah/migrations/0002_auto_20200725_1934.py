# Generated by Django 3.0.7 on 2020-07-25 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sekolah', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Angkatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('angkatan', models.CharField(default='', max_length=20)),
                ('xp', models.IntegerField(default=100)),
                ('level', models.CharField(default='Sailors', max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='nilai1',
        ),
        migrations.RemoveField(
            model_name='student',
            name='nilai2',
        ),
        migrations.RemoveField(
            model_name='student',
            name='nilai3',
        ),
        migrations.RemoveField(
            model_name='student',
            name='nilai4',
        ),
        migrations.AddField(
            model_name='student',
            name='alive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='student',
            name='hp_pot',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='xpminggu',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.CharField(default='', max_length=40)),
                ('week', models.IntegerField(default=0)),
                ('score', models.IntegerField(default=0)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sekolah.Student')),
            ],
        ),
    ]
