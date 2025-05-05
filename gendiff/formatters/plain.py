def to_str(value):
    if isinstance(value, bool):
        return "true" if value else "false"

    if value is None:
        return "null"

    if isinstance(value, str):
        return f"'{value}'"

    if isinstance(value, dict) or isinstance(value, list):
        return "[complex value]"

    return value


def iter_(node, ancestry=""):
    children = node.get("children")
    property_name = f"{ancestry}{node.get('key')}"

    if node["type"] == "root":
        parts = map(lambda child: iter_(child), children)
        lines = sum(parts, [])
        return "\n".join(lines)

    if node["type"] == "nested":
        parts = map(
            lambda child: iter_(child, f"{property_name}."),
            children,
        )
        return sum(parts, [])

    if node["type"] == "added":
        return [
            f"Property '{property_name}' was added with value: {to_str(node['value'])}"  # noqa: E501
        ]

    if node["type"] == "deleted":
        return [f"Property '{property_name}' was removed"]

    if node["type"] == "changed":
        return [
            f"Property '{property_name}' was updated. "
            f"From {to_str(node['value1'])} to {to_str(node['value2'])}"
        ]

    if node["type"] == "unchanged":
        return []

    raise ValueError(f"Unknown type: {node['type']}")


# Функция должна выставлять только тот интерфейс, который ожидает клиент
# https://www.youtube.com/watch?v=2sgMdgOSCxg
def render_plain(diff):
    return iter_(diff)
