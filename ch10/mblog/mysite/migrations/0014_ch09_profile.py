# Generated by Django 4.1.3 on 2023-09-04 04:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mysite', '0013_ch09_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ch09_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.PositiveIntegerField(default=160)),
                ('male', models.BooleanField(default=True)),
                ('website', models.URLField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]