<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=28&duration=2800&pause=900&color=58A6FF&center=true&vCenter=true&width=720&height=64&lines=Moamen+Ghareeb;AI+Engineer+%C2%B7+Cairo%2C+Egypt;Production+agentic+systems+at+White+Guard;5-layer+multi-agent+engine+%E2%80%A2+3+MCP+servers;Voice-first+developer+tools+on+the+side" alt="Moamen Ghareeb — AI Engineer" />

<br/>

<a href="https://www.linkedin.com/in/moamen-ghareeb-b4a1512b9"><img src="https://img.shields.io/badge/LinkedIn-Moamen_Ghareeb-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>&nbsp;<a href="mailto:moamen.ghareeb.11@gmail.com"><img src="https://img.shields.io/badge/Email-moamen.ghareeb.11-EA4335?style=flat-square&logo=gmail&logoColor=white" alt="Email" /></a>&nbsp;<a href="https://github.com/moamen1358?tab=repositories"><img src="https://img.shields.io/badge/Open_to-collaboration-1F6FEB?style=flat-square" alt="Open to collaboration" /></a>

<br/><br/>

<a href="https://github.com/moamen1358?tab=followers"><img src="https://img.shields.io/github/followers/moamen1358?style=flat-square&logo=github&label=Followers&color=58A6FF&labelColor=0D1117" alt="Followers" /></a>&nbsp;<img src="https://img.shields.io/github/stars/moamen1358?style=flat-square&affiliations=OWNER&color=F77F00&logo=github&label=Stars&labelColor=0D1117" alt="Stars" />&nbsp;<img src="https://komarev.com/ghpvc/?username=moamen1358&style=flat-square&color=58A6FF&label=Profile+views&labelColor=0D1117" alt="Profile views" />

</div>

---

## About

I'm an AI Engineer at **White Guard** in Cairo, specializing in production
agentic systems. I architect multi-agent runtimes, author Anthropic
Model Context Protocol (MCP) servers, design async intelligence
pipelines, and ship the automation infrastructure the business runs on.
Claude is my primary AI co-engineer.

By night I publish small, focused open-source tools — voice-first
interfaces, web automation, content pipelines. The pattern across
everything I publish is the same: a single binary or a single command
that does one job well, with a real README, clear defaults, and no
surprises.

## Career highlights

| | What I built |
|---|---|
| **5-layer multi-agent intelligence engine** | Architected a deterministic decision pipeline (signal → research → knowledge base → synthesis → generation) replacing ad-hoc prompt chains with explicit agent boundaries and full auditability. |
| **3 Anthropic MCP servers** | Python state server with 8 versioned SQL migrations + audit tooling, TypeScript SEO/site-audit scanner with crawler and worker pool, Python Google Trends MCP — structured tool surfaces any Anthropic-compatible agent can call. |
| **In-house multi-agent runtime** | Claude / Codex / Groq / Ollama orchestration with Chrome attach-mode browser automation, persistent state, scheduled cron jobs, sub-agent delegation, and a Telegram I/O surface. |
| **Custom Claude Code stack** | 12 slash commands, 8 sub-agents, and 8 skills that codify research, validation, and review patterns into reusable, deterministic primitives. |
| **Async multi-source intelligence pipeline** | aggregates signals from Apollo.io, Tavily, Perplexity, and LinkedIn; analyzed by Claude Opus 4.6 using a tiered recency framework (FRESH 0–30d, RECENT 31–90d, older). |
| **1,400+ verified partner records** | Reverse-engineered hostile vendor partner directories (JS-heavy, Cloudflare-protected) across Cisco, Fortinet, and 22 vendor catalogs in Saudi Arabia and Egypt with strict domain verification. |
| **Production infrastructure** | Docker n8n + Postgres + Qdrant + Cloudflare Tunnel + Grafana running 20 live workflows (~370 nodes) with global error workflow and Git-versioned auto-export. |

Earlier (May–Dec 2025) I worked freelance on **adversarial ML** — replicating
research on data poisoning, evaluating model robustness under label-flip
attacks across UNSW_NB15, CICIDS-2017, CTU-13, and Botnet datasets, and
demonstrating that a stacked ensemble outperformed every other classifier
tested on both detection accuracy and poison resistance.

## Open-source projects

<table>
<tr>
<td valign="top" width="50%">

### [voci](https://github.com/moamen1358/voci)

