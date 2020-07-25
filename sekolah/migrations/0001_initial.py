from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xp', models.IntegerField(default=0)),
                ('hp', models.IntegerField(default=100)),
                ('level', models.CharField(default='Sailors', max_length=20)),
                ('nilai1', models.IntegerField(default=0)),
                ('nilai2', models.IntegerField(default=0)),
                ('nilai3', models.IntegerField(default=0)),
                ('nilai4', models.IntegerField(default=0)),
                ('kepemimpinan', models.IntegerField(default=0)),
                ('nasionalisme', models.IntegerField(default=0)),
                ('kebermanfaatan', models.IntegerField(default=0)),
                ('keilmuan', models.IntegerField(default=0)),
                ('adaptif', models.IntegerField(default=0)),
                ('solidaritas', models.IntegerField(default=0)),
                ('kolaboratif', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
