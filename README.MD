Custom CSV Reader & Writer in Python
This project implements a CSV (Comma Separated Values) Reader and Writer from scratch using Python.
It supports:
1.Comma separted fields
2.Double quoted fields
3.Escaped quotes(") inside fields
4.Newline character inside quoted fields
5.Newline charcter inside quoted fields
6.Streming read(no need to load full file into memory)

The goal is to understand the love-level mechanics of CSV parsing and writing and compare performance against Python's built-in csv module

Features
CustomCsvReader  => Class

Implemented as an iterator
Reads one row at a time
Handles:
        Commas
        Quotes
        Escaped quotes ("")
Newlines inside quotes
Works in streaming mode (memory efficient)

CustomCsvWriter => Class

Writes a list of lists as CSV file
Automatically quotes fields that contain:
                                        , (comma)
                                        " (double quote)
                                        \n (newline)
Escapes double quotes: " → ""

Project Structure

custom_csv_project/
│
├── custom_csv.py        # Reader & Writer classes
├── examples.py          # Small usage example
├── benchmark.py         # Performance test
├── test_data.csv        # Sample CSV test file
├── README.md            # Documentation
└── requirements.txt     # Dependencies
