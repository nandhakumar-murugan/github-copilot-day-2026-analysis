import sys

sys.stdout.reconfigure(encoding="utf-8")

def scan_file(filename, step=5):
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
    print(f"=== {filename} (Total: {len(lines)} lines) ===")
    for i in range(0, len(lines), step):
        l = lines[i]
        tm = l[1:9]
        print(f"[{tm}] {l[11:180]}")

scan_file("Seg8_LiveCoding_Part1.txt", 6)
scan_file("Seg8_LiveCoding_Part2.txt", 8)
scan_file("Seg8_LiveCoding_Part3.txt", 7)
scan_file("Seg8_LiveCoding_Part4.txt", 7)
