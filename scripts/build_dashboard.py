import json, re

# Read the full markdown notes
with open("GitHub_Copilot_Day_Full_Notes.md", "r", encoding="utf-8") as f:
    notes_md = f.read()

# Chapters definition with seconds for YouTube API
chapters = [
    {"time": "00:00:00", "sec": 0, "title": "Pre-Stream Countdown", "speaker": "Intro & Slate", "tag": "Intro"},
    {"time": "00:08:00", "sec": 480, "title": "Welcome & Keynote Kickoff", "speaker": "Burke Holland, Pierce Boggan, Kyle Daigle (GitHub COO)", "tag": "Keynote"},
    {"time": "00:15:20", "sec": 920, "title": "Dream It, Build It, Ship It", "speaker": "James Montemagno & Pierce Boggan", "tag": "Copilot App"},
    {"time": "00:46:00", "sec": 2760, "title": "Agent Skills: Codifying Expertise", "speaker": "Matt Pocock", "tag": "Agent Skills"},
    {"time": "01:07:00", "sec": 4020, "title": "Inside Project HydraFusion: Multi-Model Orchestration", "speaker": "Julia Kasper & Aashna Garg", "tag": "HydraFusion"},
    {"time": "01:23:00", "sec": 4980, "title": "Copilot Everywhere: Multi-Surface Continuity", "speaker": "Meagan Cojocar", "tag": "Continuity"},
    {"time": "01:37:45", "sec": 5865, "title": "Claude, Codex, and BYOK in GitHub Copilot", "speaker": "Tyler Leonhardt", "tag": "BYOK"},
    {"time": "01:48:00", "sec": 6480, "title": "One Session, Every Surface: Agent Runtime & SDK", "speaker": "Patrick Nikoletich", "tag": "Agent Host Protocol"},
    {"time": "02:08:00", "sec": 7680, "title": "Live Coding Marathon: Building a 3D Foldable Device Emulator", "speaker": "Wes Bos, Burke Holland, Pierce Boggan & Friends", "tag": "Live Coding"}
]

# Speakers definition
speakers = [
    {"name": "Kyle Daigle", "role": "Chief Operating Officer (COO), GitHub", "github": "kdaigle", "linkedin": "kyledaigle", "bio": "Leading GitHub operations, culture, and developer platform evolution."},
    {"name": "Burke Holland", "role": "Principal Developer Advocate, Microsoft", "github": "burkeholland", "linkedin": "burkeholland", "bio": "Host of Copilot Day, creating developer productivity workflows and VS Code tutorials."},
    {"name": "Pierce Boggan", "role": "Product Lead, VS Code & Copilot, Microsoft", "github": "pierceboggan", "linkedin": "pierceboggan", "bio": "Leading product roadmap for VS Code agent mode and autonomous developer tooling."},
    {"name": "James Montemagno", "role": "Principal Lead Program Manager, Microsoft", "github": "jamesmontemagno", "linkedin": "jamesmontemagno", "bio": "Merge Conflict host, demonstrating the GitHub Copilot App and MCP Canvas tests."},
    {"name": "Matt Pocock", "role": "TypeScript Educator & Creator of Skills", "github": "mattpocock", "linkedin": "mattpocock", "bio": "Creator of Total TypeScript and the Show Me visual architecture skill for agents."},
    {"name": "Julia Kasper", "role": "Senior Product Manager, GitHub Copilot", "github": "juliakaspar", "linkedin": "juliakasper", "bio": "Driving model evaluation, Checkpoint Bench, and multi-model agent experiences."},
    {"name": "Aashna Garg", "role": "Principal Applied Scientist (Code AI), Microsoft", "github": "aashnagarg", "linkedin": "aashnagarg", "bio": "Lead researcher and author on HyDRA (Hybrid Dynamic Routing Architecture)."},
    {"name": "Meagan Cojocar", "role": "Product Manager, GitHub Copilot Integrations", "github": "meagancojocar", "linkedin": "meagancojocar", "bio": "Leading multi-surface continuity across GitHub Mobile, Slack, and Microsoft Teams."},
    {"name": "Tyler Leonhardt", "role": "Senior Software Engineer, VS Code & Copilot", "github": "TylerLeonhardt", "linkedin": "tylerleonhardt", "bio": "Building model choice, Anthropic Claude integration, and BYOK into VS Code."},
    {"name": "Patrick Nikoletich", "role": "Principal Software Engineer, Copilot Runtime", "github": "patniko", "linkedin": "patricknikoletich", "bio": "Architecting the Agent Host Protocol (AHP) and Copilot SDK runtime decoupling."},
    {"name": "Wes Bos", "role": "Full-Stack Educator & Syntax Podcast Host", "github": "wesbos", "linkedin": "wesbos", "bio": "Live pair programming and building the 3D foldable dual-screen emulator live on stream."}
]

