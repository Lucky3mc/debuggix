```markdown
# 🛡️ Debuggix: 9 Security Scanners + AI That Actually Fixes Your Code

<p align="center">
  <b>Detect vulnerabilities. Apply fixes with confidence.</b><br>
  Debuggix runs 9 security engines against your codebase, correlates results to eliminate noise, and generates verified patches you can review before merging.
</p>

<p align="center">
  <a href="https://debuggix.space"><strong>🚀 Start Free — No Credit Card →</strong></a>
</p>

---

## 📖 Table of Contents

- [Overview](#-overview)
- [How It Works](#-how-it-works)
- [The 9 Security Engines](#-the-9-security-engines)
- [Features](#-features)
- [Architecture](#-architecture)
- [API Reference](#-api-reference)
- [Webhooks](#-webhooks)
- [Slack Integration](#-slack-integration)
- [Pricing](#-pricing)
- [Privacy & Security](#-privacy--security)
- [Roadmap](#-roadmap)
- [Tech Stack](#-tech-stack)

---

## 🔍 Overview

Debuggix is a security platform that finds vulnerabilities in your code AND generates working fixes — not just a list of problems. It orchestrates 9 open-source security scanners in parallel, correlates their results to eliminate duplicates and false positives, then uses AI to generate production-ready code patches.

**Why Debuggix?** Traditional security tools dump a list of 500 vulnerabilities and say "good luck." You spend hours manually fixing each one. 67% of security fixes take over 4 hours. Debuggix both finds AND fixes, turning hours of manual patching into a 60-second review.

---

## ⚙️ How It Works

1. **Connect** — Paste any GitHub repository URL or upload a ZIP file
2. **Scan** — 9 specialized engines run in parallel across your codebase
3. **Review** — View findings with confidence scores, source attribution, and AI explanations
4. **Fix** — AI generates working code patches with diffs. Review, copy, or merge.

---

## 🛠️ The 9 Security Engines

| Engine | Category | What It Detects | Coverage |
|--------|----------|----------------|----------|
| **Semgrep** | Static Analysis | SQL injection, XSS, path traversal, code vulnerabilities | Python, JS, Go, Java, Ruby, PHP, Terraform |
| **Gitleaks** | Secret Detection | Hardcoded API keys, tokens, passwords, credentials | All file types |
| **TruffleHog** | Secret Detection | Secrets buried in git commit history | Git history |
| **Trivy** | Dependency Scanning | Known CVEs in packages and container images | pip, npm, Docker, apt, yum, gem |
| **Bandit** | Static Analysis | Python-specific security issues | Python |
| **ESLint** | Static Analysis | JavaScript/TypeScript security linting | .js, .ts, .jsx, .tsx |
| **Hadolint** | Configuration | Dockerfile misconfigurations and best practices | Dockerfiles |
| **Checkov** | Configuration | Infrastructure-as-Code misconfigurations | Terraform, K8s, CloudFormation, Helm |
| **OSV-Scanner** | Dependency Scanning | Open source vulnerability database | 10+ ecosystems |

All engines run in parallel. Results are merged, deduplicated, and AI-verified.

---

## 🔥 Features

### AI-Powered Fix Generation
For every vulnerability, Debuggix generates a working code fix using multiple LLM providers (Google Gemini, DeepSeek, OpenAI, OpenRouter) with automatic fallback. Each fix includes:
- **Diff view** — See exactly what changed
- **Explanation** — Understand why the fix works
- **Confidence score** — Know how reliable the fix is
- **Impact assessment** — Understand the severity of the issue

### Security Copilot (Pro+)
An AI chat interface that understands your entire codebase. Ask questions like:
- "Where are the most critical vulnerabilities?"
- "Explain the authentication flow"
- "Show me all hardcoded credentials"
- "What dependency issues exist?"

The Copilot reads your actual source files and references scan findings. Responses include file paths, line numbers, and code snippets. Context is cached for faster follow-up questions. A flush button lets you clear cached context at any time.

### Confidence Scoring & False Positive Control
Every finding receives an AI confidence score (0-100%). Higher scores mean higher likelihood of being a real vulnerability. Mark findings as confirmed or false positive to filter results.

### GitHub Integration
- **OAuth Login** — Sign up with your GitHub account
- **Private Repos** — Scan private repositories using your GitHub token
- **One-Click PR** — Create a Pull Request with all AI-generated fixes applied
- **github.dev & Codespaces** — Open files directly in browser-based editors

### Public Reports & Badges
- **Shareable Reports** — Generate a public URL with no code exposed
- **README Badge** — Add a security status badge to your repository:
```markdown
[![Security](https://ai-debugger-backend-eah5.onrender.com/api/v1/scan/badge/{username}/{repo})](https://debuggix.space)
```

### Team Collaboration
- **Shared Scans** — Share scan results with team members
- **Comments** — Discuss individual findings
- **Custom Rules** — Add custom Semgrep detection rules (Pro+)

---

## 🏗️ Architecture

### System Design

```
Users → Frontend (React, Render)
          ↓
     Backend API (FastAPI, Render)
          ↓
     Redis (Upstash) → Celery Worker (DigitalOcean Droplet)
                            ↓
                    9 Security Engines (Semgrep, Gitleaks, Trivy, etc.)
                            ↓
                    AI Fix Generation (Multi-LLM with fallback)
                            ↓
                    PostgreSQL (Render)
```

### Scan Pipeline
1. User submits a GitHub URL or ZIP file
2. Backend creates a scan record and dispatches a Celery task via Redis
3. Celery worker clones the repository with `--depth 1 --single-branch` for speed
4. 9 security engines run in parallel with configurable timeouts
5. Vendor directories, test files, and node_modules are excluded automatically
6. Results are merged, deduplicated, and scored
7. AI noise filtering removes false positives and low-confidence findings
8. Findings are saved to PostgreSQL with metadata
9. Source code is immediately deleted from the worker
10. User views results with confidence scores and AI-generated fixes

### AI Provider Fallback
```
Request → Google Gemini (free, 1000/day)
       ↓ fails
       → DeepSeek ($0.14/1M tokens)
       ↓ fails  
       → OpenAI
       ↓ fails
       → OpenRouter (free models as backup)
```

### Performance Optimizations
- Vendor directories, test files, and cache directories are excluded
- Files larger than 500KB are skipped
- Git clone uses `--depth 1 --single-branch`
- Celery workers run with configurable concurrency
- Trivy database is cached on the worker
- AI chat context is cached per scan session (1-hour TTL)

---

## 📡 API Reference

### Base URL
```
https://ai-debugger-backend-eah5.onrender.com
```

### Authentication
All API requests require a JWT token:
```
Authorization: Bearer <your_jwt_token>
```
Obtain a token via the login endpoint.

### Rate Limits
- Free tier: 10 requests/minute
- Pro tier: 60 requests/minute
- Pro+ tier: 120 requests/minute

---

### Authentication Endpoints

**Register**
```http
POST /api/v1/auth/register
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "secure_password",
  "name": "Your Name",
  "plan": "free"
}
```

**Login**
```http
POST /api/v1/auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "secure_password"
}

