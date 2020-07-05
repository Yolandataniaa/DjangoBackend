# Generated by Django 3.0.8 on 2020-07-04 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.CharField(default='', max_length=200)),
                ('rank_int', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='StudentScores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kepemimpinan_int', models.IntegerField(default=0)),
                ('kecakapan_int', models.IntegerField(default=0)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls.Student')),
            ],
        ),
    ]
