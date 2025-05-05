import os

import gendiff.tree
from gendiff.formatters import format
from gendiff.parser import parse


def get_format(file_path):
    _, extension = os.path.splitext(file_path)
    return extension.lower()[1:]


def get_data(file_path):
    return parse(open(file_path), get_format(file_path))


def generate_diff(file_path1, file_path2, format_name='stylish'):
    # Основной процесс
    # => Читаем файлы и формат
    # => Парсим данные
    # => Строим внутреннее дерево => Возвращаем форматированные данные
    #    Больше здесь ничего быть не может.
    # Сама обработка строится в виде пайплайна.
    # https://ru.hexlet.io/blog/posts/sovershennyy-kod-nishodyaschee-i-voshodyaschee-proektirovanie

    data1 = get_data(file_path1)
    data2 = get_data(file_path2)

    diff = gendiff.tree.build(data1, data2)

    return format(format_name, diff)