Response: { "access_token": "jwt...", "token_type": "bearer", "user": {...} }
```

**GitHub OAuth Login**
```http
GET /api/v1/auth/github/login
→ Redirects to GitHub for authentication
→ Returns JWT token after callback
```

**Logout**
```http
POST /api/v1/auth/logout
Authorization: Bearer <token>
```

---

### Scan Endpoints

**Trigger a GitHub Scan**
```http
POST /api/v1/scan/github
Authorization: Bearer <token>
Content-Type: application/json

{
  "repo_url": "https://github.com/user/repo",
  "name": "Optional scan name"
}

Response: { "id": "scan-uuid", "name": "repo", "status": "pending" }
```

**Trigger a ZIP Upload Scan**
```http
POST /api/v1/scan/zip
Authorization: Bearer <token>
Content-Type: multipart/form-data

file: your_code.zip
name: Optional name

Response: { "id": "scan-uuid", "name": "filename", "status": "pending" }
```

**List All Scans**
```http
GET /api/v1/scan/?page=1&limit=50
Authorization: Bearer <token>

Response: {
  "scans": [
    {
      "id": "uuid",
      "name": "my-repo",
      "repo_url": "https://github.com/user/repo",
      "status": "completed",
      "findings_count": 15,
      "critical_count": 2,
      "high_count": 5,
      "created_at": "2026-04-30T12:00:00Z",
      "completed_at": "2026-04-30T12:01:15Z"
    }
  ],
  "total": 42,
  "page": 1,
  "total_pages": 1
}
```

**Get Scan Results**
```http
GET /api/v1/scan/{scan_id}
Authorization: Bearer <token>

