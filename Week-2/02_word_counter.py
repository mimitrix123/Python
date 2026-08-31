"""Week 2 Assignment 2: Count words, lines, and characters in a text file."""


def count_file(path):
    with open(path, "r", encoding="utf-8") as file:
        text = file.read()
    lines = text.splitlines()
    words = text.split()
    return len(words), len(lines), len(text)


def main():
    path = input("Enter text file path: ").strip()
    try:
        words, lines, characters = count_file(path)
        print(f"Words: {words}")
        print(f"Lines: {lines}")
        print(f"Characters: {characters}")
    except FileNotFoundError:
        print("File not found. Check the path and try again.")
    except OSError as error:
        print(f"Unable to read file: {error}")


if __name__ == "__main__":
    main()