# Keyframe gallery
frames = [
    {"file": "frames/frame_10s.jpg", "sec": 10, "label": "Title Card: GitHub Copilot Day"},
    {"file": "frames/frame_300s.jpg", "sec": 300, "label": "Pre-Stream Live Countdown"},
    {"file": "frames/frame_600s.jpg", "sec": 600, "label": "Kyle Daigle Keynote Kickoff"},
    {"file": "frames/frame_1200s.jpg", "sec": 1200, "label": "GitHub Copilot App & Multi-Repo Agents"},
    {"file": "frames/frame_1800s.jpg", "sec": 1800, "label": "James Montemagno Canvas & MCP Testing"},
    {"file": "frames/frame_2400s.jpg", "sec": 2400, "label": "Repo Actions & Autonomous Issue Triage"},
    {"file": "frames/frame_3600s.jpg", "sec": 3600, "label": "Matt Pocock 'Show Me' Visual Architecture"},
    {"file": "frames/frame_4800s.jpg", "sec": 4800, "label": "Draft PR Generation from Agent Workflows"},
    {"file": "frames/frame_6000s.jpg", "sec": 6000, "label": "HydraFusion Multi-Model Benchmarks"},
    {"file": "frames/frame_7200s.jpg", "sec": 7200, "label": "Agent Host Protocol (AHP) Architecture"},
    {"file": "frames/frame_8400s.jpg", "sec": 8400, "label": "Copilot Mobile & Teams Cross-Surface Handoff"},
    {"file": "frames/frame_9600s.jpg", "sec": 9600, "label": "Tyler Leonhardt: BYOK in VS Code"},
    {"file": "frames/frame_10800s.jpg", "sec": 10800, "label": "Live Coding: Burke & Pierce Multi-Agent Setup"},
    {"file": "frames/frame_12000s.jpg", "sec": 12000, "label": "Dual-Screen 3D Hardware Model Render"},
    {"file": "frames/frame_13200s.jpg", "sec": 13200, "label": "Knolling Exploded Hardware Parts View"},
    {"file": "frames/frame_14400s.jpg", "sec": 14400, "label": "Interactive Virtual Apps on Foldable Device"},
    {"file": "frames/frame_15000s.jpg", "sec": 15000, "label": "Final Demo Wrap-up & Stream Outro"}
]

# Resources
resources = [
    {"category": "Core Products", "title": "GitHub Copilot App", "url": "https://gh.io/app", "desc": "Native desktop application for managing asynchronous multi-agent coding sessions."},
    {"category": "Core Products", "title": "GitHub Copilot CLI", "url": "https://docs.github.com/en/copilot/github-copilot-in-the-cli", "desc": "Terminal-native agent workflows with HydraFusion dynamic routing."},
    {"category": "Core Products", "title": "Copilot Dev Days", "url": "https://copilot-dev-days.github.io/", "desc": "Official hands-on workshops, guided labs, and tutorials."},
    {"category": "Core Products", "title": "Copilot Feature Catalog", "url": "https://gh.io/ghcopilot-features", "desc": "Official breakdown of agent capabilities, models, and pricing."},
    {"category": "Protocols & SDKs", "title": "Agent Host Protocol (AHP)", "url": "https://github.com/microsoft/agent-host-protocol", "desc": "Standard open protocol decoupling agent execution runtimes from client UIs."},
    {"category": "Protocols & SDKs", "title": "GitHub Copilot SDK", "url": "https://github.com/github/copilot-sdk", "desc": "SDK to embed, control, and orchestrate the Copilot Agent Runtime."},
    {"category": "Protocols & SDKs", "title": "Matt Pocock's Agent Skills", "url": "https://github.com/mattpocock/skills", "desc": "Reusable agent skills including 'Show Me' visual architecture sketches."},
    {"category": "Protocols & SDKs", "title": "Model Context Protocol (MCP)", "url": "https://modelcontextprotocol.io/", "desc": "Standard for exposing custom tools and data sources to AI agents."},
    {"category": "Research", "title": "HyDRA Research Paper", "url": "https://arxiv.org/abs/2406.18665", "desc": "Microsoft Research publication on Hybrid Dynamic Routing Architecture by Aashna Garg et al."},
    {"category": "Research", "title": "GitHub Engineering Blog", "url": "https://github.blog/", "desc": "Official blog covering AI architectures, agent benchmarks, and release posts."}
]

