import csv
import random
import string
import time
from typing import List

from custom_csv import CustomCsvReader, CustomCsvWriter


def random_field() -> str:
    """Generate a random field with sometimes comma/quote/newline."""
    base = "".join(random.choices(string.ascii_letters + " ", k=random.randint(5, 15)))
    choice = random.randint(1, 5)

    if choice == 1:
        return base + ", extra"          # comma
    elif choice == 2:
        return base + ' "quote"'         # quote
    elif choice == 3:
        return base + "\nnext line"      # newline
    else:
        return base                      # simple


def generate_rows(n_rows: int, n_cols: int) -> List[List[str]]:
    return [[random_field() for _ in range(n_cols)] for _ in range(n_rows)]


def benchmark_writer(rows: List[List[str]]) -> None:
    print("=== Write Benchmark ===")
    # Standard csv.writer
    start = time.perf_counter()
    with open("std_output.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    t_std = time.perf_counter() - start

    # CustomCsvWriter
    start = time.perf_counter()
    with open("custom_output.csv", "w", encoding="utf-8", newline="") as f:
        writer = CustomCsvWriter(f)
        writer.write_rows(rows)
    t_custom = time.perf_counter() - start

    print(f"csv.writer       : {t_std:.4f} s")
    print(f"CustomCsvWriter  : {t_custom:.4f} s\n")


def benchmark_reader() -> None:
    print("=== Read Benchmark ===")
    # Standard csv.reader
    start = time.perf_counter()
    with open("custom_output.csv", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        count_std = sum(1 for _ in reader)
    t_std = time.perf_counter() - start

    # CustomCsvReader
    start = time.perf_counter()
    with open("custom_output.csv", encoding="utf-8") as f:
        reader = CustomCsvReader(f)
        count_custom = sum(1 for _ in reader)
    t_custom = time.perf_counter() - start

    print(f"csv.reader       : {t_std:.4f} s (rows: {count_std})")
    print(f"CustomCsvReader  : {t_custom:.4f} s (rows: {count_custom})\n")


def main():
    random.seed(42)

    n_rows = 10000
    n_cols = 5

    print(f"Generating {n_rows} rows x {n_cols} columns...")
    rows = generate_rows(n_rows, n_cols)
    print("Done.\n")

    benchmark_writer(rows)
    benchmark_reader()


if __name__ == "__main__":
    main()
