from gendiff.formatters.json import render_json
from gendiff.formatters.plain import render_plain
from gendiff.formatters.stylish import render_stylish


def format(format_name, tree):
    if format_name == 'json':
        return render_json(tree)
    if format_name == 'plain':
        return render_plain(tree)
    if format_name == 'stylish':
        return render_stylish(tree)

    raise ValueError(f'Unknown format: {format_name}')
