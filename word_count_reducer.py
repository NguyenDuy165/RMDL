#!/usr/bin/env python
import sys
for line in sys.stdin:
    print(f"Processing: {line.strip()}", file=sys.stderr)  # Debugging output
    # Your reducer logic here
