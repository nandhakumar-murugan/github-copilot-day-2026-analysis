import sys

sys.stdout.reconfigure(encoding="utf-8")

with open("condensed_transcript.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

def get_text_range(start_time_str, end_time_str):
    res = []
    for line in lines:
        if line.startswith("["):
            tm = line[1:9]
            if start_time_str <= tm <= end_time_str:
                res.append(line)
    return "".join(res)

segments = [
    ("Seg1_Intro_Kyle", "00:08:00", "00:15:30"),
    ("Seg2_James_Montemagno", "00:15:30", "00:46:00"),
    ("Seg3_Matt_Pocock", "00:46:00", "01:07:00"),
    ("Seg4_HydraFusion", "01:07:00", "01:23:00"),
    ("Seg5_Meagan_Cojocar", "01:23:00", "01:37:45"),
    ("Seg6_Tyler_Leonhardt", "01:37:45", "01:48:00"),
    ("Seg7_Patrick_Nikoletich", "01:48:00", "02:08:00"),
    ("Seg8_LiveCoding_Part1", "02:08:00", "02:40:00"),
    ("Seg8_LiveCoding_Part2", "02:40:00", "03:15:00"),
    ("Seg8_LiveCoding_Part3", "03:15:00", "03:45:00"),
    ("Seg8_LiveCoding_Part4", "03:45:00", "04:11:40"),
]

for name, st, et in segments:
    txt = get_text_range(st, et)
    with open(f"{name}.txt", "w", encoding="utf-8") as out:
        out.write(txt)
    print(f"Wrote {name}.txt ({len(txt)} chars)")
