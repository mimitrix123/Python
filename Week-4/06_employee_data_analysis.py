"""Week 4 Capstone Project: Employee Data Analysis using Pandas."""

import pandas as pd


FILE = "employees.csv"
OUTPUT = "high_salary_employees.csv"


def analyze():
    data = pd.read_csv(FILE)

    print("Employee Dataset")
    print(data)

    print("\nAverage Salary:", data["Salary"].mean())

    print("\nEmployees per Department:")
    print(data["Department"].value_counts())

    threshold = float(input("\nEnter salary threshold: "))
    filtered = data[data["Salary"] > threshold]

    print("\nEmployees above threshold:")
    print(filtered)

    filtered.to_csv(OUTPUT, index=False)
    print(f"\nFiltered data exported to {OUTPUT}")


if __name__ == "__main__":
    analyze()
