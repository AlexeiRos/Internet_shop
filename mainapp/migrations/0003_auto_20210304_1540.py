# Generated by Django 3.1.6 on 2021-03-04 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_notebook_smartphone'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='for_anonymous_user',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cart',
            name='in_order',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cart',
            name='total_products',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='sd_volume_max',
            field=models.CharField(max_length=255, verbose_name='Максимальный объем памяти'),
        ),
    ]
