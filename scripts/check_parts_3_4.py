import sys

sys.stdout.reconfigure(encoding="utf-8")

with open("Seg8_LiveCoding_Part3.txt", "r", encoding="utf-8") as f:
    text3 = f.read()

with open("Seg8_LiveCoding_Part4.txt", "r", encoding="utf-8") as f:
    text4 = f.read()

print("=== PART 3 KEY EXCERPTS ===")
for l in text3.splitlines()[::4]:
    print(l[:140])

print("\n=== PART 4 KEY EXCERPTS ===")
for l in text4.splitlines()[::4]:
    print(l[:140])
