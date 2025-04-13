#!/usr/bin/env python
import sys
import csv
import string

# Read CSV from standard input; no header exists.
reader = csv.reader(sys.stdin)

for row in reader:
    # Expecting exactly three columns: polarity, title, text.
    if len(row) < 3:
        continue
    polarity, title, text = row[0], row[1], row[2]
    # Combine title and text into one review.
    review = f"{title} {text}"
    # Preprocess: convert to lower case and remove punctuation.
    review = review.lower().translate(str.maketrans('', '', string.punctuation))
    # Convert polarity: "1" -> 0 (negative) and "2" -> 1 (positive)
    label = "0" if polarity.strip() == "1" else "1"
    # Emit the result: label and preprocessed review, tab-separated.
    print(f"{label}\t{review}")
