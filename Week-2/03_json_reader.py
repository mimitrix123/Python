"""Week 2 Assignment 3: Read and display JSON data."""

import json


def load_json(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def main():
    path = input("Enter JSON file path: ").strip()
    try:
        data = load_json(path)
        print("\nFormatted JSON:")
        print(json.dumps(data, indent=4, ensure_ascii=False))
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError as error:
        print(f"Invalid JSON: {error}")
    except OSError as error:
        print(f"Unable to read file: {error}")


if __name__ == "__main__":
    main()
