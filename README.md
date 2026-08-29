<div align="center">
  <img src="https://raw.githubusercontent.com/Aviral2642/Aviral2642/main/assets/hero.svg?v=3" alt="Aviral Srivastava" width="100%" />
</div>

<div align="center">
  <a href="https://pwnies.com/"><img src="https://img.shields.io/badge/PWNIE_AWARDS_2026-NOMINEE-f5b942?style=for-the-badge&logo=awesomelists&logoColor=f5b942&labelColor=0b0f1a" alt="Pwnie Awards 2026 Nominee" /></a>
  <a href="https://www.linkedin.com/in/aviralsrivastava23/"><img src="https://img.shields.io/badge/LINKEDIN-0b0f1a?style=for-the-badge&logo=linkedin&logoColor=00F0FF&labelColor=0b0f1a" alt="LinkedIn" /></a>
  <a href="https://medium.com/@aviral23"><img src="https://img.shields.io/badge/MEDIUM-0b0f1a?style=for-the-badge&logo=medium&logoColor=FF2D95&labelColor=0b0f1a" alt="Medium" /></a>
  <a href="https://hackernoon.com/u/aviralxroot"><img src="https://img.shields.io/badge/HACKERNOON-0b0f1a?style=for-the-badge&logo=hackernoon&logoColor=39FFB0&labelColor=0b0f1a" alt="HackerNoon" /></a>
  <a href="https://sessionize.com/aviral-srivastava/"><img src="https://img.shields.io/badge/SPEAKER-0b0f1a?style=for-the-badge&logo=sessionize&logoColor=C084FC&labelColor=0b0f1a" alt="Sessionize" /></a>
  <a href="https://app.hackthebox.com/users/212766"><img src="https://img.shields.io/badge/HACKTHEBOX-0b0f1a?style=for-the-badge&logo=hackthebox&logoColor=9FEF00&labelColor=0b0f1a" alt="HackTheBox" /></a>
  <a href="https://nvd.nist.gov/vuln/detail/CVE-2026-33017"><img src="https://img.shields.io/badge/CISA_KEV-0b0f1a?style=for-the-badge&logo=shieldsdotio&logoColor=FF2D55&labelColor=0b0f1a" alt="CISA KEV" /></a>
</div>

<div align="center">
  <img src="https://raw.githubusercontent.com/Aviral2642/Aviral2642/main/assets/pwnie.svg?v=1" alt="Pwnie Awards 2026 — Nominee, Best Server-Side / Cloud Bug" width="100%" />
</div>

<div align="center">

## `◈` PWNIE AWARDS 2026 — NOMINEE

<sub><b>BEST SERVER-SIDE / CLOUD BUG</b> · for <b>CVE-2026-33017</b> · announced at <b>DEF CON 34</b>, Las Vegas</sub>

</div>

> The Pwnies are the closest thing offensive security has to an industry ballot — the bugs your peers thought were the best work of the year. **CVE-2026-33017 was nominated for Best Server-Side / Cloud Bug in 2026.** It didn't take the statue at DEF CON 34. The nomination is the part I keep.

<table>
<tr>
<td width="33%" valign="top">

#### `▸` The bug
An unauthenticated `exec()` sink reachable from Langflow's **public flow endpoint**. No credentials, no chained primitive, no exotic preconditions — one request to a documented route and you are running code on the orchestrator.

</td>
<td width="33%" valign="top">

#### `▸` Why it mattered
Langflow sits *underneath* the AI stack — it holds model credentials, vector-store keys, and tool-call permissions. Compromising the orchestrator compromises everything it orchestrates. **CVSS 9.3 CRITICAL.**

</td>
<td width="34%" valign="top">

#### `▸` What happened next
Added to the **CISA KEV** catalog. Exploited in the wild **within 20 hours** of disclosure. Covered by The Hacker News, Help Net Security, Infosecurity, Sysdig, and Qualys — quoted by name as the discoverer.

</td>
</tr>
</table>

