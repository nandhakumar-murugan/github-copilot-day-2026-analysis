with open("Seg2_James_Montemagno.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Let us find sections and what James demonstrates
lines = text.splitlines()
print(f"Total lines in Seg2: {len(lines)}")
# Print every 5th line to see the progression
for i in range(0, len(lines), 7):
    print(lines[i][:110])
