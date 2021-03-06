# Generated by Django 3.0.7 on 2020-08-11 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sekolah', '0002_auto_20200725_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='jumlahpotion',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='KirimPesan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('potion', models.IntegerField(default=0)),
                ('pesan', models.CharField(default='Ketik pesan disini', max_length=40)),
                ('pengirim', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sekolah.Student')),
            ],
        ),
    ]
