# Дерево не знает ничего про вывод и не может готовить данные для него.
# Дерево описывает собой разницу между данными (не визуально).

# Правильный способ строить дерево – находить объединение ключей
# и выполнять один проход
# https://www.youtube.com/watch?v=vkUTX1hruF8
# У каждой ноды должен быть тип.
# Всего их 5 (по количеству разных вариантов поведения).
def build_diff(data1, data2):
    result = []

    keys = data1.keys() | data2.keys()

    for key in sorted(keys):
        if key not in data2:
            # тип ноды может иметь любое другое имя
            # ключ со значением может называться value1/value2
            result.append({
                'key': key,
                'type': 'deleted',
                'value': data1[key]
            })
        elif key not in data1:
            result.append({
                'key': key,
                'type': 'added',
                'value': data2[key]
            })
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            result.append({
                'key': key,
                'type': 'nested',
                'children': build_diff(data1[key], data2[key])
            })
        elif data1[key] != data2[key]:
            result.append({
                'key': key,
                'type': 'changed',
                'value1': data1[key],
                'value2': data2[key]
            })
        else:
            result.append({
                'key': key,
                'type': 'unchanged',
                'value': data1[key],
            })

    return result


def build(data1, data2):
    return {
        'type': 'root',
        'children': build_diff(data1, data2)
    }
