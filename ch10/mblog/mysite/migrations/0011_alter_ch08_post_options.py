# Generated by Django 4.1.3 on 2023-08-30 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0010_alter_ch08_post_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ch08_post',
            options={'ordering': ('pub_time',)},
        ),
    ]