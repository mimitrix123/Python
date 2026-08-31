"""Week 2 Practice Set: Data structures and loops."""


def list_crud():
    values = [10, 20, 30]
    print("Initial list:", values)
    values.append(40)          # Create
    values[1] = 25             # Update
    values.remove(30)          # Delete
    print("After CRUD:", values)  # Read


def word_frequency():
    sentence = input("Enter a sentence: ").lower()
    words = sentence.split()
    frequency = {}
    for word in words:
        word = word.strip(".,!?;:")
        if word:
            frequency[word] = frequency.get(word, 0) + 1
    print("Word frequency:", frequency)


def pattern():
    rows = int(input("Enter number of rows: "))
    for i in range(1, rows + 1):
        for _ in range(i):
            print("*", end=" ")
        print()


def min_max():
    numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
    if not numbers:
        print("No numbers entered.")
        return
    print("Smallest:", min(numbers))
    print("Largest:", max(numbers))


def sort_lambda():
    values = ["python", "C++", "java", "JavaScript", "go"]
    print("Alphabetical (case-insensitive):", sorted(values, key=lambda x: x.lower()))


def main():
    list_crud()
    word_frequency()
    pattern()
    min_max()
    sort_lambda()


if __name__ == "__main__":
    main()
