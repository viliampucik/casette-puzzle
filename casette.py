#!/usr/bin/env python
import sys

t = ""

for line in sys.stdin:
    s = [i for l in line.strip().split(",") if (i := int(l))]
    c = sum(1 for a, b in zip(s, s[1:]) if a > 0 and b < 0)
    t += f"{c / 4 - 1:.0f}"

for i in range(0, len(t), 8):
    print(chr(int(t[i+1:i+6], 3)), end="")