Real-time speech-to-text and translation overlay for Linux. Streaming
NVIDIA Parakeet on the local GPU with optional cloud STT (Deepgram,
AssemblyAI, Soniox) and cloud LLM translation (Cerebras, Google
Gemini). Hybrid mode keeps live partials on local OPUS-MT.

`Python` &nbsp;`PySide6` &nbsp;`CUDA` &nbsp;`NVIDIA NeMo`

</td>
<td valign="top" width="50%">

### [f9-talk](https://github.com/moamen1358/f9-talk)

System-wide hold-to-talk dictation for Linux. Single
statically-linked Rust binary distributed as a `.deb`. Cloud or local
STT, audio-reactive overlay, optional translation.

`Rust` &nbsp;`tokio` &nbsp;`egui` &nbsp;`Linux`

</td>
</tr>

<tr>
<td valign="top" width="50%">

### [WannaScrape](https://github.com/moamen1358/WannaScrape)

Production-grade Python web scraper with Playwright fingerprint
rotation, plugin-based bot-detection (Cloudflare, Akamai,
PerimeterX, DataDome), CAPTCHA solving, and proxy rotation. CLI and
FastAPI service.

`Python` &nbsp;`Playwright` &nbsp;`FastAPI`

</td>
<td valign="top" width="50%">

### [WannaSearch](https://github.com/moamen1358/WannaSearch)

Google News search CLI and HTTP API. Company-focused queries,
time-range filtering, automatic per-company log archives with Cairo
timezone timestamps.

`Python` &nbsp;`FastAPI` &nbsp;`CLI`

</td>
</tr>

<tr>
<td valign="top" width="50%">

### [WannaClick](https://github.com/moamen1358/WannaClick)

Browser extension that auto-clicks any text-matched element on any
page. Configurable random delays, single-page-app navigation
support, on-page status indicator.

`JavaScript` &nbsp;`Browser Extension`

</td>
<td valign="top" width="50%">

### [LUMINAFLOW](https://github.com/moamen1358/LUMINAFLOW)

Desktop automation tool that records mouse, keyboard, and gesture
input on Linux and replays it on demand. tkinter GUI, persistent
action lists.

`Python` &nbsp;`tkinter` &nbsp;`pynput`

</td>
</tr>

<tr>
<td valign="top" colspan="2" align="center">

### [attendance-cv](https://github.com/moamen1358/attendance-cv)

Face-recognition attendance system. YOLOv11 + ArcFace (InsightFace) + ChromaDB on a Streamlit frontend, with role-based dashboards for administrators, teachers, and students. Originally my graduation project.

`Python` &nbsp;`YOLOv11` &nbsp;`ArcFace` &nbsp;`ChromaDB` &nbsp;`Streamlit`

</td>
</tr>
</table>

## How I work

**Languages** &nbsp; <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" /> <img src="https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white" alt="Rust" /> <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript" /> <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black" alt="JavaScript" /> <img src="https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=postgresql&logoColor=white" alt="SQL" /> <img src="https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white" alt="Bash" />

**AI / agents** &nbsp; <img src="https://img.shields.io/badge/Anthropic_Claude-D4A27F?style=flat-square&logo=anthropic&logoColor=white" alt="Anthropic Claude" /> <img src="https://img.shields.io/badge/Claude_Code-D4A27F?style=flat-square&logo=anthropic&logoColor=white" alt="Claude Code" /> <img src="https://img.shields.io/badge/MCP-1A1A1A?style=flat-square" alt="Model Context Protocol" /> <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white" alt="LangChain" /> <img src="https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white" alt="OpenAI" /> <img src="https://img.shields.io/badge/Gemini-8E75B2?style=flat-square&logo=googlegemini&logoColor=white" alt="Google Gemini" /> <img src="https://img.shields.io/badge/Ollama-000000?style=flat-square&logo=ollama&logoColor=white" alt="Ollama" /> <img src="https://img.shields.io/badge/OpenRouter-0F0F0F?style=flat-square" alt="OpenRouter" /> <img src="https://img.shields.io/badge/Groq-F55036?style=flat-square" alt="Groq" />

**ML / inference** &nbsp; <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" alt="PyTorch" /> <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white" alt="TensorFlow" /> <img src="https://img.shields.io/badge/NVIDIA_NeMo-76B900?style=flat-square&logo=nvidia&logoColor=white" alt="NVIDIA NeMo" /> <img src="https://img.shields.io/badge/CTranslate2-FF6B35?style=flat-square" alt="CTranslate2" /> <img src="https://img.shields.io/badge/ONNX-005CED?style=flat-square&logo=onnx&logoColor=white" alt="ONNX" /> <img src="https://img.shields.io/badge/InsightFace-FF1744?style=flat-square" alt="InsightFace" /> <img src="https://img.shields.io/badge/HuggingFace-FFD21E?style=flat-square&logo=huggingface&logoColor=black" alt="HuggingFace" />

