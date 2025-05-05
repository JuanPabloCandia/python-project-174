def build_indent(depth):
    return ' ' * (depth * 4 - 2)


# Важно правильное выделение этой функции
# https://ru.hexlet.io/challenges/python_trees_stringify_exercise
def to_str(data, depth):
    if isinstance(data, bool):
        return 'true' if data else 'false'

    if data is None:
        return 'null'

    if isinstance(data, dict):
        parts = []
        for key in data:
            indent = build_indent(depth + 1)
            formatted_value = to_str(data[key], depth + 1)
            parts.append(f"{indent}  {key}: {formatted_value}")
        output = '\n'.join(parts)
        return f"{{\n{output}\n{build_indent(depth)}  }}"

    return data


# Обход дерева всегда в глубину на один уровень (+1)
# Не может быть -1, +4, или погружение на 4 пробела '    '

def iter_(node, depth=0):
    children = node.get('children')
    indent = build_indent(depth)
    formatted_value = to_str(node.get('value'), depth)
    formatted_value1 = to_str(node.get('value1'), depth)
    formatted_value2 = to_str(node.get('value2'), depth)

    # Логика целиком и полностью определяется типом.
    # На верхнем уровне проверка по типу, все остальные ифы внутри.
    # Принципиально, что не должно быть особых нод,
    # обрабатываемых не так, как все остальные.
    if node['type'] == 'root':
        lines = map(lambda child: iter_(child, depth + 1), children)
        result = '\n'.join(lines)
        return f'{{\n{result}\n}}'

    if node['type'] == 'nested':
        lines = map(lambda child: iter_(child, depth + 1), children)
        result = '\n'.join(lines)
        return f"{indent}  {node['key']}: {{\n{result}\n{indent}  }}"

    if node['type'] == 'added':
        return f"{indent}+ {node['key']}: {formatted_value}"

    if node['type'] == 'deleted':
        return f"{indent}- {node['key']}: {formatted_value}"

    if node['type'] == 'changed':
        lines = [
            f"{indent}- {node['key']}: {formatted_value1}",
            f"{indent}+ {node['key']}: {formatted_value2}"
        ]
        return '\n'.join(lines)

    if node['type'] == 'unchanged':
        return f"{indent}  {node['key']}: {formatted_value}"

    raise ValueError(f"Unknown type: {node['type']}")


def render_stylish(tree):
    return iter_(tree)
