# Generated by Django 4.1.3 on 2023-08-28 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_maker_alter_post_options_pphoto_pmodel_ch07_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ch07_product',
            name='nickname',
            field=models.CharField(default='超值二手機', max_length=15, verbose_name='摘要'),
        ),
        migrations.AlterField(
            model_name='ch07_product',
            name='pmodel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.pmodel', verbose_name='型號'),
        ),
        migrations.AlterField(
            model_name='ch07_product',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='價格'),
        ),
        migrations.AlterField(
            model_name='ch07_product',
            name='year',
            field=models.PositiveIntegerField(default=2016, verbose_name='出廠年份'),
        ),
        migrations.AlterField(
            model_name='pphoto',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.ch07_product'),
        ),
    ]
