"""Week 1 - Assignment 2: Student Grade Calculator."""


def calculate_average(marks):
    return sum(marks) / len(marks)


def calculate_grade(average):
    if average >= 90:
        return "A+"
    if average >= 80:
        return "A"
    if average >= 70:
        return "B"
    if average >= 60:
        return "C"
    if average >= 50:
        return "D"
    return "F"


def main():
    try:
        count = int(input("Enter number of subjects: "))
        if count <= 0:
            print("Number of subjects must be positive.")
            return

        marks = []
        for i in range(1, count + 1):
            mark = float(input(f"Enter marks for subject {i} (0-100): "))
            if not 0 <= mark <= 100:
                print("Marks must be between 0 and 100.")
                return
            marks.append(mark)

        average = calculate_average(marks)
        grade = calculate_grade(average)
        print(f"Average: {average:.2f}")
        print(f"Grade: {grade}")
    except ValueError:
        print("Please enter valid numeric values.")


if __name__ == "__main__":
    main()