Response: {
  "scan": {
    "id": "uuid",
    "name": "my-repo",
    "repo_url": "https://github.com/user/repo",
    "status": "completed",
    "findings_count": 15,
    "critical_count": 2,
    "high_count": 5,
    "medium_count": 6,
    "low_count": 2
  },
  "findings": [
    {
      "id": "finding-id",
      "tool": "semgrep",
      "severity": "critical",
      "file_path": "src/auth.js",
      "line_number": 42,
      "message": "SQL injection vulnerability detected",
      "code_snippet": "query = 'SELECT * FROM users WHERE id=' + userId",
      "ai_confidence": 92,
      "ai_fix": {
        "fixed_code": "query = 'SELECT * FROM users WHERE id=?'",
        "explanation": "Use parameterized queries to prevent SQL injection"
      }
    }
  ],
  "summary": {
    "total": 15,
    "critical": 2,
    "high": 5,
    "medium": 6,
    "low": 2
  }
}
```

**Delete a Scan**
```http
DELETE /api/v1/scan/{scan_id}
Authorization: Bearer <token>

Response: { "message": "Scan deleted" }
```

**Create Fix Pull Request**
```http
POST /api/v1/scan/{scan_id}/create-fix-pr
Authorization: Bearer <token>

Response: {
  "success": true,
  "pr_url": "https://github.com/user/repo/pull/42",
  "message": "Fix PR created successfully"
}
```

---

### Public Endpoints (No Authentication)

**Public Scan Report**
```http
GET /api/v1/scan/public/{scan_id}

Response: {
  "scan": {
    "id": "abc12345",
    "name": "my-repo",
    "repo_url": "https://github.com/user/repo",
    "scanned_at": "2026-04-30T12:00:00Z",
    "duration_seconds": 75.3,
    "lines_scanned": 15000
  },
  "summary": {
    "total": 15,
    "by_severity": { "critical": 2, "high": 5, "medium": 6, "low": 2 },
    "risk_level": "HIGH"
  },
  "findings": [...],  // No code snippets exposed
  "engines_used": ["Semgrep", "Gitleaks", "Trivy", "Bandit", "ESLint", "Hadolint", "Checkov", "OSV-Scanner", "TruffleHog"]
}
```

**Security Badge**
```http
GET /api/v1/scan/badge/{username}/{repo}

Response: SVG badge image showing security status
Statuses: "secure", "X critical", "X high", "not scanned"
```

---

### AI Endpoints

**Generate AI Fix for a Finding**
```http
POST /api/v1/ai/fix
Authorization: Bearer <token>
Content-Type: application/json

{
  "code_snippet": "query = 'SELECT * FROM users WHERE id=' + userId",
  "error_message": "SQL injection detected",
  "language": "javascript",
  "file_path": "/src/auth.js"
}

Response: {
  "success": true,
  "fixed_code": "query = 'SELECT * FROM users WHERE id=?'",
  "explanation": "Parameterized queries prevent SQL injection by separating SQL logic from data.",
  "model": "gemini-2.0-flash",
  "provider": "gemini"
}
```

**Explain Code**
```http
POST /api/v1/ai/explain
Authorization: Bearer <token>
Content-Type: application/json

{
  "code_snippet": "const result = await db.query('SELECT * FROM users');",
  "question": "Is this query safe?",
  "language": "javascript"
}

Response: { "success": true, "explanation": "This query is safe because..." }
```

**Code Review**
```http
POST /api/v1/ai/review
Authorization: Bearer <token>
Content-Type: application/json

{
  "code_snippet": "function processUser(input) { eval(input); }",
  "language": "javascript"
}

Response: { "success": true, "issues": [{ "severity": "critical", "message": "eval() is dangerous..." }] }
```

**Improve Code**
```http
POST /api/v1/ai/improve
Authorization: Bearer <token>
Content-Type: application/json

