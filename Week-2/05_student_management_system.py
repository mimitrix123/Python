"""Week 2 Mini Project: Student Management System.
CRUD operations backed by a CSV file for permanent storage.
"""

import csv
from pathlib import Path

FILE = Path(__file__).with_name("students.csv")
FIELDS = ["roll_number", "name", "marks"]


def load_students():
    if not FILE.exists():
        return []
    try:
        with FILE.open("r", newline="", encoding="utf-8") as file:
            return list(csv.DictReader(file))
    except (OSError, csv.Error) as error:
        print(f"Could not read student data: {error}")
        return []


def save_students(students):
    try:
        with FILE.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(students)
        return True
    except OSError as error:
        print(f"Could not save student data: {error}")
        return False


def add_student(students):
    roll = input("Roll number: ").strip()
    if any(s["roll_number"] == roll for s in students):
        print("A student with this roll number already exists.")
        return
    name = input("Name: ").strip()
    try:
        marks = float(input("Marks (0-100): "))
        if not 0 <= marks <= 100:
            raise ValueError
    except ValueError:
        print("Marks must be a number between 0 and 100.")
        return
    students.append({"roll_number": roll, "name": name, "marks": f"{marks:g}"})
    if save_students(students):
        print("Student added and saved.")


def search_student(students):
    key = input("Enter roll number or name: ").strip().lower()
    matches = [s for s in students if s["roll_number"].lower() == key or s["name"].lower() == key]
    if not matches:
        print("Student not found.")
        return
    for s in matches:
        print(f"Roll: {s['roll_number']} | Name: {s['name']} | Marks: {s['marks']}")


def delete_student(students):
    roll = input("Enter roll number to delete: ").strip()
    remaining = [s for s in students if s["roll_number"] != roll]
    if len(remaining) == len(students):
        print("Student not found.")
        return
    if save_students(remaining):
        students[:] = remaining
        print("Student deleted and changes saved.")


def show_all(students):
    if not students:
        print("No students found.")
        return
    print("\nRoll Number | Name | Marks")
    print("-" * 30)
    for s in students:
        print(f"{s['roll_number']} | {s['name']} | {s['marks']}")


def main():
    students = load_students()
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student\n2. Search Student\n3. Delete Student\n4. Show All\n5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_student(students)
        elif choice == "2":
            search_student(students)
        elif choice == "3":
            delete_student(students)
        elif choice == "4":
            show_all(students)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