<sub>Writeups: **[Medium](https://medium.com/@aviral23/cve-2026-33017-how-i-found-an-unauthenticated-rce-in-langflow-by-reading-the-code-they-already-dc96cdce5896)** · **[HackerNoon](https://hackernoon.com/u/aviralxroot)** · Advisory **[GHSA-vwmf-pq79-vjvx](https://github.com/langflow-ai/langflow/security/advisories/GHSA-vwmf-pq79-vjvx)** · **[NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-33017)**</sub>

<img src="https://raw.githubusercontent.com/Aviral2642/Aviral2642/main/assets/divider.svg?v=2" width="100%" />

<div align="center">
  <img src="https://raw.githubusercontent.com/Aviral2642/Aviral2642/main/assets/terminal.svg?v=3" alt="root@aviral — whoami" width="100%" />
</div>

<img src="https://raw.githubusercontent.com/Aviral2642/Aviral2642/main/assets/divider.svg?v=2" width="100%" />

<div align="center">
  <img src="https://raw.githubusercontent.com/Aviral2642/Aviral2642/main/assets/threat.svg?v=3" alt="Assigned CVEs" width="100%" />
</div>

### `▓` The 2026 Batch — Breaking Agentic Workflow Platforms

> Four CVEs across two orchestrators, all landing on the same seam: the gap between **"we validated this input"** and **"we already ran it."**

| CVE | Target | Finding | Severity | Advisory · Fix |
|---|---|---|---|---|
| **[CVE-2026-69258](https://nvd.nist.gov/vuln/detail/CVE-2026-69258)** | **Flowise** | Unauthenticated **property injection** — the Prediction API spreads `overrideConfig` into the flow execution context with no allow-list, so an attacker controls internals the flow assumed were server-owned | `8.8 HIGH` <sub>CVSS 4.0</sub><br><sub>CWE-639 · CWE-915</sub> | [GHSA-6vh2-wg4h-4vwj](https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-6vh2-wg4h-4vwj)<br><sub>fixed in `flowise@3.1.3`</sub> |
| **[CVE-2026-73081](https://nvd.nist.gov/vuln/detail/CVE-2026-73081)** | **Activepieces** | **OS command injection** — the worker builds a Code step's on-disk path from the step *name* and hands it to a shell-invoked build command. Shell metacharacters execute during compilation, **before any sandbox exists** | `8.7 HIGH` <sub>CVSS 4.0</sub><br><sub>CWE-78</sub> | [GHSA-3pfv-m69p-5fv5](https://github.com/activepieces/activepieces/security/advisories/GHSA-3pfv-m69p-5fv5)<br><sub>fixed in `0.80.0`</sub> |
| **[CVE-2026-73083](https://nvd.nist.gov/vuln/detail/CVE-2026-73083)** | **Activepieces** | **Sandbox escape** — in `SANDBOX_CODE_ONLY` mode the engine loads the compiled module via `importFresh()` (a `require()` wrapper) *before* the V8 isolate is applied. Top-level code reaches `child_process`, `fs`, and `AP_ENCRYPTION_KEY` | `7.6 HIGH` <sub>CVSS 4.0</sub><br><sub>CWE-693</sub> | [GHSA-gr3h-c2j7-r52g](https://github.com/activepieces/activepieces/security/advisories/GHSA-gr3h-c2j7-r52g)<br><sub>fixed in `0.80.0`</sub> |
| **[CVE-2026-73084](https://nvd.nist.gov/vuln/detail/CVE-2026-73084)** | **Activepieces** | **XSS in the OAuth callback** — `/api/redirect` embeds the attacker-supplied `code` parameter into an inline `<script>` unescaped. Unauthenticated script execution in the app origin against any logged-in victim | `6.1 MEDIUM` <sub>CVSS 3.1</sub><br><sub>CWE-79</sub> | [GHSA-hc39-cm5m-q8g7](https://github.com/activepieces/activepieces/security/advisories/GHSA-hc39-cm5m-q8g7)<br><sub>fixed in `0.83.0`</sub> |

<sub>All four assigned via the **GitHub CNA**. Flowise writeup: **[Flowise patched `overrideConfig`. I found the two places the patch never reached.](https://medium.com/@aviral23/cve-2026-69258-flowise-patched-overrideconfig-i-found-the-two-places-the-patch-never-reached-cb907387cbbe)**</sub>

<table>
<tr>
<td width="42%" align="center">
  <img src="https://raw.githubusercontent.com/Aviral2642/Aviral2642/main/assets/badge.svg?v=3" alt="Operator credential" width="290" />
</td>
<td width="58%" valign="middle">

#### `▸` CVE-2026-53923 — the one I like most

A **32-bit integer truncation** in vLLM's GGUF dequantization kernels. The kernel processes fewer elements than it allocated, so the tail of the output tensor is never written — it just keeps whatever was in GPU memory before.

On a multi-tenant inference server, that residue is **another user's data**.

Nothing crashes. No sanitizer fires. Every individual line of the kernel looks correct, and the types are all perfectly reasonable. It fails silently, which is exactly why it survived from `0.5.5` all the way to `0.23.1rc0`.

`CVSS 5.3` · `CWE-681` + `CWE-200` · [GHSA-5jv2-g5wq-cmr4](https://github.com/vllm-project/vllm/security/advisories/GHSA-5jv2-g5wq-cmr4)

<sub>Writeups: **[Medium](https://medium.com/@aviral23/cve-2026-53923-how-a-32-bit-integer-in-vllm-leaks-one-users-gpu-memory-into-another-s-7f726bf5bb23)** · **[HackerNoon](https://hackernoon.com/the-32-bit-integer-that-leaks-your-neighbors-gpu-memory-a-deep-dive-into-cve-2026-53923-in-vllm)**</sub>

</td>
</tr>
</table>

<img src="https://raw.githubusercontent.com/Aviral2642/Aviral2642/main/assets/divider.svg?v=2" width="100%" />

<div align="center">

## `◈` RANGE TIME — HACK THE BOX

</div>

<!-- HTB:START -->
<div align="center">
  <a href="https://app.hackthebox.com/users/212766"><img src="https://raw.githubusercontent.com/Aviral2642/Aviral2642/main/assets/htb.svg?v=c1f617f9" alt="Hack The Box live telemetry — AviralxRoot" width="100%" /></a>
</div>

<div align="center">

<sub>`◈` <b>LIVE</b> — <a href="https://github.com/Aviral2642/Aviral2642/blob/main/.github/workflows/htb-sync.yml"><code>htb-sync.yml</code></a> re-reads the Hack The Box API every six hours and redraws this card whenever a number moves. Last change <b>2026-08-29 16:42 UTC</b>.</sub>

</div>

> **AviralxRoot** — **Guru** on points, **Prodigy III · level 89** on XP. Global **#64** · **#12** in United States, **1,936** points, **68** user and **50** root flags, **227** challenges, **148** Sherlock tasks, and **6** fortresses cleared end to end. Nothing on this card is typed by hand.
<!-- HTB:END -->

<img src="https://raw.githubusercontent.com/Aviral2642/Aviral2642/main/assets/divider.svg?v=2" width="100%" />

### `▓` Independent Bug Reports — Disclosed Without CVE

> Valid, reproducible findings where the vendor declined assignment (often behind a retroactive documentation shield). Published anyway.

| Target | Finding | Severity | Status |
|---|---|---|---|
| **XGBoost** `×5` | Heap OOB in tree node access · UBJSON parser memory corruption · Parallel tree double-free · Unsafe `pickle.loads()` on network data (CWE-502) · Hardcoded `0xff99` magic as Rabit tracker auth (CWE-798) | `CRITICAL` / `HIGH` | Vendor declined — "performance + resourcing". Full writeup on [Medium](https://medium.com/@aviral23/i-found-5-security-vulnerabilities-in-xgboost-heres-what-happened-189327f97fbf) |
| **Google `sentencepiece`** | Off-by-4 bounds check in `DecodePrecompiledCharsMap` → OOB read via crafted `.model` (UBSan-confirmed) | `MEDIUM` | Google VRP **#498463886** — tokenizer backbone of Gemma, T5, PaLM |
| **Google `sentencepiece`** | Unvalidated trie values used as piece-array indices → heap OOB read in release builds | `HIGH` | Google VRP **#498465599** — upstream fix [PR #1207](https://github.com/google/sentencepiece/pull/1207) |
| **vLLM** | LoRA adapter SSRF → RCE chain | `HIGH` | Closed via documentation shield. Public writeup |

<sub>Separate from the seven assigned CVEs above.</sub>

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
| `2026` | **BSides Las Vegas** | *Rejected-Input Programming: Exploiting Parsers That Say No Too Late* — Breaking Ground, Aug 5 |
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

> Quoted by name as the discoverer across major security press. This is the bug that went on to be nominated for a Pwnie.

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
  <a href="https://pwnies.com/"><img src="https://img.shields.io/badge/PWNIE_AWARDS_2026_NOMINEE-BEST_SERVER--SIDE_%2F_CLOUD_BUG-f5b942?style=for-the-badge&labelColor=0b0f1a" /></a>
  <br/>
  <img src="https://img.shields.io/badge/RSA_SECURITY_SCHOLAR-2025-FF2D95?style=for-the-badge&labelColor=0b0f1a" />
  <img src="https://img.shields.io/badge/CYBERSECURITY_INNOVATOR_OF_THE_YEAR-BSIDES_BLR-C084FC?style=for-the-badge&labelColor=0b0f1a" />
  <img src="https://img.shields.io/badge/ISSN_BEST_INTL_RESEARCH-AWARD-F5B942?style=for-the-badge&labelColor=0b0f1a" />
  <img src="https://img.shields.io/badge/YOUNG_RESEARCHER-AWARD-00F0FF?style=for-the-badge&labelColor=0b0f1a" />
  <br/>
  <br/>
  <a href="https://app.hackthebox.com/users/212766"><img src="https://www.hackthebox.com/badge/image/212766" alt="Hack The Box — AviralxRoot" height="50" /></a>
</div>

<img src="https://raw.githubusercontent.com/Aviral2642/Aviral2642/main/assets/divider.svg?v=2" width="100%" />

<div align="center">
  <img src="https://raw.githubusercontent.com/Aviral2642/Aviral2642/main/assets/footer.svg?v=2" alt="The future belongs to offensive AI" width="100%" />
</div>