{
  "code_snippet": "for (let i = 0; i < arr.length; i++) { console.log(arr[i]); }",
  "language": "javascript"
}

Response: { "success": true, "improved_code": "arr.forEach(item => console.log(item));", "changes": ["..." ] }
```

**Security Copilot (Streaming)**
```http
POST /api/v1/ai/copilot/stream
Authorization: Bearer <token>
Content-Type: application/json

{
  "scan_id": "scan-uuid",
  "question": "Where are all the SQL queries in this codebase?",
  "chat_history": []
}

Response: Server-Sent Events stream
Events: status, progress, finding, complete
```

**Flush Copilot Cache**
```http
POST /api/v1/ai/copilot/cache/flush
Authorization: Bearer <token>
Content-Type: application/json

{ "scan_id": "scan-uuid" }

Response: { "message": "Chat context flushed. Next query will re-analyze the codebase." }
```

**AI Service Status**
```http
GET /api/v1/ai/status
Authorization: Bearer <token>

Response: {
  "available": true,
  "provider": "gemini",
  "model": "gemini-2.0-flash",
  "user_has_access": true,
  "user_tier": "pro_plus",
  "copilot_enabled": true
}
```

---

## 🔔 Webhooks

Webhooks allow you to receive real-time notifications about scan events. Configure them in your Dashboard → Settings → Webhooks.

### Available Events

| Event | Trigger | Payload |
|-------|---------|---------|
| `scan.started` | A scan begins processing | `scan_id`, `repo_url`, `timestamp` |
| `scan.completed` | A scan finishes successfully | `scan_id`, `findings_count`, `critical_count`, `high_count`, `timestamp` |
| `scan.failed` | A scan encounters an error | `scan_id`, `error_message`, `timestamp` |
| `finding.critical` | A critical vulnerability is found | `scan_id`, `finding_id`, `severity`, `message`, `file_path` |
| `finding.high` | A high-severity vulnerability is found | `scan_id`, `finding_id`, `severity`, `message`, `file_path` |

### Configure Webhooks

**Generate a Webhook URL**
```http
POST /api/v1/integrations/webhooks/generate
Authorization: Bearer <token>
Content-Type: application/json

{
  "events": ["scan.completed", "finding.critical", "finding.high"]
}

Response: {
  "webhook_url": "https://ai-debugger-backend-eah5.onrender.com/api/v1/webhooks/receive/abc12345",
  "secret": "generated_secret_key_here",
  "events": ["scan.completed", "finding.critical", "finding.high"],
  "message": "Webhook generated. Copy your secret now - it won't be shown again!"
}
```

**Update Webhook Events**
```http
PUT /api/v1/integrations/webhooks/events
Authorization: Bearer <token>
Content-Type: application/json

{
  "events": ["scan.started", "scan.completed", "scan.failed"]
}

Response: { "events": [...], "message": "Webhook events updated" }
```

**Test Webhook**
```http
POST /api/v1/integrations/webhooks/test
Authorization: Bearer <token>

Response: { "message": "Test webhook sent successfully" }
```

**Revoke Webhook**
```http
DELETE /api/v1/integrations/webhooks/revoke
Authorization: Bearer <token>

Response: { "message": "Webhook revoked" }
```

**Get Webhook Status**
```http
GET /api/v1/integrations/webhooks
Authorization: Bearer <token>

Response: {
  "url": "https://ai-debugger-backend-eah5.onrender.com/api/v1/webhooks/receive/abc12345",
  "secret": "***hidden***",
  "events": ["scan.completed", "finding.critical"]
}
```

### Webhook Payload Example

When a scan completes, your endpoint receives:
```json
{
  "event": "scan.completed",
  "scan_id": "c6c1c371-9d26-4010-9867-e9a63114203a",
  "scan_name": "my-repo",
  "repo_url": "https://github.com/user/repo",
  "findings_count": 15,
  "critical_count": 2,
  "high_count": 5,
  "medium_count": 6,
  "low_count": 2,
  "timestamp": "2026-04-30T12:01:15Z"
}
```

### Verifying Webhook Signatures

Each webhook request includes an `X-Debuggix-Signature` header. Verify it using your webhook secret:

```python
import hmac
import hashlib

