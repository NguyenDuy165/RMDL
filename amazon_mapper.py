#!/usr/bin/env python
import sys
import csv
import re

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "if",
    "in", "into", "is", "it", "no", "not", "of", "on", "or", "such", "that",
    "the", "their", "then", "there", "these", "they", "this", "to", "was",
    "will", "with"
}

def simple_stem(w):
    for s in ("ing", "ed", "s"):
        if w.endswith(s) and len(w) - len(s) >= 3:
            return w[:-len(s)]
    return w

def clean_tokens(text):
    text = re.sub(r'[^a-z\s]', ' ', text.lower())
    tokens = [simple_stem(w) for w in text.split() if w not in STOPWORDS]
    return " ".join(tokens)

reader = csv.reader(sys.stdin)
for row in reader:
    if len(row) < 3:
        continue
    raw_label, title, body = row[0], row[1], row[2]

    # map 1/2 → 0/1
    try:
        lbl = int(raw_label)
        if lbl == 1:
            label = 0
        elif lbl == 2:
            label = 1
        else:
            continue
    except ValueError:
        continue

    text = clean_tokens(title + " " + body)
    if text:
        print(f"{label}\t{text}")
