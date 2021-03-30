# Generated by Django 3.1.5 on 2021-03-30 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_auto_20210327_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('in_progress', 'Заказ в обработке'), ('completed', 'Заказ выполнен'), ('new', 'Новый заказ'), ('in_ready', 'Заказ готов')], default='new', max_length=100, verbose_name='Статус заказа'),
        ),
    ]