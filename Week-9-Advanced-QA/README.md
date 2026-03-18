# ⚡ Week 9 — Performance, Security & Advanced QA Topics

> **Week Goal:** Explore non-functional testing — performance, security, and accessibility — the areas that separate good QA engineers from great ones.

---

## 📚 Learning Objectives

By the end of this week, you will be able to:

- [ ] Explain performance testing types (load, stress, spike, endurance) and run a basic load test
- [ ] Identify the **OWASP Top 10** security vulnerabilities and demonstrate a basic security test
- [ ] Perform a **security test** safely on a deliberately vulnerable application (DVWA)
- [ ] Conduct an **accessibility audit** using axe DevTools and keyboard testing
- [ ] Use **Google Lighthouse** for a quick multi-dimensional quality score

---

## 📖 Key Topics & Theory

### 1. Performance Testing Types

| Type | What It Tests | Scenario |
|------|--------------|----------|
| **Load Testing** | Normal expected traffic volume | 100 concurrent users for 30 minutes |
| **Stress Testing** | Beyond maximum capacity — where does it break? | Ramp up to 2000 users until the server fails |
| **Spike Testing** | Sudden, extreme traffic bursts | 0 → 5,000 users in 30 seconds (flash sale) |
| **Endurance Testing** | Extended period at normal load | 200 concurrent users for 8 hours (memory leaks) |
| **Volume Testing** | Large amounts of data | 10 million records in the database |
| **Scalability Testing** | How performance improves as resources scale | Add a server — does throughput double? |

---

### 2. Key Performance Metrics

| Metric | Definition | Acceptable Target |
|--------|-----------|------------------|
| **Response Time** | Time from request to first byte | < 200ms (50th percentile); < 500ms (95th) |
| **Throughput (RPS)** | Requests processed per second | Depends on requirements |
| **Error Rate** | % of failed requests under load | < 1% under normal load |
| **Concurrent Users** | Simultaneous active users handled | Per business requirements |
| **CPU Utilization** | Server CPU usage under load | < 70% under normal load |
| **Memory Usage** | RAM consumed over time | Should not grow continuously (memory leak check) |
| **Apdex Score** | User satisfaction index (0–1) | > 0.9 is "Excellent" |

---

### 3. Apache JMeter — Basic Load Test Structure

```
Test Plan
  └── Thread Group (= virtual users)
        ├── Number of Threads: 100 (users)
        ├── Ramp-up Period: 30 seconds
        ├── Loop Count: 5 (each user sends 5 requests)
        │
        ├── HTTP Request Defaults (Base URL: https://reqres.in)
        │
        ├── HTTP Request: GET /api/users
        ├── HTTP Request: POST /api/login
        │
        └── Listeners (Results Viewers)
              ├── Summary Report
              ├── View Results Tree
              └── Aggregate Graph
```

---

### 4. OWASP Top 10 — The QA Tester's Security Checklist

The **OWASP Top 10** is the definitive list of the most critical web application security vulnerabilities. QA engineers should be able to **test for** (not exploit) these vulnerabilities:

| # | Vulnerability | QA Test Approach |
|---|--------------|-----------------|
| **A01** | Broken Access Control | Can user A view/modify user B's data by changing an ID? |
| **A02** | Cryptographic Failures | Is sensitive data sent over HTTP? Stored as plaintext passwords? |
| **A03** | Injection (SQL, XSS, Command) | Does `' OR '1'='1` bypass login? Does `<script>alert(1)</script>` execute? |
| **A04** | Insecure Design | Are security controls designed in from the start, or bolted on? |
| **A05** | Security Misconfiguration | Default passwords? Verbose error messages leaking server info? Directory listing? |
| **A06** | Vulnerable Components | Are dependencies up to date? `npm audit`, `pip audit` clean? |
| **A07** | Auth Failures | Brute-forcing allowed? Weak passwords accepted? Tokens expire properly? |
| **A08** | Data Integrity Failures | Is user input validated and sanitized? Unsigned JWTs accepted? |
| **A09** | Logging Failures | Are security events (login failures, admin access) logged? |
| **A10** | SSRF | Can you cause the server to fetch internal network resources? |

---

### 5. Basic Security Test Examples (for Authorized Apps Only)

```
1. SQL Injection — in login username field:
   Input: admin' OR '1'='1'; --
   → Expected: 400/401 error, NOT bypassed authentication
   → Bug if: You are logged in without a real account

2. Cross-Site Scripting (XSS) — in search or comment field:
   Input: <script>alert('XSS')</script>
   → Expected: Displayed as plain text, NOT executed
   → Bug if: An alert dialog appears

3. Insecure Direct Object Reference (IDOR):
   After logging in as User A:
   Request: GET /api/orders/12345  (User B's order ID)
   → Expected: 403 Forbidden
   → Bug if: You can see User B's private order details

4. Broken Authentication — Password Policy:
   Register with password: "1"
   → Expected: Rejected with strength requirements error
   → Bug if: The account is created successfully

5. Information Leakage in Errors:
   Trigger a 500 error (send malformed data)
   → Expected: Generic "Something went wrong" message
   → Bug if: Stack trace, file paths, version info visible

6. Sensitive Data Over HTTP (use browser DevTools → Network):
   → Expected: All requests use HTTPS (padlock icon)
   → Bug if: Any sensitive data transmitted over plain HTTP
```

