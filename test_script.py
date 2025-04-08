#!/usr/bin/env python
import sys

# Read input from stdin
for line in sys.stdin:
    # Strip leading/trailing whitespaces
    line = line.strip()
    
    # Split the line into words
    words = line.split()
    
    # Emit each word with a count of 1
    for word in words:
        print(f"{word}\t1")
