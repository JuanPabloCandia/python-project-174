import json
import yaml


# Здесь ничего кроме данных и их типа. Парсер парсит данные, а не файлы.
# Никакого намека на файловую систему, чтение файлов и расширения.
def parse(data, format_name):
    # Дефолтом может быть только выброс исключения
    # https://ru.hexlet.io/blog/posts/sovershennyy-kod-defolty-v-svitchah
    if format_name == 'json':
        return json.load(data)
    if format_name in {'yml', 'yaml'}:
        return yaml.safe_load(data)

    raise ValueError(f'Unknown format: {format_name}')
