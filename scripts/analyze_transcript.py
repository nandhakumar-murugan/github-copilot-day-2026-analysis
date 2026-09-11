import re, sys

sys.stdout.reconfigure(encoding="utf-8")

def parse_vtt(vtt_file):
    with open(vtt_file, "r", encoding="utf-8") as f:
        text = f.read()

    # Pattern for vtt cues
    cues = re.findall(r"(\d{2}:\d{2}:\d{2}\.\d{3}) --> (\d{2}:\d{2}:\d{2}\.\d{3})\n([\s\S]*?)(?=\n\d{2}:\d{2}:\d{2}\.\d{3} -->|\Z)", text)
    
    clean_cues = []
    seen = set()
    for start, end, body in cues:
        # clean html tags
        body = re.sub(r"<[^>]+>", "", body).strip()
        body = " ".join(body.split())
        if body and body not in seen:
            seen.add(body)
            clean_cues.append((start, end, body))
    return clean_cues

cues = parse_vtt("subtitles.en.vtt")
print(f"Total unique cues: {len(cues)}")

# Let's search for mentions of speaker names or key transitions
keywords = [
    "Kyle", "James", "Montemagno", "Matt", "Pocock", "HydraFusion", "Aashna", "Julia", 
    "Meagan", "Tyler", "Leonhardt", "Patrick", "Nikoletich", "Wes Bos", "Burke", "Pierce"
]

for kw in keywords:
    matches = [c for c in cues if kw.lower() in c[2].lower()]
    print(f"Keyword '{kw}': {len(matches)} matches")
    for m in matches[:3]:
        print(f"   [{m[0]}] {m[2]}")
