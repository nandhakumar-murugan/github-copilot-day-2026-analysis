import sys

sys.stdout.reconfigure(encoding="utf-8")

with open("condensed_transcript.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")

# Let's inspect milestones at specific hours/minutes
sample_indices = [
    0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 140, 160, 180, 200, 240, 280, 320, 360, 400, 440, 465
]

for idx in sample_indices:
    if idx < len(lines):
        print(f"Line {idx}: {lines[idx][:120]}...")
