# Generated by Django 4.1.3 on 2023-09-01 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0012_alter_ch08_post_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ch09_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('enabled', models.BooleanField(default=False)),
            ],
        ),
    ]
