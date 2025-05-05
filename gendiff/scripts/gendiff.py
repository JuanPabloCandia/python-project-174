import argparse
from gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file", help="First file to compare")
    parser.add_argument("second_file", help="Second file to compare")
    args = parser.parse_args()

    diff = generate_diff(args.first_file, args.second_file)
    print(diff)  


if __name__ == "__main__":
    main()
