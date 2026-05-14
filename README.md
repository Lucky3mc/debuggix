
# 🛡️ Debuggix — 9 Security Engines. 60 Seconds. Not AI only but Guided with 9 Trusted Security Tools.

<p align="center">
  <a href="https://debuggix.space">
    <img src="https://debuggix.space/debuggix-favicon.png" alt="Debuggix Logo" width="320" />
  </a>
</p>

<p align="center">
  <b>One scan. Nine engines. Zero noise.</b><br>
  Debuggix orchestrates Semgrep, Gitleaks, Trivy, Bandit, TruffleHog, ESLint, Hadolint, Checkov, and OSV-Scanner in parallel — then uses AI to filter out false positives and generate working fixes.
</p>

<p align="center">
  <a href="https://debuggix.space"><strong>🔍 Scan Your First Repo Free →</strong></a>
  &nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="https://debuggix.space/verified"><strong>🏆 See Verified Repos →</strong></a>
</p>

---

## ⚡ Why Developers Choose Debuggix

| 😤 The Old Way | ✅ The Debuggix Way |
|---------------|---------------------|
| Run 1 scanner, miss 40% of vulns | 9 engines run simultaneously — catch what others miss |
| 500 findings, 300 are false positives | AI correlates results across engines, eliminates duplicates |
| Spend hours Googling fixes | AI generates working patches with explanations |
| "Trust me bro" security | Public verification badge anyone can click to verify |
| $98/dev/month (Snyk) | Free tier with all 9 engines, no credit card |

---

## 🚨 The State of App Security in 2026


44% of attacks on public-facing apps require ZERO authentication.
67% of security fixes take over 4 hours manually.


**Recent breaches that could have been caught by multi-engine scanning:**

| Incident | What Happened | Would Debuggix Catch It? |
|----------|---------------|--------------------------|
| **Vercel OAuth Breach** | Third-party AI tool token compromised | ✅ TruffleHog + Gitleaks detect leaked tokens |
| **cPanel Backdoor Attack** | Auth bypass exploited on thousands of servers | ✅ Semgrep + Checkov flag auth misconfigurations |
| **Canvas Platform Lockout** | 8,000+ schools locked out via SaaS attack vector | ✅ Trivy + OSV-Scanner catch dependency CVEs |
| **Candy Crush/Tinder Data Leak** | Terabytes of user data exposed via data broker | ✅ All engines scan supply chain for data exposure risks |

*Sources: Cycode, Vercel Security Bulletin, The Hacker News, IBM Security Advisory*

---

## 🛠️ The 9 Engines Running in Every Scan

| Engine | What It Scans | Finds |
|--------|--------------|-------|
| **Semgrep** | Source code patterns | SQL injection, XSS, path traversal, deserialization bugs |
| **Gitleaks** | Current codebase | Hardcoded API keys, passwords, tokens, credentials |
| **TruffleHog** | Full git history | Secrets buried in old commits (verified against live APIs) |
| **Trivy** | Dependencies + containers | Known CVEs, vulnerable packages, malware in deps |
| **Bandit** | Python-specific | Hardcoded passwords, unsafe yaml, shell injection |
| **ESLint** | JavaScript/TypeScript | eval() usage, dangerouslySetInnerHTML, unsafe regex |
| **Hadolint** | Dockerfiles | Running as root, unpinned versions, missing .dockerignore |
| **Checkov** | Infrastructure-as-Code | Open S3 buckets, Terraform/K8s misconfigurations |
| **OSV-Scanner** | Open source vulns | Dependency vulnerabilities from Google's OSV database |

<p align="center"><b>All 9 run in parallel. Results in ~60 seconds.</b></p>

---

## 🔥 How AI Makes This Different

### 1. Noise Filtering
- Deduplicates findings across all 9 engines
- Reads your README and CONTRIBUTING docs to identify intentional patterns
- Auto-skips test files, vendor dirs, node_modules
- Assigns confidence scores (0-100%) to every finding
- Categories: **Confirmed Issues** | **Might Be Intentional** | **False Positives**

### 2. AI Fix Generation (Pro)

Vulnerability found → AI analyzes surrounding code → generates patch → you review → merge

Each fix includes: diff view, plain-English explanation, confidence score, and impact assessment.

