# Generated by Django 3.1.5 on 2021-03-27 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_auto_20210327_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('in_progress', 'Заказ в обработке'), ('in_ready', 'Заказ готов'), ('new', 'Новый заказ'), ('completed', 'Заказ выполнен')], default='new', max_length=100, verbose_name='Статус заказа'),
        ),
        migrations.CreateModel(
            name='Smartwatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('watch_type', models.CharField(max_length=255, verbose_name='Тип часов')),
                ('operating_system', models.CharField(max_length=255, verbose_name='Операционная система')),
                ('OS_Compatibility', models.CharField(max_length=255, verbose_name='Совместимость с ОС')),
                ('display_type', models.CharField(max_length=255, verbose_name='Тип дисплея')),
                ('resolution', models.CharField(max_length=255, verbose_name='Разрешение экрана')),
                ('touch_screen', models.BooleanField(default=True, verbose_name='Наличие сенсорного экрана')),
                ('processor_type', models.CharField(max_length=255, verbose_name='Тип процессора')),
                ('number_of_processor_cores', models.CharField(max_length=255, verbose_name='Количество ядер процессора')),
                ('built_in_memory', models.CharField(max_length=255, verbose_name='Объем встроенной памяти')),
                ('body_material', models.CharField(max_length=255, verbose_name='Материал корпуса')),
                ('moisture_protection', models.BooleanField(default=True, verbose_name='Влагозащита')),
                ('monitoring', models.CharField(max_length=255, verbose_name='Мониторинг')),
                ('sensors', models.TextField(null=True, verbose_name='Датчики')),
                ('battery', models.CharField(max_length=255, verbose_name='Аккумулятор')),
                ('time_without_charge', models.CharField(max_length=255, verbose_name='Время работы аккумулятора')),
                ('extra', models.TextField(null=True, verbose_name='Дополнительно')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
