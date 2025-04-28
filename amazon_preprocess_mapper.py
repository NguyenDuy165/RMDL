#!/usr/bin/env python
import sys
import csv
import string

def preprocess_review(title, text):
    """
    Combine the title and text, convert to lower-case, and remove punctuation.
    """
    review = f"{title} {text}"
    review = review.lower().translate(str.maketrans('', '', string.punctuation))
    return review

reader = csv.reader(sys.stdin)
line_id = 0
for row in reader:
    # Each row is: polarity, title, text
    if len(row) < 3:
        continue
    polarity, title, text = row[0], row[1], row[2]
    review = preprocess_review(title, text)
    # Output format: review_id <tab> review_text
    print(f"{line_id}\t{review}")
    line_id += 1
