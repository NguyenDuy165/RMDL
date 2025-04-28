#!/usr/bin/env python
import sys

for line in sys.stdin:
    # mapper already emitted: label \t text
    line = line.strip()
    if not line:
        continue
    # you could do further aggregation here if needed
    print(line)