> ⚠️ **IMPORTANT:** Only test these on applications you are explicitly authorized to test. Authorized options include: DVWA (local install), company staging environments, deliberately vulnerable practice apps. **Never test third-party live applications.**

---

### 6. Setting Up DVWA (Damn Vulnerable Web App)

DVWA is a deliberately insecure PHP web application for practicing security testing legally.

```bash
# Using Docker (easiest method):
docker pull vulnerables/web-dvwa
docker run -d -p 80:80 vulnerables/web-dvwa

# Access in browser: http://localhost/
# Default login: admin / password
# Setup: click "Create / Reset Database"
# Set security level to "Low" for initial practice
```

**DVWA Security Labs to Practice:**
- SQL Injection: `/dvwa/vulnerabilities/sqli/`
- XSS (Reflected): `/dvwa/vulnerabilities/xss_r/`
- XSS (Stored): `/dvwa/vulnerabilities/xss_s/`
- Brute Force: `/dvwa/vulnerabilities/brute/`
- CSRF: `/dvwa/vulnerabilities/csrf/`

---

### 7. Accessibility Testing (A11y)

**WCAG 2.1** (Web Content Accessibility Guidelines) — 4 core principles:

| Principle | Meaning |
|-----------|---------|
| **Perceivable** | Content is available to all senses (alt text for images, captions for video) |
| **Operable** | All functionality works via keyboard; sufficient time to interact |
| **Understandable** | Language is clear; errors are descriptive; forms are labeled |
| **Robust** | Compatible with assistive technologies (screen readers, voice control) |

**WCAG Conformance Levels:**
- **Level A** — Minimum (must pass)
- **Level AA** — Standard (most regulations require this)
- **Level AAA** — Enhanced (best practice)

#### Quick Accessibility Test Checklist
- [ ] All images have descriptive `alt` text (or `alt=""` if decorative)
- [ ] All form fields have visible, associated `<label>` elements
- [ ] Color is not the only way information is conveyed
- [ ] Text has sufficient contrast ratio (4.5:1 for normal text)
- [ ] All functionality is reachable and usable with keyboard only (Tab + Enter)
- [ ] Focus indicator is visible when using keyboard
- [ ] Page has a meaningful `<title>` and heading hierarchy (h1 → h2 → h3)
- [ ] Links have descriptive text (not just "Click here" or "Read more")
- [ ] Videos have captions (if applicable)
- [ ] No content flashes more than 3 times per second (seizure risk)

---

### 8. Google Lighthouse — Free Instant Audit

Open Chrome DevTools → **Lighthouse** tab → Generate Report

Scores (0–100) on:
- ⚡ **Performance** (load speed, Core Web Vitals)
- ♿ **Accessibility** (WCAG checks)
- ✅ **Best Practices** (HTTPS, no deprecated APIs)
- 🔍 **SEO** (crawlability, meta tags)

> 💡 Run Lighthouse on every web app you test. Zero setup, zero cost, instant insights.

---

## 🛠️ Hands-on Tasks & Activities

| Day | Activity |
|-----|----------|
| **Monday** | Set up and run a JMeter or k6 load test on a demo API; test at 10, 50, 100 virtual users; document results |
| **Tuesday** | Set up DVWA with Docker; complete SQL Injection + XSS labs; document each finding |
| **Wednesday** | Test the demo app for 5 OWASP Top 10 items; create a security test checklist |
| **Thursday** | Accessibility audit: run axe DevTools + manual keyboard testing on any public website; create report |
| **Friday** | Run Lighthouse on 3 websites; compile all deliverables |

### k6 Load Test Script (Alternative to JMeter)
```javascript
// load_test.js — run with: k6 run load_test.js
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '30s', target: 20 },   // Ramp up to 20 users
    { duration: '1m', target: 50 },    // Hold at 50 users
    { duration: '30s', target: 0 },    // Ramp down
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'],  // 95% of requests under 500ms
    http_req_failed: ['rate<0.01'],    // Error rate under 1%
  },
};

export default function () {
  const res = http.get('https://reqres.in/api/users?page=2');
  check(res, {
    'status is 200': (r) => r.status === 200,
    'response time < 500ms': (r) => r.timings.duration < 500,
  });
  sleep(1);
}
```

**Install k6:**
```bash
# macOS:
brew install k6

# Run test:
k6 run load_test.js
```

---

## 🖥️ Tools & Software

