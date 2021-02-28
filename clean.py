import os
import csv

def numeric(value):
    """Check if value can be converted to float or integer, if not just return value"""
    if "." in str(value):
        try:
            float(value)
        except ValueError:
            return value.strip()
        else:
            return float(value)
    else:
        try:
            int(value)
        except ValueError:
            return value.strip()
        else:
            return int(value)

def clean_value(value):
    """Check if value is null, else try and convert to number, then return result"""
    if value == "" or value.isspace() or value == "NULL":
        return ""

    return numeric(value)

def clean_line(line):
    """Clean every value in line and return new cleaned line (list)"""
    return [clean_value(v) for v in line]

def clean(file):
    """Open a file and clean every line returned by csv.reader, returning a new list of cleaned lines"""
    with open(file, "r") as f:
        return [clean_line(l) for l in csv.reader(f)]

def prompt_continue():
    while True:
        response = input("Save? [y/n] ").lower().strip()
        if response == "y":
            return True
        elif response == "n":
            return False

def write_file(file, lines):
    """Write cleaned lines to new file with .clean.csv extension"""
    if prompt_continue():
        with open(f"{os.path.splitext(file)[0]}.clean.csv", "w", newline="") as f:
            writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
            writer.writerows(lines)


for file in os.listdir("."):
    if os.path.isfile(file):
        if not file.endswith(".clean.csv") and file.endswith(".csv"):
            input(f"Enter to see {os.path.basename(file)} cleaned...")

            cleaned_lines = clean(file)
            for line in cleaned_lines:
                print(line)
            print("\n")

            write_file(file, cleaned_lines)