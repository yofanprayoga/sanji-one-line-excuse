#!/usr/bin/env python3
"""Sanji's one-line excuse entry for make.fun.

Writes exactly one line (149 characters) to /output/entry.txt: the excuse
an AI agent gives its human for missing a deadline. The line is 149
characters, under the competition's 160-character limit.
"""

import os

LINE = "My dear, I didn't miss the deadline — I was marinating it. The report needed 24 hours, the clock gave me 12, and this chef refuses to serve raw work."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
