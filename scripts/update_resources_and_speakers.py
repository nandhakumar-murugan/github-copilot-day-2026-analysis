# Add speaker directory and resources to GitHub_Copilot_Day_Full_Notes.md and README.md

import re

# Read current notes
with open("GitHub_Copilot_Day_Full_Notes.md", "r", encoding="utf-8") as f:
    notes = f.read()

# Generate the Speakers Table
speakers_section = """
---

## 👥 Featured Speakers & Profiles

| Speaker | Role / Affiliation | GitHub | LinkedIn |
| :--- | :--- | :--- | :--- |
| **Kyle Daigle** | Chief Operating Officer (COO), GitHub | [@kdaigle](https://github.com/kdaigle) | [in/kyledaigle](https://www.linkedin.com/in/kyledaigle) |
| **Burke Holland** | Principal Developer Advocate, Microsoft / GitHub | [@burkeholland](https://github.com/burkeholland) | [in/burkeholland](https://www.linkedin.com/in/burkeholland) |
| **Pierce Boggan** | Product Lead, VS Code & GitHub Copilot, Microsoft | [@pierceboggan](https://github.com/pierceboggan) | [in/pierceboggan](https://www.linkedin.com/in/pierceboggan) |
| **James Montemagno** | Principal Lead Program Manager, Microsoft DevRel | [@jamesmontemagno](https://github.com/jamesmontemagno) | [in/jamesmontemagno](https://www.linkedin.com/in/jamesmontemagno) |
| **Matt Pocock** | TypeScript Educator, Creator of Total TypeScript & Skills | [@mattpocock](https://github.com/mattpocock) | [in/mattpocock](https://www.linkedin.com/in/mattpocock) |
| **Julia Kasper** | Senior Product Manager, VS Code & GitHub Copilot | [@juliakaspar](https://github.com/juliakaspar) | [in/juliakasper](https://www.linkedin.com/in/juliakasper) |
| **Aashna Garg** | Principal Applied Scientist (Code AI & HyDRA), Microsoft | [@aashnagarg](https://github.com/aashnagarg) | [in/aashnagarg](https://www.linkedin.com/in/aashnagarg) |
| **Meagan Cojocar** | Product Manager, GitHub Copilot (Integrations & Mobile) | [@meagancojocar](https://github.com/meagancojocar) | [in/meagancojocar](https://www.linkedin.com/in/meagancojocar) |
| **Tyler Leonhardt** | Senior Software Engineer, VS Code & Copilot Team | [@TylerLeonhardt](https://github.com/TylerLeonhardt) | [in/tylerleonhardt](https://www.linkedin.com/in/tylerleonhardt) |
| **Patrick Nikoletich** | Principal Software Engineer, Copilot Agent Runtime & SDK | [@patniko](https://github.com/patniko) | [in/patricknikoletich](https://www.linkedin.com/in/patricknikoletich) |
| **Wes Bos** | Full-Stack Developer, Educator & Syntax Podcast Host | [@wesbos](https://github.com/wesbos) | [in/wesbos](https://www.linkedin.com/in/wesbos) |
"""

# Generate Resources Section
resources_section = """
---

## 🔗 Essential Resources & Technical Links

### 🛠️ Products, Downloads & Documentation
* **GitHub Copilot App:** [https://gh.io/app](https://gh.io/app) — Native desktop application for orchestrating asynchronous multi-agent workflows across repositories.
* **GitHub Copilot CLI:** [GitHub CLI Docs](https://docs.github.com/en/copilot/github-copilot-in-the-cli) — Terminal-native agent workflows powered by HydraFusion.
* **Copilot Dev Days Workshop:** [https://copilot-dev-days.github.io/](https://copilot-dev-days.github.io/) — Interactive labs and hands-on developer guides.
* **Official GitHub Copilot Features:** [https://gh.io/ghcopilot-features](https://gh.io/ghcopilot-features) — Full feature matrix and updates.
* **Official YouTube Broadcast:** [YouTube: GitHub Copilot Day Live (ID: 0kOXsQUNzss)](https://www.youtube.com/watch?v=0kOXsQUNzss).
* **GitHub Universe Conference:** [https://githubuniverse.com/](https://githubuniverse.com/) — Flagship annual GitHub developer conference.

### 📚 Open Source Repositories & Protocols
* **Agent Host Protocol (AHP):** [`microsoft/agent-host-protocol`](https://github.com/microsoft/agent-host-protocol) — Standard open protocol for decoupling agent runtimes from frontend clients.
* **GitHub Copilot SDK:** [`github/copilot-sdk`](https://github.com/github/copilot-sdk) — SDK for programmatically invoking, extending, and embedding the Copilot Agent Runtime.
* **Matt Pocock's Agent Skills:** [`mattpocock/skills`](https://github.com/mattpocock/skills) — Repository of reusable agent skills (including the `Show Me` visual architecture generator).
* **Model Context Protocol (MCP):** [https://modelcontextprotocol.io/](https://modelcontextprotocol.io/) — Open specification for connecting agents to external tools, local files, and browser canvases.
* **Visual Studio Code:** [`microsoft/vscode`](https://github.com/microsoft/vscode) — The open-source code editor supporting agent mode, MCP, and BYOK.

### 🔬 Research & Papers
* **Project HydraFusion / HyDRA Research:** [Microsoft Research: HyDRA - Hybrid Dynamic Routing Architecture](https://arxiv.org/abs/2406.18665) — Technical publication by Aashna Garg et al. on cost-effective, high-accuracy multi-model orchestration.
* **GitHub Technology Blog:** [https://github.blog/](https://github.blog/) — Announcements and engineering deep-dives into agent-native development.

### 🎙️ Community, Media & Podcasts
* **Syntax FM (Wes Bos & Scott Tolinski):** [https://syntax.fm/](https://syntax.fm/) — Leading web development podcast covering AI tools and front-end architectures.
* **Merge Conflict Podcast (James Montemagno & Frank Krueger):** [https://www.mergeconflict.fm/](https://www.mergeconflict.fm/) — Weekly developer podcast discussing AI, mobile, and cloud software engineering.
* **Burke Holland on YouTube:** [Burke Holland Developer Channel](https://www.youtube.com/@BurkeHolland) — Tutorials on VS Code tips, Copilot hacks, and agentic workflows.
"""

# Append or inject into notes before the closing
if "## 👥 Featured Speakers & Profiles" not in notes:
    # Insert before Actionable Developer Takeaways or at end
    parts = notes.split("## Actionable Developer Takeaways & Best Practices")
    if len(parts) == 2:
        new_notes = parts[0] + speakers_section + "\n" + resources_section + "\n\n## Actionable Developer Takeaways & Best Practices" + parts[1]
    else:
        new_notes = notes + "\n" + speakers_section + "\n" + resources_section

    with open("GitHub_Copilot_Day_Full_Notes.md", "w", encoding="utf-8") as f:
        f.write(new_notes)
    print("Updated GitHub_Copilot_Day_Full_Notes.md with speakers and resources.")

# Now update README.md
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

if "## 👥 Featured Speakers & Profiles" not in readme:
    readme_additions = speakers_section + "\n" + resources_section
    new_readme = readme + "\n" + readme_additions
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_readme)
    print("Updated README.md with speakers and resources.")
