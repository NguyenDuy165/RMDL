#!/usr/bin/env python
import sys

current_word = None
current_count = 0

# Read input from stdin
for line in sys.stdin:
    # Strip leading/trailing whitespaces
    line = line.strip()
    
    # Split the line into word and count
    word, count = line.split("\t")
    
    try:
        count = int(count)
    except ValueError:
        continue  # Ignore lines with invalid counts
    
    # Accumulate the count for the current word
    if current_word == word:
        current_count += count
    else:
        # Print the current word and its count
        if current_word:
            print(f"{current_word}\t{current_count}")
        
        # Set the new word and reset the count
        current_word = word
        current_count = count

# Print the last word and its count
if current_word == word:
    print(f"{current_word}\t{current_count}")
