import re, sys

sys.stdout.reconfigure(encoding="utf-8")

def parse_vtt(vtt_file):
    with open(vtt_file, "r", encoding="utf-8") as f:
        content = f.read()

    blocks = re.split(r"\n\s*\n", content)
    cues = []
    time_pat = re.compile(r"(\d{2}:\d{2}:\d{2}\.\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2}\.\d{3})")
    
    last_text = ""
    for b in blocks:
        lines = b.strip().splitlines()
        if not lines:
            continue
        m = None
        text_lines = []
        for line in lines:
            tm = time_pat.search(line)
            if tm:
                m = tm
            elif m:
                clean = re.sub(r"<[^>]+>", "", line).strip()
                if clean:
                    text_lines.append(clean)
        if m and text_lines:
            text = " ".join(text_lines)
            if text != last_text:
                cues.append((m.group(1), m.group(2), text))
                last_text = text
    return cues

cues = parse_vtt("subtitles.en.vtt")
print(f"Total extracted cues: {len(cues)}")

keywords = [
    "Kyle", "James", "Montemagno", "Matt", "Pocock", "HydraFusion", "Aashna", "Julia", 
    "Meagan", "Tyler", "Leonhardt", "Patrick", "Nikoletich", "Wes", "Burke", "Pierce"
]

for kw in keywords:
    matches = [c for c in cues if kw.lower() in c[2].lower()]
    print(f"Keyword '{kw}': {len(matches)} matches")
    for m in matches[:2]:
        print(f"   [{m[0]}] {m[2]}")