### 3. Security Copilot (Pro+)
Ask questions about your codebase in plain English:
> *"Show me all hardcoded credentials"*
> *"What dependencies have critical CVEs?"*
> *"Explain the authentication flow"*

The Copilot reads your actual source files and references real scan findings.



## 🏆 Public Verification — Your Security Badge

When your repo passes all 9 engines with zero critical/high issues, you get a **verified badge**:

<p align="center">
  <a href="https://debuggix.space/verified">
    <img src="https://img.shields.io/badge/VERIFIED%20by%20Debuggix-9%20ENGINES-7928CA?style=for-the-badge&logo=shield&logoColor=white&labelColor=0D1117" alt="Verified by Debuggix - 9 Engines" />
  </a>
</p>

**Add this to your README:**
```markdown
[![Verified by Debuggix](https://ai-debugger-backend-eah5.onrender.com/scan/v1/badge/YOUR_SCAN_ID)](https://debuggix.space/verified)
```

**Or add this to your landing page HTML:**
```html
<a href="https://debuggix.space/verified">
  <img src="https://ai-debugger-backend-eah5.onrender.com/scan/v1/badge/YOUR_SCAN_ID" alt="Verified by Debuggix" />
</a>
```

- ✅ Add it to your README, landing page, or app store listing
- ✅ Changes color automatically when you re-scan (green = A+ clean, orange = warnings, red = critical)
- ✅ Anyone can click to verify your security status
- ✅ **No code is ever exposed** on the public page

---

## 📊 Dashboard Features


✅ Color-coded severity borders (critical = red left border, high = orange, etc.)
✅ Full-text search across all findings
✅ Filter by severity, category, engine
✅ Expand/collapse individual findings or all at once
✅ Close/reopen issues as fixed
✅ One-click "Close All" for confirmed issues
✅ Export full scan report as JSON
✅ Share scan with team members
✅ Comment on individual findings




## 💰 Pricing

| | Free | Pro | Pro+ |
|---|------|-----|------|
| **Price** | $0 forever | $29/mo | $50/mo |
| **Scans/month** | 10 public | 100 private | 500 private |
| **All 9 engines** | ✅ | ✅ | ✅ |
| **AI fixes** | ❌ | ✅ | ✅ |
| **GitHub PR creation** | ❌ | ✅ | ✅ |
| **Security Copilot** | ❌ | ❌ | ✅ |
| **API access** | ❌ | ❌ | ✅ |
| **Slack + Webhooks** | ❌ | ❌ | ✅ |
| **Team seats** | 1 | 3 | 10 |

<p align="center"><a href="https://debuggix.space/register"><strong>Start Free — No Credit Card →</strong></a></p>

---

## 🔒 Your Code Stays Yours

- **Zero retention** — Source code deleted immediately after scanning
- **No AI training** — We never train models on your code
- **TLS 1.3 + AES-256** — All data encrypted in transit and at rest
- **Open-source engines** — All 9 scanners are independently auditable
- **Export/delete anytime** — Your data, your control

---

## 🗺️ What's Coming

- [x] 9-engine orchestration
- [x] AI fix generation
- [x] Public verification badges
- [x] GitHub PR integration
- [x] Team collaboration
- [ ] VS Code extension (coming soon)
- [ ] GitHub Actions CI/CD integration
- [ ] Self-hosted enterprise edition

---

## ⚡ Tech Stack

| Layer | Tech |
|-------|------|
| Backend | FastAPI + Celery + Redis |
| Frontend | React + TypeScript + TailwindCSS |
| Database | PostgreSQL |
| AI | Gemini, DeepSeek, OpenAI, OpenRouter (auto-fallback) |
| Hosting | Render + DigitalOcean |

---

## ⭐ Built solo. No VC. No Data Selling.

Debuggix is built by a developer who believes security should be fast, affordable, and accessible to everyone — not just enterprises with six-figure budgets.

- 🐛 **Found a bug?** [Open an issue](https://github.com/Lucky3mc/debuggix/issues)
- 📧 **Contact:** [luckydiety@gmail.com](mailto:luckydiety@gmail.com)
- 🌐 **Website:** [debuggix.space](https://debuggix.space)

---

<p align="center">
  <b>9 engines. 60 seconds. Your code, secured.</b><br>
  <a href="https://debuggix.space"><strong>🚀 Scan Free Now →</strong></a>
</p>
```
