import sys, re

sys.stdout.reconfigure(encoding="utf-8")

with open("Seg8_LiveCoding_Part1.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Let us find what they started building around 02:08 - 02:25
print("=== Beginning of Live Coding Project ===")
for l in text.splitlines()[:25]:
    print(l[:140])
