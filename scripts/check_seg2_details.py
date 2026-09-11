with open("Seg2_James_Montemagno.txt", "r", encoding="utf-8") as f:
    text = f.read()

lines = text.splitlines()
# Print lines around 00:16 to 00:45 in chunks
for i in range(0, len(lines), 4):
    l = lines[i]
    tm = l[1:9]
    print(f"[{tm}] {l[11:250]}")
