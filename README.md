<div align="center">
  <img src="https://raw.githubusercontent.com/Aviral2642/Aviral2642/main/assets/hero.svg?v=2" alt="Aviral Srivastava" width="100%" />
</div>

<div align="center">
  <a href="https://www.linkedin.com/in/aviralsrivastava23/"><img src="https://img.shields.io/badge/LINKEDIN-0b0f1a?style=for-the-badge&logo=linkedin&logoColor=00F0FF&labelColor=0b0f1a" alt="LinkedIn" /></a>
  <a href="https://medium.com/@aviral23"><img src="https://img.shields.io/badge/MEDIUM-0b0f1a?style=for-the-badge&logo=medium&logoColor=FF2D95&labelColor=0b0f1a" alt="Medium" /></a>
  <a href="https://hackernoon.com/u/aviralxroot"><img src="https://img.shields.io/badge/HACKERNOON-0b0f1a?style=for-the-badge&logo=hackernoon&logoColor=39FFB0&labelColor=0b0f1a" alt="HackerNoon" /></a>
  <a href="https://sessionize.com/aviral-srivastava/"><img src="https://img.shields.io/badge/SPEAKER-0b0f1a?style=for-the-badge&logo=sessionize&logoColor=C084FC&labelColor=0b0f1a" alt="Sessionize" /></a>
  <a href="https://app.hackthebox.com/profile/212766"><img src="https://img.shields.io/badge/HACKTHEBOX-0b0f1a?style=for-the-badge&logo=hackthebox&logoColor=9FEF00&labelColor=0b0f1a" alt="HackTheBox" /></a>
  <a href="https://nvd.nist.gov/vuln/detail/CVE-2026-33017"><img src="https://img.shields.io/badge/CISA_KEV-0b0f1a?style=for-the-badge&logo=shieldsdotio&logoColor=FF2D55&labelColor=0b0f1a" alt="CISA KEV" /></a>
</div>

<img src="https://raw.githubusercontent.com/Aviral2642/Aviral2642/main/assets/divider.svg?v=2" width="100%" />

<div align="center">
  <img src="https://raw.githubusercontent.com/Aviral2642/Aviral2642/main/assets/terminal.svg?v=2" alt="root@aviral — whoami" width="100%" />
</div>

<img src="https://raw.githubusercontent.com/Aviral2642/Aviral2642/main/assets/divider.svg?v=2" width="100%" />

<div align="center">
  <img src="https://raw.githubusercontent.com/Aviral2642/Aviral2642/main/assets/threat.svg?v=2" alt="Assigned CVEs" width="100%" />
</div>

<table>
<tr>
<td width="42%" align="center">
  <img src="https://raw.githubusercontent.com/Aviral2642/Aviral2642/main/assets/badge.svg?v=2" alt="Operator credential" width="290" />
</td>
<td width="58%" valign="middle">

#### `▸` CVE-2026-53923 — the one I like most

A **32-bit integer truncation** in vLLM's GGUF dequantization kernels. The kernel processes fewer elements than it allocated, so the tail of the output tensor is never written — it just keeps whatever was in GPU memory before.

On a multi-tenant inference server, that residue is **another user's data**.

Nothing crashes. No sanitizer fires. Every individual line of the kernel looks correct, and the types are all perfectly reasonable. It fails silently, which is exactly why it survived from `0.5.5` all the way to `0.23.1rc0`.

`CVSS 5.3` · `CWE-681` + `CWE-200`

