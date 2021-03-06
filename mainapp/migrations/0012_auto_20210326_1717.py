# Generated by Django 3.1.5 on 2021-03-26 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_auto_20210326_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('in_ready', 'Заказ готов'), ('in_progress', 'Заказ в обработке'), ('completed', 'Заказ выполнен'), ('new', 'Новый заказ')], default='new', max_length=100, verbose_name='Статус заказа'),
        ),
    ]