**Cloud STT** &nbsp; <img src="https://img.shields.io/badge/Deepgram-13EF93?style=flat-square&logoColor=black" alt="Deepgram" /> <img src="https://img.shields.io/badge/AssemblyAI-2E76FF?style=flat-square" alt="AssemblyAI" /> <img src="https://img.shields.io/badge/Soniox-1F8AED?style=flat-square" alt="Soniox" /> <img src="https://img.shields.io/badge/Cerebras-FF4500?style=flat-square" alt="Cerebras" />

**Web / UI** &nbsp; <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI" /> <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white" alt="Streamlit" /> <img src="https://img.shields.io/badge/Gradio-FF7C00?style=flat-square&logo=gradio&logoColor=white" alt="Gradio" /> <img src="https://img.shields.io/badge/Qt-41CD52?style=flat-square&logo=qt&logoColor=white" alt="Qt" /> <img src="https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white" alt="Next.js" /> <img src="https://img.shields.io/badge/Tailwind-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white" alt="Tailwind" />

**Automation / scraping** &nbsp; <img src="https://img.shields.io/badge/Playwright-2EAD33?style=flat-square&logo=playwright&logoColor=white" alt="Playwright" /> <img src="https://img.shields.io/badge/n8n-EA4B71?style=flat-square&logo=n8n&logoColor=white" alt="n8n" /> <img src="https://img.shields.io/badge/Apify-FF9013?style=flat-square&logo=apify&logoColor=white" alt="Apify" /> <img src="https://img.shields.io/badge/Tavily-2B59FF?style=flat-square" alt="Tavily" /> <img src="https://img.shields.io/badge/Perplexity-22B8CD?style=flat-square&logo=perplexity&logoColor=white" alt="Perplexity" /> <img src="https://img.shields.io/badge/Apollo.io-2D5BFF?style=flat-square" alt="Apollo.io" />

**Data / databases** &nbsp; <img src="https://img.shields.io/badge/PostgreSQL-336791?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL" /> <img src="https://img.shields.io/badge/Pinecone-1C17FF?style=flat-square&logo=pinecone&logoColor=white" alt="Pinecone" /> <img src="https://img.shields.io/badge/Qdrant-DC244C?style=flat-square&logo=qdrant&logoColor=white" alt="Qdrant" /> <img src="https://img.shields.io/badge/ChromaDB-FF6B35?style=flat-square" alt="ChromaDB" /> <img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white" alt="Pandas" /> <img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white" alt="NumPy" />

**Infrastructure** &nbsp; <img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black" alt="Linux" /> <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker" /> <img src="https://img.shields.io/badge/CUDA-76B900?style=flat-square&logo=nvidia&logoColor=white" alt="CUDA" /> <img src="https://img.shields.io/badge/Cloudflare-F38020?style=flat-square&logo=cloudflare&logoColor=white" alt="Cloudflare Tunnel" /> <img src="https://img.shields.io/badge/Grafana-F46800?style=flat-square&logo=grafana&logoColor=white" alt="Grafana" /> <img src="https://img.shields.io/badge/uv-FFD43B?style=flat-square" alt="uv" /> <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white" alt="Git" />

## Education

**BSc Computer Engineering — First-Class Honors**
Higher Institute of Engineering and Technology, Kafr El-Shaikh
October 2020 – June 2025

## Contribution activity

<div align="center">

<img src="https://github-readme-activity-graph.vercel.app/graph?username=moamen1358&theme=github-compact&hide_border=true&bg_color=00000000&color=58A6FF&line=58A6FF&point=F77F00&area=true&area_color=58A6FF&height=260" alt="Contribution activity over time" />

</div>

## Currently

I'm working on real-time multilingual subtitle quality improvements in
[voci](https://github.com/moamen1358/voci), auto-detection of
presentation context for [f9-talk](https://github.com/moamen1358/f9-talk),
and the next iteration of the partner-portal automation suite at
White Guard.

## Get in touch

Fastest paths: [LinkedIn](https://www.linkedin.com/in/moamen-ghareeb-b4a1512b9)
or [email](mailto:moamen.ghareeb.11@gmail.com). For project-specific
questions, opening an issue on the relevant repository is the surest
way to get a fast response.
