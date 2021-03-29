from django import template
from django.utils.safestring import mark_safe

from mainapp.models import Smartphone

register = template.Library()


TABLE_HEAD = """
                <table class="table">
                    <tbody>
             """

TABLE_TAIL = """
                 </tbody>
                </table>
             """

TABLE_CONTENT = """
                    <tr>
                        <td>{name}</td>
                        <td>{value}</td>
                    </tr>
                """

PRODUCT_SPEC = {
    'notebook': {
        'Диагональ': 'diagonal',
        'Тип дисплея': 'display_type',
        'Частота процессора': 'processor_freq',
        'Оперативная память': 'ram',
        'Видеокарта': 'video',
        'Время работы аккумулятора': 'time_without_charge'
    },
    'smartphone': {
        'Диагональ': 'diagonal',
        'Тип дисплея': 'display_type',
        'Разрешение экрана': 'resolution',
        'Оперативная память': 'ram',
        'Наличие слота для SD карты': 'sd',
        'Максимальный объем SD карты': 'sd_volume_max',
        'Заряд аккумулятора': 'accum_volume',
        'Камера(МП)': 'main_cam_mp',
        'Фронтальная камера(МП)': 'frontal_cam_mp',
    },
    'television': {
        'Диагональ': 'diagonal',
        'Тип дисплея': 'display_type',
        'Разрешение экрана': 'resolution',
        'Частота обновления экрана': 'screen_refresh_rate',
        'Операционная система': 'operating_system',
        'Мощность звука': 'sound_power',
        'Наличие слота для SD карты': 'sd',
        'Дополнительно': 'extra',
    },
    'smartwatch': {
        'Тип': 'watch_type',
        'Операционная система': 'operating_system',
        'Совместимость с ОС': 'OS_Compatibility',
        'Тип дисплея': 'display_type',
        'Разрешение экрана': 'resolution',
        'Наличие сенсорного экрана ': 'touch_screen',
        'Тип процессора': 'processor_type',
        'Количество ядер процессора': 'number_of_processor_cores',
        'Объем встроенной памяти': 'built_in_memory',
        'Материал корпуса': 'body_material',
        'Влагозащита': 'moisture_protection',
        'Мониторинг': 'monitoring',
        'Датчики': 'sensors',
        'Аккумулятор ': 'battery',
        'Время работы аккумулятора': 'time_without_charge',
        'Дополнительно': 'extra',
    }
}


def get_product_spec(product, model_name):
    table_content = ''
    for name, value in PRODUCT_SPEC[model_name].items():
        table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
    return table_content


@register.filter
def product_spec(product):
    model_name = product.__class__._meta.model_name
    if isinstance(product, Smartphone):
        if not product.sd:
            PRODUCT_SPEC['smartphone'].pop('Максимальный объем SD карты')
        else:
            PRODUCT_SPEC['smartphone']['Максимальный объем SD карты'] = 'sd_volume_max'
    return mark_safe(TABLE_HEAD + get_product_spec(product, model_name) + TABLE_TAIL)