| Tool | Purpose | Cost |
|------|---------|------|
| **Apache JMeter** | GUI-based performance testing | Free / open source |
| **k6** | Code-based load testing (CLI) | Free / open source |
| **DVWA** (via Docker) | Safe SQL injection / XSS practice | Free |
| **OWASP ZAP** | Automated security scanning | Free |
| **axe DevTools** | Accessibility testing browser extension | Free (Chrome/Firefox) |
| **NVDA** | Windows screen reader | Free |
| **VoiceOver** | macOS/iOS built-in screen reader | Built-in (Cmd+F5) |
| **Google Lighthouse** | Performance + accessibility audit | Built into Chrome DevTools |
| **Docker Desktop** | Run DVWA container | Free |

---

## 📚 Recommended Resources

- 📹 "JMeter Tutorial for Complete Beginners" — Naveen AutomationLabs YouTube
- 📹 "k6 Load Testing Tutorial" — k6.io YouTube channel
- 📹 "OWASP Top 10 Explained" — TechWorld with Nana YouTube
- 📹 "Accessibility Testing — Where to Start" — Deque Systems YouTube
- 📖 **Official:** OWASP Top 10 (free PDF) — [owasp.org/Top10](https://owasp.org/Top10/)
- 📖 **Official:** WCAG 2.1 Quick Reference — [w3.org/WAI/WCAG21/quickref](https://www.w3.org/WAI/WCAG21/quickref/)
- 🆓 **Free Practice:** PortSwigger Web Security Academy — [portswigger.net/web-security](https://portswigger.net/web-security) (free labs)
- 🆓 **Free Practice:** DVWA — [github.com/digininja/DVWA](https://github.com/digininja/DVWA)

---

## 📝 Deliverables — Due Friday EOD

### Deliverable 1: Performance Test Report
- Tool used: JMeter or k6
- 3 test runs: 10, 50, 100 virtual users
- Results table: throughput (RPS), avg response time, 95th percentile, error rate for each run
- Graph screenshot (JMeter aggregate report or k6 dashboard)
- Brief analysis: at what point does performance degrade? What would you recommend investigating?

### Deliverable 2: Security Test Report
- Tests performed against DVWA (SQL Injection, XSS minimum)
- For each: vulnerability type, steps performed, expected vs. actual result, severity, screenshot
- OWASP checklist: apply OWASP Top 10 to a demo application; mark each as Pass / Fail / Not Tested

**⚠️ Reminder:** All security testing must be on DVWA (local), company-authorized staging environments, or PortSwigger Academy labs. Do NOT test third-party live systems.

### Deliverable 3: Accessibility Audit Report
- Website tested (choose any public site)
- axe DevTools scan results (screenshot of findings)
- Manual keyboard navigation test: can you complete all main task flows using only keyboard?
- 5 specific accessibility issues found (or "0 critical issues found with evidence")
- Lighthouse accessibility score screenshot

### Deliverable 4: Quality Audit Summary (1 page)
Personal reflection on all non-functional testing done this week:
- What did you find most valuable?
- What surprised you?
- If you were advising a company about their QA program, which of these areas would you recommend they prioritize first — and why?

---

## ✅ Assessment & Feedback Criteria

| Criteria | Excellent (4) | Good (3) | Developing (2) | Needs Work (1) |
|----------|--------------|----------|---------------|----------------|
| **Performance testing** | Correct setup; results at 3 load levels; trends analyzed; actionable findings | Ran tests; documented results | Test ran but results misunderstood | Could not complete setup |
| **Security testing** | Found 3+ vulnerabilities on DVWA; impacts stated; reports professional | Found 1–2 documented well | Conceptually understood but not tested | Testing on unauthorized targets ⚠️ |
| **Accessibility testing** | Used multiple tools; found real issues; keyboard tested | Used axe DevTools at least | Ran automated scan only | Did not test |
| **Ethical awareness** | Demonstrated clear understanding of authorized-only testing | Generally appropriate | Some oversight | Showed intent to test unauthorized systems |

---

## 💼 Real-World Application & Tips

> 🏢 **In real companies:** Performance and security testing are often done by specialists, but **all QA engineers are expected to have basic literacy** in both. The ability to say "This API has no rate limiting on login attempts — that's a potential brute-force risk" marks you as a senior-minded QA engineer regardless of your experience level.

> 💡 **Pro Tip:** Run Google Lighthouse on every web application you test. Zero setup, zero cost, and it gives you instant scores on Performance, Accessibility, Best Practices, and SEO — four dimensions that otherwise require separate tools.

> 💡 **Pro Tip:** The fastest way to test accessibility is to close your mouse and try to use the app with only your keyboard. If you get stuck, that's a bug. If you can't figure out where the focus is, that's a bug. Takes 5 minutes and reveals real issues.

---

*← [Week 8 — Test Automation](../Week-8-Test-Automation/README.md) | [Week 10 — Capstone Project →](../Week-10-Capstone/README.md)*
