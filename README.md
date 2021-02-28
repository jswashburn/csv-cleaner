# csv-cleaner - Clean up your csv data before importing it as a flat file into SQL server.
## Usage (You will need a python interpreter)
1. Place the script in the directory containing your csv files.
2. Run the script.
3. Output will display your cleaned csv lines - review and save file. Script moves on to the next file.
4. Cleaned csv file will be saved as cleanedfile.clean.csv

### What it "cleans"
* Empty strings, all whitespace strings, strings containing the word "NULL" are all converted to an empty string '' - which can actually be interpreted by SQL as NULL
* Turns strings containing numeric values into their actual numeric type. Ints are written as ints and decimal/float values are written with their decimal point
