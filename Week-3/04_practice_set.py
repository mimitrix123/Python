"""Week 3 Practice Set: File handling and Python libraries."""

import json
from pathlib import Path


def count_lines(path):
    with open(path, "r", encoding="utf-8") as file:
        return sum(1 for _ in file)


def merge_files(first, second, output):
    with open(output, "w", encoding="utf-8") as target:
        for source_path in (first, second):
            with open(source_path, "r", encoding="utf-8") as source:
                target.write(source.read())
                target.write("\n")


def analyze_csv(path):
    import pandas as pd
    data = pd.read_csv(path)
    print("Shape:", data.shape)
    print("Columns:", list(data.columns))
    print("\nSummary:")
    print(data.describe(include="all"))
    return data


def plot_line_graph(x, y, output="line_graph.png"):
    import matplotlib.pyplot as plt
    plt.plot(x, y, marker="o")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Line Graph")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output)
    plt.close()


def json_demo(path="sample_data.json"):
    data = {"name": "Python Student", "skills": ["OOP", "Pandas", "Matplotlib"], "score": 95}
    Path(path).write_text(json.dumps(data, indent=4), encoding="utf-8")
    loaded = json.loads(Path(path).read_text(encoding="utf-8"))
    print("JSON data:", loaded)
    return loaded


if __name__ == "__main__":
    print("Run the individual functions above with your own input files.")
    json_demo()
