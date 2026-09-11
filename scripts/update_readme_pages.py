with open("README.md", "r", encoding="utf-8") as f:
    text = f.read()

# Add GitHub Pages badge and live link to README.md
live_url = "https://nandhakumar-murugan.github.io/github-copilot-day-2026-analysis/"
badge_insert = f"""[![GitHub Pages](https://img.shields.io/badge/Live%20Dashboard-GitHub%20Pages-blue?style=flat&logo=github)]({live_url})
"""

# Place right after the other badges
new_text = text.replace("[![Model Orchestration](https://img.shields.io/badge/Preview-Project%20HydraFusion-purple)]()", 
                        f"[![Model Orchestration](https://img.shields.io/badge/Preview-Project%20HydraFusion-purple)]()\n{badge_insert}")

# Also add in the Key Documents section
doc_insert = f"""### 🌐 Live Interactive Web App
👉 **[Open Interactive Video Dashboard & Notes]({live_url})**
* **Synced YouTube Video Player**: Click any agenda chapter to jump the video directly to that moment.
* **Keyframe Visual Explorer**: Browse captured slides, lower-third banners, and 3D demos.
* **Instant Keyword Filter**: Search topics, models, HydraFusion, Agent Skills, and speakers in real time.
* **Interactive Speaker Directory**: Click directly into speaker GitHub and LinkedIn accounts.

"""

new_text = new_text.replace("### 📄 Key Documents", f"{doc_insert}\n### 📄 Key Documents")

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_text)

print("README.md updated with live GitHub Pages URL.")
