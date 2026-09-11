import re, sys

sys.stdout.reconfigure(encoding="utf-8")

with open("subtitles.en.vtt", "r", encoding="utf-8") as f:
    content = f.read()

blocks = re.split(r"\n\s*\n", content)
time_pat = re.compile(r"(\d{2}:\d{2}:\d{2})\.\d{3}\s*-->\s*(\d{2}:\d{2}:\d{2})\.\d{3}")

clean_stream = []
last_text = ""
for b in blocks:
    lines = b.strip().splitlines()
    if not lines:
        continue
    tm = None
    text_lines = []
    for line in lines:
        m = time_pat.search(line)
        if m:
            tm = m.group(1)
        elif tm:
            clean = re.sub(r"<[^>]+>", "", line).strip()
            clean = clean.replace("&gt;", ">").replace("&lt;", "<").replace("&amp;", "&")
            if clean:
                text_lines.append(clean)
    if tm and text_lines:
        t = " ".join(text_lines)
        if t != last_text:
            clean_stream.append((tm, t))
            last_text = t

# Let's save condensed transcript with timestamps every ~30-60 seconds or per paragraph
condensed = []
curr_time = ""
curr_buf = []

for tm, t in clean_stream:
    # check time difference or seconds
    if not curr_time:
        curr_time = tm
    curr_buf.append(t)
    # If 60 seconds passed or buffer has enough words
    h, m, s = map(int, tm.split(":"))
    sec = h * 3600 + m * 60 + s
    
    cur_h, cur_m, cur_s = map(int, curr_time.split(":"))
    cur_sec = cur_h * 3600 + cur_m * 60 + cur_s
    
    if sec - cur_sec >= 30:
        full_text = " ".join(curr_buf)
        # deduplicate repeated phrases common in rolling captions
        # simple word dedup
        words = full_text.split()
        dedup_words = []
        for i, w in enumerate(words):
            if i > 0 and w == words[i-1]:
                continue
            dedup_words.append(w)
        condensed.append((curr_time, " ".join(dedup_words)))
        curr_time = tm
        curr_buf = []

if curr_buf:
    condensed.append((curr_time, " ".join(curr_buf)))

with open("condensed_transcript.txt", "w", encoding="utf-8") as f:
    for tm, txt in condensed:
        f.write(f"[{tm}] {txt}\n")

print(f"Condensed transcript written: {len(condensed)} blocks")