html_template = f"""<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>GitHub Copilot Day 2026: Interactive Video Dashboard & Notes</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          colors: {{
            ghdark: '#0d1117',
            ghsurface: '#161b22',
            ghborder: '#30363d',
            ghgreen: '#238636',
            ghgreenlight: '#2ea043',
            ghblue: '#58a6ff',
            ghpurple: '#bc8cff'
          }}
        }}
      }}
    }}
  </script>
  <style>
    body {{ background-color: #0d1117; color: #c9d1d9; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }}
    .scrollbar-thin::-webkit-scrollbar {{ width: 6px; height: 6px; }}
    .scrollbar-thin::-webkit-scrollbar-thumb {{ background: #30363d; border-radius: 3px; }}
    .scrollbar-thin::-webkit-scrollbar-track {{ background: transparent; }}
    .prose-custom h1, .prose-custom h2, .prose-custom h3 {{ color: #f0f6fc; font-weight: 600; margin-top: 1.5rem; margin-bottom: 0.75rem; }}
    .prose-custom h1 {{ font-size: 1.75rem; border-bottom: 1px solid #30363d; padding-bottom: 0.5rem; }}
    .prose-custom h2 {{ font-size: 1.35rem; border-bottom: 1px solid #21262d; padding-bottom: 0.4rem; }}
    .prose-custom h3 {{ font-size: 1.15rem; color: #58a6ff; }}
    .prose-custom p, .prose-custom li {{ line-height: 1.6; color: #c9d1d9; }}
    .prose-custom ul {{ list-style-type: disc; padding-left: 1.5rem; margin-bottom: 1rem; }}
    .prose-custom table {{ width: 100%; border-collapse: collapse; margin: 1rem 0; }}
    .prose-custom th, .prose-custom td {{ border: 1px solid #30363d; padding: 0.5rem 0.75rem; text-align: left; }}
    .prose-custom th {{ background-color: #161b22; color: #f0f6fc; }}
    .prose-custom code {{ background-color: #21262d; color: #ff7b72; padding: 0.2rem 0.4rem; border-radius: 4px; font-size: 0.875rem; }}
    .prose-custom a {{ color: #58a6ff; text-decoration: none; }}
    .prose-custom a:hover {{ text-decoration: underline; }}
    .prose-custom blockquote {{ border-left: 4px solid #388bfd; padding-left: 1rem; color: #8b949e; margin: 1rem 0; }}
  </style>
</head>
<body class="min-h-screen flex flex-col">

  <!-- Top Header Navigation -->
  <header class="bg-ghsurface border-b border-ghborder sticky top-0 z-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
      <div class="flex items-center space-x-3">
        <i class="fa-brands fa-github text-3xl text-white"></i>
        <div>
          <h1 class="font-bold text-white text-lg tracking-wide flex items-center gap-2">
            GitHub Copilot Day <span class="text-xs bg-ghgreen px-2 py-0.5 rounded-full text-white font-normal">2026 Live</span>
          </h1>
          <p class="text-xs text-gray-400">September 10, 2026 • 4h 11m • Video Analysis & Interactive Notes</p>
        </div>
      </div>

      <div class="flex items-center space-x-3">
        <a href="https://github.com/nandhakumar-murugan/github-copilot-day-2026-analysis" target="_blank" class="text-xs bg-ghborder hover:bg-gray-700 text-white px-3 py-1.5 rounded-md flex items-center gap-2 transition">
          <i class="fa-brands fa-github"></i> Star Repo
        </a>
        <a href="https://www.youtube.com/watch?v=0kOXsQUNzss" target="_blank" class="text-xs bg-red-600 hover:bg-red-700 text-white px-3 py-1.5 rounded-md flex items-center gap-2 transition">
          <i class="fa-brands fa-youtube"></i> Watch on YouTube
        </a>
      </div>
    </div>
  </header>

  <!-- Main Layout -->
  <main class="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6 grid grid-cols-1 lg:grid-cols-12 gap-6">

    <!-- Left Column: Video Player, Chapters, Keyframe Gallery (5 cols on desktop) -->
    <div class="lg:col-span-5 space-y-6">
      
      <!-- Video Player Card -->
      <div class="bg-ghsurface border border-ghborder rounded-xl overflow-hidden shadow-lg sticky top-20">
        <div class="relative aspect-video bg-black">
          <iframe id="yt-player" class="w-full h-full"
            src="https://www.youtube.com/embed/0kOXsQUNzss?enablejsapi=1&origin={re.escape('')}"
            title="GitHub Copilot Day Live Stream" frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen></iframe>
        </div>
        <div class="p-3 bg-ghsurface flex items-center justify-between border-t border-ghborder text-xs">
          <span class="text-gray-400 flex items-center gap-1.5">
            <span class="w-2 h-2 rounded-full bg-red-500 animate-ping"></span> Live Broadcast Recording
          </span>
          <span id="current-timestamp" class="text-ghblue font-mono font-bold">00:00:00</span>
        </div>

        <!-- Quick Jump Chapter Carousel/List -->
        <div class="p-3 border-t border-ghborder">
          <div class="flex items-center justify-between mb-2">
            <h3 class="text-xs font-semibold text-gray-300 uppercase tracking-wider flex items-center gap-1.5">
              <i class="fa-regular fa-clock text-ghgreen"></i> Chapters (Click to Jump)
            </h3>
            <span class="text-[10px] text-gray-500">{len(chapters)} Chapters</span>
          </div>
          <div class="max-h-60 overflow-y-auto scrollbar-thin space-y-1.5 pr-1" id="chapters-list">
            <!-- Rendered by JS -->
          </div>
        </div>
      </div>

      <!-- Keyframe Carousel / Visual Explorer -->
      <div class="bg-ghsurface border border-ghborder rounded-xl p-4 shadow-lg">
        <div class="flex items-center justify-between mb-3">
          <h3 class="text-xs font-semibold text-gray-300 uppercase tracking-wider flex items-center gap-1.5">
            <i class="fa-regular fa-image text-ghpurple"></i> Keyframe Visuals ({len(frames)})
          </h3>
          <span class="text-[10px] text-gray-500">Extracted Key Moments</span>
        </div>
        <div class="grid grid-cols-2 sm:grid-cols-3 gap-2" id="keyframe-grid">
          <!-- Rendered by JS -->
        </div>
      </div>

    </div>

    <!-- Right Column: Tabs (Notes, Speakers, Resources, Search) (7 cols on desktop) -->
    <div class="lg:col-span-7 space-y-6">

      <!-- Navigation Tabs -->
      <div class="bg-ghsurface border border-ghborder rounded-xl p-2 flex space-x-1 sm:space-x-2">
        <button onclick="switchTab('notes')" id="tab-btn-notes" class="flex-1 py-2 px-3 text-xs sm:text-sm font-medium rounded-lg text-white bg-ghborder transition flex items-center justify-center gap-2">
          <i class="fa-regular fa-file-lines text-ghgreen"></i> Detailed Notes
        </button>
        <button onclick="switchTab('speakers')" id="tab-btn-speakers" class="flex-1 py-2 px-3 text-xs sm:text-sm font-medium rounded-lg text-gray-400 hover:text-white transition flex items-center justify-center gap-2">
          <i class="fa-solid fa-users text-ghblue"></i> Speakers ({len(speakers)})
        </button>
        <button onclick="switchTab('resources')" id="tab-btn-resources" class="flex-1 py-2 px-3 text-xs sm:text-sm font-medium rounded-lg text-gray-400 hover:text-white transition flex items-center justify-center gap-2">
          <i class="fa-solid fa-link text-ghpurple"></i> Resources & Docs
        </button>
      </div>

      <!-- Tab Content: Detailed Notes -->
      <div id="tab-notes" class="bg-ghsurface border border-ghborder rounded-xl p-6 shadow-lg space-y-6">
        <!-- Search filter inside notes -->
        <div class="relative">
          <i class="fa-solid fa-magnifying-glass absolute left-3 top-3 text-gray-400 text-xs"></i>
          <input type="text" id="notes-filter" oninput="filterNotes()" placeholder="Search topics, models, HydraFusion, Agent Skills, AHP, speakers..." 
            class="w-full bg-[#0d1117] border border-ghborder rounded-lg pl-9 pr-4 py-2 text-xs text-white placeholder-gray-500 focus:outline-none focus:border-ghblue transition">
        </div>

        <div id="notes-body" class="prose-custom max-w-none text-sm">
          <!-- Markdown injected here -->
        </div>
      </div>

      <!-- Tab Content: Speakers Directory -->
      <div id="tab-speakers" class="hidden space-y-4">
        <div class="bg-ghsurface border border-ghborder rounded-xl p-4">
          <h2 class="text-base font-bold text-white flex items-center gap-2 mb-1">
            <i class="fa-solid fa-users text-ghblue"></i> Event Speakers & Leadership
          </h2>
          <p class="text-xs text-gray-400">Connect with the GitHub & Microsoft engineers and educators who presented during Copilot Day.</p>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4" id="speakers-grid">
          <!-- Rendered by JS -->
        </div>
      </div>

      <!-- Tab Content: Resources & Documentation -->
      <div id="tab-resources" class="hidden space-y-4">
        <div class="bg-ghsurface border border-ghborder rounded-xl p-4">
          <h2 class="text-base font-bold text-white flex items-center gap-2 mb-1">
            <i class="fa-solid fa-book-bookmark text-ghpurple"></i> Essential Resources, Repos & Papers
          </h2>
          <p class="text-xs text-gray-400">Direct documentation links, open-source repositories, protocols, and technical research referenced during the event.</p>
        </div>
        <div class="space-y-3" id="resources-list">
          <!-- Rendered by JS -->
        </div>
      </div>

    </div>

  </main>

  <!-- Modal for Keyframe Preview -->
  <div id="image-modal" class="fixed inset-0 bg-black/80 z-50 hidden flex items-center justify-center p-4" onclick="closeModal()">
    <div class="max-w-3xl w-full bg-ghsurface border border-ghborder rounded-xl overflow-hidden p-4 space-y-3" onclick="event.stopPropagation()">
      <div class="flex items-center justify-between">
        <h4 id="modal-title" class="text-sm font-semibold text-white"></h4>
        <button onclick="closeModal()" class="text-gray-400 hover:text-white"><i class="fa-solid fa-xmark text-lg"></i></button>
      </div>
      <img id="modal-img" src="" alt="Frame preview" class="w-full rounded-lg border border-ghborder">
      <div class="flex justify-between items-center pt-2">
        <span id="modal-time" class="text-xs text-ghblue font-mono"></span>
        <button id="modal-jump-btn" class="text-xs bg-ghgreen hover:bg-ghgreenlight text-white px-3 py-1.5 rounded-md flex items-center gap-1.5 transition">
          <i class="fa-solid fa-play text-[10px]"></i> Jump to this moment in video
        </button>
      </div>
    </div>
  </div>

  <!-- Footer -->
  <footer class="bg-ghsurface border-t border-ghborder py-6 mt-12 text-center text-xs text-gray-500">
    <p>GitHub Copilot Day 2026 Analysis Dashboard • Built with automated AI transcription, keyframe sampling & document extraction.</p>
    <p class="mt-1">Maintained on GitHub by <a href="https://github.com/nandhakumar-murugan" target="_blank" class="text-ghblue hover:underline">@nandhakumar-murugan</a></p>
  </footer>

  <!-- App Data & Scripts -->
  <script>
    const chaptersData = {json.dumps(chapters)};
    const speakersData = {json.dumps(speakers)};
    const framesData = {json.dumps(frames)};
    const resourcesData = {json.dumps(resources)};
    const fullNotesMarkdown = {json.dumps(notes_md)};

    let activeTab = 'notes';

    // Seek YouTube Player
    function seekTo(seconds, title) {{
      const iframe = document.getElementById('yt-player');
      iframe.src = `https://www.youtube.com/embed/0kOXsQUNzss?autoplay=1&start=${{seconds}}&enablejsapi=1`;
      
      const h = Math.floor(seconds / 3600).toString().padStart(2, '0');
      const m = Math.floor((seconds % 3600) / 60).toString().padStart(2, '0');
      const s = Math.floor(seconds % 60).toString().padStart(2, '0');
      document.getElementById('current-timestamp').innerText = `${{h}}:${{m}}:${{s}} • ${{title}}`;
      
      // highlight active chapter button
      document.querySelectorAll('.chapter-item').forEach(el => el.classList.remove('border-ghblue', 'bg-ghborder/50'));
      const activeEl = document.getElementById(`chapter-${{seconds}}`);
      if (activeEl) activeEl.classList.add('border-ghblue', 'bg-ghborder/50');
    }}

    // Render Chapters
    function renderChapters() {{
      const container = document.getElementById('chapters-list');
      container.innerHTML = chaptersData.map(c => `
        <div id="chapter-${{c.sec}}" onclick="seekTo(${{c.sec}}, '${{c.title.replace(/'/g, "\\\\'")}}')" 
          class="chapter-item cursor-pointer p-2 rounded-lg bg-ghsurface hover:bg-ghborder border border-ghborder transition flex items-start justify-between gap-2 group">
          <div>
            <div class="text-xs font-medium text-white group-hover:text-ghblue transition">${{c.title}}</div>
            <div class="text-[11px] text-gray-400 truncate max-w-[260px]">${{c.speaker}}</div>
          </div>
          <span class="text-[10px] font-mono text-ghgreen bg-ghgreen/10 border border-ghgreen/30 px-1.5 py-0.5 rounded whitespace-nowrap">${{c.time}}</span>
        </div>
      `).join('');
    }}

    // Render Keyframes
    function renderKeyframes() {{
      const grid = document.getElementById('keyframe-grid');
      grid.innerHTML = framesData.map(f => `
        <div onclick="openModal('${{f.file}}', '${{f.label}}', ${{f.sec}})" class="cursor-pointer group relative rounded-lg overflow-hidden border border-ghborder bg-black aspect-video">
          <img src="${{f.file}}" alt="${{f.label}}" class="w-full h-full object-cover group-hover:scale-105 transition duration-300">
          <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent opacity-80 group-hover:opacity-100 transition p-1.5 flex flex-col justify-end">
            <span class="text-[9px] text-white font-medium line-clamp-1">${{f.label}}</span>
            <span class="text-[8px] font-mono text-ghblue">${{Math.floor(f.sec/60)}}m ${{f.sec%60}}s</span>
          </div>
        </div>
      `).join('');
    }}

    // Render Speakers
    function renderSpeakers() {{
      const grid = document.getElementById('speakers-grid');
      grid.innerHTML = speakersData.map(s => `
        <div class="bg-ghsurface border border-ghborder rounded-xl p-4 space-y-3 hover:border-gray-500 transition">
          <div class="flex items-center space-x-3">
            <img src="https://github.com/${{s.github}}.png" alt="${{s.name}}" class="w-12 h-12 rounded-full border border-ghborder object-cover" onerror="this.src='https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png'">
            <div>
              <h3 class="font-bold text-white text-sm">${{s.name}}</h3>
              <p class="text-[11px] text-gray-400 line-clamp-1">${{s.role}}</p>
            </div>
          </div>
          <p class="text-xs text-gray-300 leading-relaxed">${{s.bio}}</p>
          <div class="flex items-center space-x-2 pt-1 border-t border-ghborder">
            <a href="https://github.com/${{s.github}}" target="_blank" class="text-xs bg-ghborder hover:bg-gray-700 text-white px-2.5 py-1 rounded flex items-center gap-1.5 transition">
              <i class="fa-brands fa-github"></i> @${{s.github}}
            </a>
            <a href="https://www.linkedin.com/in/${{s.linkedin}}" target="_blank" class="text-xs bg-[#0a66c2]/20 hover:bg-[#0a66c2]/30 text-[#58a6ff] border border-[#0a66c2]/40 px-2.5 py-1 rounded flex items-center gap-1.5 transition">
              <i class="fa-brands fa-linkedin"></i> LinkedIn
            </a>
          </div>
        </div>
      `).join('');
    }}

    // Render Resources
    function renderResources() {{
      const list = document.getElementById('resources-list');
      list.innerHTML = resourcesData.map(r => `
        <div class="bg-ghsurface border border-ghborder rounded-xl p-3.5 flex items-start justify-between hover:border-ghblue transition group">
          <div class="space-y-1">
            <div class="flex items-center gap-2">
              <span class="text-[10px] font-semibold uppercase tracking-wider px-2 py-0.5 rounded bg-ghborder text-gray-300">${{r.category}}</span>
              <a href="${{r.url}}" target="_blank" class="font-semibold text-white group-hover:text-ghblue transition text-sm flex items-center gap-1.5">
                ${{r.title}} <i class="fa-solid fa-arrow-up-right-from-square text-[10px] text-gray-400"></i>
              </a>
            </div>
            <p class="text-xs text-gray-400">${{r.desc}}</p>
          </div>
          <a href="${{r.url}}" target="_blank" class="text-xs text-ghblue hover:underline whitespace-nowrap ml-4 self-center font-medium">Open <i class="fa-solid fa-chevron-right text-[10px]"></i></a>
        </div>
      `).join('');
    }}

    // Tab Switching
    function switchTab(tab) {{
      activeTab = tab;
      ['notes', 'speakers', 'resources'].forEach(t => {{
        const btn = document.getElementById(`tab-btn-${{t}}`);
        const content = document.getElementById(`tab-${{t}}`);
        if (t === tab) {{
          btn.className = "flex-1 py-2 px-3 text-xs sm:text-sm font-medium rounded-lg text-white bg-ghborder transition flex items-center justify-center gap-2";
          content.classList.remove('hidden');
        }} else {{
          btn.className = "flex-1 py-2 px-3 text-xs sm:text-sm font-medium rounded-lg text-gray-400 hover:text-white transition flex items-center justify-center gap-2";
          content.classList.add('hidden');
        }}
      }});
    }}

    // Keyframe Modal
    function openModal(imgSrc, title, seconds) {{
      document.getElementById('modal-img').src = imgSrc;
      document.getElementById('modal-title').innerText = title;
      const h = Math.floor(seconds / 3600).toString().padStart(2, '0');
      const m = Math.floor((seconds % 3600) / 60).toString().padStart(2, '0');
      const s = Math.floor(seconds % 60).toString().padStart(2, '0');
      document.getElementById('modal-time').innerText = `Timestamp: ${{h}}:${{m}}:${{s}} (${{seconds}}s)`;
      document.getElementById('modal-jump-btn').onclick = () => {{
        closeModal();
        seekTo(seconds, title);
      }};
      document.getElementById('image-modal').classList.remove('hidden');
    }}

    function closeModal() {{
      document.getElementById('image-modal').classList.add('hidden');
    }}

    // Filter Notes
    function filterNotes() {{
      const query = document.getElementById('notes-filter').value.toLowerCase().trim();
      const body = document.getElementById('notes-body');
      if (!query) {{
        body.innerHTML = marked.parse(fullNotesMarkdown);
        return;
      }}
      // Simple filter: split paragraphs, show matching
      const paragraphs = fullNotesMarkdown.split('\\n\\n');
      const filtered = paragraphs.filter(p => p.toLowerCase().includes(query));
      if (filtered.length === 0) {{
        body.innerHTML = `<div class="p-8 text-center text-gray-500">No matching sections found for "<strong>${{query}}</strong>".</div>`;
      }} else {{
        body.innerHTML = marked.parse(filtered.join('\\n\\n'));
      }}
    }}

    // Initialization
    window.addEventListener('DOMContentLoaded', () => {{
      renderChapters();
      renderKeyframes();
      renderSpeakers();
      renderResources();
      document.getElementById('notes-body').innerHTML = marked.parse(fullNotesMarkdown);
    }});
  </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"Generated index.html successfully ({len(html_template)} bytes)")