def verify_webhook(payload: bytes, signature: str, secret: str) -> bool:
    expected = hmac.new(
        secret.encode(),
        payload,
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(expected, signature)
```

```javascript
const crypto = require('crypto');

function verifyWebhook(payload, signature, secret) {
  const expected = crypto
    .createHmac('sha256', secret)
    .update(payload)
    .digest('hex');
  return crypto.timingSafeEqual(
    Buffer.from(expected),
    Buffer.from(signature)
  );
}
```

---

## 💬 Slack Integration

Send scan notifications directly to a Slack channel. Requires Pro+ plan.

**Connect Slack**
```http
GET /api/v1/integrations/slack/auth
Authorization: Bearer <token>
→ Redirects to Slack OAuth
→ Saves webhook URL after authorization
```

**Disconnect Slack**
```http
POST /api/v1/integrations/slack/disconnect
Authorization: Bearer <token>

Response: { "message": "Slack disconnected" }
```

**Send Test Notification**
```http
POST /api/v1/integrations/slack/test
Authorization: Bearer <token>

Response: { "message": "Test notification sent" }
```

---

## 💰 Pricing

| Plan | Price | Scans | Key Features |
|------|-------|-------|-------------|
| **Free** | $0 forever | 10 public scans/month | All 9 engines, basic detection, community support |
| **Pro** | $29/month | 100 private scans/month | AI-powered fixes, GitHub PR integration, email support |
| **Pro+** | $50/month | 500 private scans/month | Security Copilot, API access, 3 team seats, Slack integration, webhooks, custom rules |

All plans include a free trial. No credit card required for the free tier.

[Start Free →](https://debuggix.space/register)

---

## 🔒 Privacy & Security

- **Zero retention:** Your source code is processed and immediately deleted after scanning
- **No training on your code:** We never use your code to train AI models
- **End-to-end encryption:** All data encrypted in transit (TLS 1.3) and at rest (AES-256)
- **Open-source engines:** All 9 scanners are open-source and independently auditable
- **Your data is yours:** Export or delete your data at any time

---

## 🗺️ Roadmap

- [x] **Phase 1:** Multi-Scanner Orchestration & Web Dashboard
- [x] **Phase 2:** AI-Powered Fix Generation
- [x] **Phase 3:** Team Collaboration & Shared Scans
- [x] **Phase 4:** GitHub, Slack & Webhook Integrations
- [x] **Phase 5:** Public Reports & Security Badges
- [ ] **Phase 6:** VS Code Extension (Q2 2026)
- [ ] **Phase 7:** Self-Hosted Enterprise Edition (Q3 2026)
- [ ] **Phase 8:** Native CI/CD Integration (GitHub Actions, GitLab CI)

---

## ⚡ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | FastAPI (Python) |
| Frontend | React + TypeScript + Tailwind CSS |
| Database | PostgreSQL |
| Queue | Redis + Celery |
| AI | Google Gemini, DeepSeek, OpenAI, OpenRouter (auto-fallback) |
| Hosting | Render (API), DigitalOcean (Workers) |
| Security Tools | Semgrep, Gitleaks, Trivy, Bandit, ESLint, Hadolint, Checkov, OSV-Scanner, TruffleHog |

---

## 🤝 Built by a Solo Developer

Debuggix is a sovereign product. No VCs. No data selling. No bloated enterprise features you don't need. Just one developer who cares about making the web more secure.

- ⭐ **Star this repo** to support the project
- 🐛 **Found a bug?** [Open an issue](https://github.com/Lucky3mc/debuggix/issues)
- 📧 **Enterprise inquiries:** [luckydiety@gmail.com](mailto:luckydiety@gmail.com)
- 🌐 **Website:** [debuggix.space](https://debuggix.space)

---

## 📄 License

Debuggix is proprietary software. This repository serves as public documentation and the community hub. AI-generated fixes are suggestions — always review code before merging.

<p align="center">
  <b>The best time to secure your code was yesterday. The second best time is now.</b><br>
  <a href="https://debuggix.space"><strong>Try Debuggix Free →</strong></a>
</p>
```