<sub>Writeups: **[Medium](https://medium.com/@aviral23/cve-2026-53923-how-a-32-bit-integer-in-vllm-leaks-one-users-gpu-memory-into-another-s-7f726bf5bb23)** · **[HackerNoon](https://hackernoon.com/the-32-bit-integer-that-leaks-your-neighbors-gpu-memory-a-deep-dive-into-cve-2026-53923-in-vllm)**</sub>

</td>
</tr>
</table>

### `▓` Independent Bug Reports — Disclosed Without CVE

> Valid, reproducible findings where the vendor declined assignment (often behind a retroactive documentation shield). Published anyway.

| Target | Finding | Severity | Status |
|---|---|---|---|
| **XGBoost** `×5` | Heap OOB in tree node access · UBJSON parser memory corruption · Parallel tree double-free · Unsafe `pickle.loads()` on network data (CWE-502) · Hardcoded `0xff99` magic as Rabit tracker auth (CWE-798) | `CRITICAL` / `HIGH` | Vendor declined — "performance + resourcing". Full writeup on [Medium](https://medium.com/@aviral23) |
| **Google `sentencepiece`** | Off-by-4 bounds check in `DecodePrecompiledCharsMap` → OOB read via crafted `.model` (UBSan-confirmed) | `MEDIUM` | Google VRP **#498463886** — tokenizer backbone of Gemma, T5, PaLM |
| **Google `sentencepiece`** | Unvalidated trie values used as piece-array indices → heap OOB read in release builds | `HIGH` | Google VRP **#498465599** — upstream fix [PR #1207](https://github.com/google/sentencepiece/pull/1207) |
| **vLLM** | LoRA adapter SSRF → RCE chain | `HIGH` | Closed via documentation shield. Public writeup |

<sub>Separate from **CVE-2026-53923** above, which vLLM did assign.</sub>

<img src="https://raw.githubusercontent.com/Aviral2642/Aviral2642/main/assets/divider.svg?v=2" width="100%" />

<div align="center">
  <img src="https://raw.githubusercontent.com/Aviral2642/Aviral2642/main/assets/arsenal.svg?v=2" alt="Capability Matrix" width="100%" />
</div>

<img src="https://raw.githubusercontent.com/Aviral2642/Aviral2642/main/assets/divider.svg?v=2" width="100%" />

<div align="center">

## `◈` STANDARDS BODY CONTRIBUTIONS

</div>

| Body | Contribution | Detail |
|---|---|---|
| **NIST** | OLIR Catalog Mapping — **live** | First AI-security framework mapping in the NIST Online Informative References catalog: **OWASP LLM Top 10 v2.0 → NIST CSF 2.0**, with **169 relationship entries** covering 77 of 106 CSF subcategories. Listed Point of Contact on the NIST CSRC website. |
| **MITRE** | CWE / CAPEC submissions | Weakness submissions in Phase-03 review, derived from CVE-2026-33017 (AI workflow definition injection). |

<div align="center">

## `◈` TRANSMISSIONS — INVITED TALKS

<sub>Full speaker profile → <b><a href="https://sessionize.com/aviral-srivastava/">sessionize.com/aviral-srivastava</a></b></sub>

</div>

| Year | Conference | Talk |
|:---:|---|---|
| `2026` | **RSAC 2026** | *From Prompt to Pager: Preparing for AI-Native Incidents Now* |
| `2026` | **ISACA North America** | *Breaking the Loop: Offensive Testing of RL and Agentic AI Systems* |
| `2025` | **CactusCon 14** | *Agents Under Siege: Live Attacks from RAG to Tool Calls* |
| `2025` | **CypherCon 2025** | *Deceiving the Deceivers: Offensive Security Strategies for Adversarial AI* |
| `2025` | **BSidesSLC** | *Filling Gaps in AI Governance: How ISO/IEC 42001 Shapes AI Risk & Compliance* |
| `2025` | **BSidesTC** | *ROP Alchemy: Universal Gadgets via Type Confusion* |
| `2025` | **CactusCon 13** | *Weaponizing AI: Adversarial Attacks, Hallucinations, and the Offensive Frontier* |
| `2024` | **HOPE XV** | Invited talk — details under NDA |
| `2024` | **BSidesChicago** | *Hacking Neural Networks: The Hidden Vulnerabilities of AI Systems* |

<details>
<summary><b><code>▶</code> SIGNAL INTERCEPT — Press coverage of CVE-2026-33017</b></summary>

<br>

> Quoted by name as the discoverer across major security press.

- **[The Hacker News](https://thehackernews.com/)** — *Critical Langflow Flaw CVE-2026-33017 Triggers Attacks within 20 Hours of Disclosure*
- **[Help Net Security](https://www.helpnetsecurity.com/)** — *CISA sounds alarm on Langflow RCE after rapid exploitation*
- **[Infosecurity Magazine](https://www.infosecurity-magazine.com/)** — *Hackers Exploit Critical Langflow Bug in Just 20 Hours*
- **[Sysdig Threat Research](https://www.sysdig.com/)** — *How attackers compromised Langflow AI pipelines in 20 hours*
- **[Cloud Security Alliance](https://labs.cloudsecurityalliance.org/)** — Research Notes ×2
- **[Qualys ThreatProtect](https://threatprotect.qualys.com/)** — *CISA Added Langflow Vulnerability to KEV Catalog*
- **[Barrack AI](https://blog.barrack.ai/)** — *Langflow Got Hacked Twice Through the Same exec() Call*
- **[HackerNoon](https://hackernoon.com/u/aviralxroot)** — *CVE-2026-33017: Unauthenticated RCE in Langflow's Public Flow Endpoint Explained*
- **[InfoSec Today](https://www.infosectoday.io/)** · **[CiberSafety](https://cibersafety.com/)**

</details>

<img src="https://raw.githubusercontent.com/Aviral2642/Aviral2642/main/assets/divider.svg?v=2" width="100%" />

<div align="center">

## `◈` OPERATIONS — TOOLS & PIPELINES

</div>

<table>
<tr>
<td width="50%" valign="top">

#### `▸` ZeroDayForge
Full-spectrum adversary emulation and exploit automation framework.

</td>
<td width="50%" valign="top">

#### `▸` Autonomous n-day Kernel Exploit Pipeline
Apple-silicon toolchain (radare2 · lldb · Ghidra headless) running
`RECON → AUTO-PICK → 12-POINT SAFETY GATE → PATCH ANALYSIS → ROOT CAUSE → EXPLOIT STRATEGY → COMPILE VERIFY`,
emitting Exploit-DB-format `exploit.c`.

</td>
</tr>
<tr>
<td width="50%" valign="top">

#### `▸` Multi-Agent CVE Hunting Pipeline
Agent team — *Recon · Auditor · Exploiter · Reporter* — governed by a 14-rule submission framework and a 4-gate filter (unauthenticated · default config · no doc shield · core feature).

</td>
<td width="50%" valign="top">

#### `▸` LLM-Driven Cryptographic CTF Generator
Automated cryptographic challenge generation. MS thesis, Penn State.

</td>
</tr>
</table>

<img src="https://raw.githubusercontent.com/Aviral2642/Aviral2642/main/assets/divider.svg?v=2" width="100%" />

<div align="center">

## `◈` DOSSIER

</div>

<table>
<tr>
<td width="50%" valign="top">

### `▸` Experience
**Security Engineer (L4)** — Amazon Ads Security
<sub>Sunnyvale, CA · 2025 – Present</sub>

AppSec reviews · threat modeling · penetration testing · AI/ML security · agentic workflows · prompt injection · RAG hardening

**Security Internships** `×6`
<sub>Malware RE · secure DevOps · GRC</sub>

**Teaching Assistant — Red Teaming & CTFs**
<sub>The Pennsylvania State University</sub>

</td>
<td width="50%" valign="top">

### `▸` Education
**MS, Cybersecurity Analytics & Operations**
<sub>The Pennsylvania State University · GPA 4.0</sub>

<sub>Research Assistant · RSA Security Scholar</sub>
<sub>Thesis: <i>AI-Generated Cryptographic CTF Challenges</i></sub>

**BTech, Computer Science** — Amity University
<sub>Cryptography · Secure Systems · Network Security</sub>

</td>
</tr>
</table>

### `▸` Commendations

<div align="center">
  <img src="https://img.shields.io/badge/RSA_SECURITY_SCHOLAR-2025-FF2D95?style=for-the-badge&labelColor=0b0f1a" />
  <img src="https://img.shields.io/badge/CYBERSECURITY_INNOVATOR_OF_THE_YEAR-BSIDES_BLR-C084FC?style=for-the-badge&labelColor=0b0f1a" />
  <img src="https://img.shields.io/badge/ISSN_BEST_INTL_RESEARCH-AWARD-F5B942?style=for-the-badge&labelColor=0b0f1a" />
  <img src="https://img.shields.io/badge/YOUNG_RESEARCHER-AWARD-00F0FF?style=for-the-badge&labelColor=0b0f1a" />
  <br/>
  <a href="https://app.hackthebox.com/profile/212766"><img src="https://img.shields.io/badge/HACKTHEBOX-PRO_HACKER_·_TOP_200_GLOBAL_·_%2324_US-9FEF00?style=for-the-badge&logo=hackthebox&logoColor=black&labelColor=0b0f1a" /></a>
</div>

<img src="https://raw.githubusercontent.com/Aviral2642/Aviral2642/main/assets/divider.svg?v=2" width="100%" />

<div align="center">
  <img src="https://raw.githubusercontent.com/Aviral2642/Aviral2642/main/assets/footer.svg?v=2" alt="The future belongs to offensive AI" width="100%" />
</div>
