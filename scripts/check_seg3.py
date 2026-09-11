with open("Seg3_Matt_Pocock.txt", "r", encoding="utf-8") as f:
    text = f.read()

lines = text.splitlines()
print(f"Total lines in Seg3: {len(lines)}")
for i in range(0, len(lines), 4):
    l = lines[i]
    tm = l[1:9]
    print(f"[{tm}] {l[11:220]}")
