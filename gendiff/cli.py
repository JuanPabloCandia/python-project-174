import argparse
from gendiff.scripts.gendiff import generate_diff  # Asegúrate que esta función exista y esté bien importada

def parse_args():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        "-f", "--format", default="stylish", help="set format of output"
    )
    return parser.parse_args()

def main():
    args = parse_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)
