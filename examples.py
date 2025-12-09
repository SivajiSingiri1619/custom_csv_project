import csv
from custom_csv import CustomCsvReader, CustomCsvWriter


def main():
    rows = [
        ["name", "comment"],
        ["Ram", 'He said "Hello"'],
        ["Sita", "Line1\nLine2"],
        ["Kumar", "Flat 101, MG Road"],
    ]

    out_file = "writer_test.csv"

    # Write using our CustomCsvWriter
    with open(out_file, "w", encoding="utf-8", newline="") as f:
        writer = CustomCsvWriter(f)
        writer.write_rows(rows)

    print(f"Wrote rows to {out_file} using CustomCsvWriter.\n")

    # Read back using Python's csv.reader
    print("Reading back with csv.reader:")
    with open(out_file, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


if __name__ == "__main__":
    main()
