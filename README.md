# 👾 Aviral Srivastava — Offensive AI Researcher | Application Security Engineer | CVE Hunter

![Cyberpunk Header](https://capsule-render.vercel.app/api?type=wave&color=gradient&customColorList=12,20,24,30&text=Aviral%20Srivastava&height=220&fontSize=45&fontColor=ffffff&animation=twinkling&stroke=00FFFF&strokeWidth=2)

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=22&duration=3500&pause=900&color=00FFFF&width=720&center=true&vCenter=true&lines=Discoverer+of+CVE-2026-33017+%E2%80%A2+CISA+KEV;Offensive+AI+%2F+ML+Infrastructure+Security;Agentic+AI+%2B+MCP+%2B+RAG+Exploitation;Kernel+%2B+GPU+%2B+Tokenizer+Memory+Corruption;NIST+OLIR+Contributor;RSA+Security+Scholar+2025+%E2%80%A2+RSAC+Speaker+2026" alt="Typing SVG" />
</p>

<p align="center">
  <a href="https://nvd.nist.gov/vuln/detail/CVE-2026-33017"><img src="https://img.shields.io/badge/CISA_KEV-CVE--2026--33017-%23ff003c?style=for-the-badge&logo=hackthebox&logoColor=white" /></a>
  <img src="https://img.shields.io/badge/CVEs_Assigned-2-%2300ff9f?style=for-the-badge&logo=cve&logoColor=black" />
  <img src="https://img.shields.io/badge/NIST_OLIR-Contributor-%23f59e0b?style=for-the-badge&logo=nist" />
  <img src="https://img.shields.io/badge/RSAC_2026-Speaker-%237c3aed?style=for-the-badge&logo=rsa&logoColor=white" />
</p>

---

## 🏅 RSA Security Scholar 2025

<p align="center">
  <img src="https://img.shields.io/badge/RSA%20Security%20Scholar-2025-%23ff007f?style=for-the-badge&logo=verizon&logoColor=white" />
  <img src="https://img.shields.io/badge/Cybersecurity_Innovator_of_the_Year-BSides_Bangalore-%23e11d48?style=for-the-badge&logo=academia&logoColor=white" />
</p>

> Selected as a 2025 **RSA Security Scholar**, representing the intersection of AI security, vulnerability research, and offensive red teaming at one of the world's premier security conferences.

---

## 🎯 Status Console

![Status](https://img.shields.io/badge/AI%20Threat%20Ops-ENGAGED-00ffcc?style=for-the-badge&logo=databricks)
![Access Level](https://img.shields.io/badge/Access%20Level-ROOT-ff0055?style=for-the-badge&logo=gnu-bash)
![Location](https://img.shields.io/badge/Origin-Sunnyvale_%2F_Unknown_Node-green?style=flat-square&logo=tor)
![Mode](https://img.shields.io/badge/Mode-Hunt%2FPublish%2FDisclose-purple?style=flat-square&logo=ghost)

---

## 🧩 Expertise

* 🔐 **AI/ML Infrastructure Security** — agentic workflow exploitation, RAG hardening, prompt injection, MCP attack surface, model file deserialization, GPU memory corruption
* 🛠️ **Offensive Security** — adversary emulation, red teaming, fuzzing, symbolic execution, n-day exploit development, kernel research
* 🤖 **Adversarial ML** — jailbreaking, attention-head attacks, safety alignment failures, predictive multiplicity (Rashomon attacks)
* 🧠 **Cryptography** — LLM-driven CTF generation, JWE/JWT bypasses, authenticated encryption pitfalls
* ☁️ **Cloud Security & DevSecOps** — application security reviews, threat modeling, secure SDLC
* 📜 **Standards & Governance** — NIST OLIR, OWASP, ISO/IEC 42001

---

## 🛡️ CVE Portfolio & Vulnerability Research

> Original vulnerability research across the AI/ML stack: orchestration, agents, inference engines, tokenizers, model serializers, and security tooling itself.

### 🔥 Confirmed CVEs

| CVE | Target | Class | Severity | Notes |
|---|---|---|---|---|
| **CVE-2026-33017** | Langflow | Unauthenticated RCE | **Critical 9.3** | 🚨 **CISA KEV** · Exploited in the wild within **20 hours** of disclosure · Federal remediation deadline · GHSA-vwmf-pq79-vjvx |
| **CVE-2026-32628** | AnythingLLM | SQL Injection (Built-in SQL Agent) | **High** | GHSA-jwjx-mw2p-5wc7 · CWE-89 in agentic tool-call surface |

### 🟣 Independent Bug Reports — No CVE, Disclosed Publicly

Valid, technically inarguable findings where the vendor declined to assign a CVE (often through a retroactive documentation shield) but where the underlying issue is real, reproducible, and publicly disclosed.

| Target | Finding | Severity | Status |
|---|---|---|---|
| **XGBoost** (×5) | Heap OOB in tree node access · UBJSON parser memory corruption · Parallel tree double-free · Unsafe `pickle.loads()` on network data (CWE-502) · Hardcoded `0xff99` magic number as Rabit tracker auth (CWE-798) | Critical / High | Vendor declined ("performance + resourcing"). Full technical writeup published on [Medium](https://medium.com/@aviral23) and LinkedIn. |
| **Google `sentencepiece`** | Off-by-4 bounds check in `DecodePrecompiledCharsMap` enabling OOB read via crafted `.model` files (UBSan-confirmed) | Medium | Google VRP Report #498463886 · sentencepiece is the tokenizer backbone of Gemma, T5, and PaLM |
| **Google `sentencepiece`** | Unvalidated trie values used as piece array indices (heap OOB read, release builds) | High | Google VRP Report #498465599 · Upstream fix landed via [PR #1207](https://github.com/google/sentencepiece/pull/1207) |
| **vLLM** | LoRA adapter SSRF → RCE chain | High | Closed via documentation shield. Public writeup. |

---

## 📜 Standards Body Contributions

| Body | Contribution | Detail |
|---|---|---|
| **NIST** | OLIR Catalog Mapping (Live) | First AI security framework mapping in the NIST Online Informative References catalog: OWASP LLM Top 10 v2.0 → NIST CSF 2.0, **169 relationship entries** covering 77 of 106 CSF subcategories. Listed Point of Contact on the NIST CSRC website. |

---

## 🎤 Invited Talks

> Full speaker profile: [sessionize.com/aviral-srivastava](https://sessionize.com/aviral-srivastava/)

| Conference | Year | Talk |
|---|---|---|
| **RSAC 2026** | 2026 | *From Prompt to Pager: Preparing for AI-Native Incidents Now* |
| **ISACA North America 2026** | 2026 | *Breaking the Loop: Offensive Testing of RL and Agentic AI Systems* |
| **CactusCon 14** | 2025 | *Agents Under Siege: Live Attacks from RAG to Tool Calls* |
| **CypherCon 2025** | 2025 | *Deceiving the Deceivers: Offensive Security Strategies for Adversarial AI Attacks* |
| **BSidesSLC 2025** | 2025 | *Filling Gaps in AI Governance: How ISO/IEC 42001 Shapes the Future of AI Risk and Compliance* |
| **BSidesTC 2025** | 2025 | *ROP Alchemy: Universal Gadgets via Type Confusion* |
| **CactusCon 13** | 2025 | *Weaponizing AI: Adversarial Attacks, Hallucinations, and the Offensive Security Frontier* |
| **HOPE XV** | 2024 | Invited Talk (details under NDA) |
| **BSidesChicago 2024** | 2024 | *Hacking Neural Networks: The Hidden Vulnerabilities of AI Systems* |

---

## 📰 Media Coverage

Coverage of CVE-2026-33017 across major cybersecurity publications. Quoted by name as the discoverer in The Hacker News, Help Net Security, Barrack AI, and Cloud Security Alliance research notes.

* [The Hacker News](https://thehackernews.com/) — *Critical Langflow Flaw CVE-2026-33017 Triggers Attacks within 20 Hours of Disclosure*
* [Help Net Security](https://www.helpnetsecurity.com/) — *CISA sounds alarm on Langflow RCE after rapid exploitation*
* [Infosecurity Magazine](https://www.infosecurity-magazine.com/) — *Hackers Exploit Critical Langflow Bug in Just 20 Hours*
* [Sysdig Threat Research](https://www.sysdig.com/) — *CVE-2026-33017: How attackers compromised Langflow AI pipelines in 20 hours*
* [Cloud Security Alliance](https://labs.cloudsecurityalliance.org/) — Research Notes (×2) on the Langflow RCE
* [Qualys ThreatProtect](https://threatprotect.qualys.com/) — *CISA Added Langflow Vulnerability to KEV Catalog*
* [Barrack AI](https://blog.barrack.ai/) — *Langflow Got Hacked Twice Through the Same exec() Call*
* [InfoSec Today](https://www.infosectoday.io/) — *Critical Langflow Flaw Triggers Attacks within 20 Hours*
* [HackerNoon](https://hackernoon.com/u/aviralxroot) — *CVE-2026-33017: Unauthenticated RCE in Langflow's Public Flow Endpoint Explained*
* [CiberSafety](https://cibersafety.com/) — *CVE-2026-33017 in Langflow: Critical vulnerability for RCE without authentication*

---

## 🚀 Projects & Tools

* 🎯 **ZeroDayForge** — Full-spectrum adversary emulation and exploit automation framework
* 🧨 **Autonomous n-day Linux Kernel Exploit Pipeline** — Mac M1 toolchain (radare2, lldb, Ghidra headless) running RECON → AUTO-PICK → 12-POINT SAFETY GATE → PATCH ANALYSIS → ROOT CAUSE → EXPLOIT STRATEGY → COMPILE VERIFY, producing Exploit-DB-format `exploit.c` artifacts
* 🛡️ **Multi-Agent CVE Hunting Pipeline** — Claude Code agent team (Recon · Auditor · Exploiter · Reporter) governed by a 14-rule submission framework and a 4-gate filter (unauthenticated · default config · no doc shield · core feature)
* 🧪 **LLM-Driven Cryptographic CTF Generator** — Automated cryptographic challenge generation system (MS Thesis, Penn State)

---

## 💼 Experience

* 🔐 **Security Engineer (L4) — Amazon Ads Security**, Sunnyvale, CA (2025 – Present)
  AppSec reviews, threat modeling, penetration testing, AI/ML security, agentic workflows, prompt injection, RAG hardening
* 🧪 **Security Internships (6×)** — Malware reverse engineering, secure DevOps, GRC
* 🧑‍🏫 **Teaching Assistant — Red Teaming, CTFs, Penn State** — Led offensive security labs and workshops

---

## 🎓 Education

* 🎓 **MS in Cybersecurity Analytics & Operations — The Pennsylvania State University**
  GPA: 4.0 · Research Assistant · RSA Security Scholar
  Thesis: *AI-Generated Cryptographic CTF Challenges*
* 🎓 **BTech in Computer Science — Amity University**
  Focus: Cryptography, Secure Systems, Network Security

---

## 🏆 Awards & Recognition

* 🥇 **RSA Security Scholar 2025**
* 🏅 **Cybersecurity Innovator of the Year** — BSides Bangalore 2023
* 📜 **ISSN Best International Research Award**
* 🌟 **Young Researcher Award**
* 🎙️ Speaker: **RSAC**, **ISACA North America**, **HOPE XV**, **CypherCon**, **CactusCon (×2)**, **BSides (×3)**
* 🌍 **HackTheBox PRO HACKER** — Top 200 Global · 🇺🇸 Rank #24
  ![HTB Badge](https://www.hackthebox.com/badge/image/212766) · [HTB Profile](https://app.hackthebox.com/profile/212766)

---

## 🌐 Connect

<p align="left">
  <a href="https://www.linkedin.com/in/aviralsrivastava23/"><img src="https://img.shields.io/badge/LinkedIn-aviralsrivastava23-%230A66C2?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
  <a href="https://medium.com/@aviral23"><img src="https://img.shields.io/badge/Medium-@aviral23-%23000000?style=for-the-badge&logo=medium&logoColor=white" /></a>
  <a href="https://hackernoon.com/u/aviralxroot"><img src="https://img.shields.io/badge/HackerNoon-aviralxroot-%2300FF00?style=for-the-badge&logo=hackernoon&logoColor=black" /></a>
  <a href="https://sessionize.com/aviral-srivastava/"><img src="https://img.shields.io/badge/Sessionize-Speaker-%231AB7EA?style=for-the-badge&logo=sessionize&logoColor=white" /></a>
  <a href="https://app.hackthebox.com/profile/212766"><img src="https://img.shields.io/badge/HackTheBox-Top_200_Global-%239FEF00?style=for-the-badge&logo=hackthebox&logoColor=black" /></a>
</p>

---

## 📊 GitHub Stats

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=Aviral2642&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0d1117&title_color=00ffff&icon_color=ff007f&text_color=ffffff" height="170" />
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=Aviral2642&theme=tokyonight&hide_border=true&background=0d1117&ring=00ffff&fire=ff007f&currStreakLabel=00ffff" height="170" />
</p>

---

> 💬 _"The more they secure, the more we exploit. The future belongs to offensive AI."_

![Footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24,30&height=120&section=footer&animation=twinkling)
