# 🟠 Week 4 — Bug Tracking & Defect Management

> **Week Goal:** Become proficient at identifying, documenting, prioritizing, and tracking bugs through their full lifecycle using Jira.

---

## 📚 Learning Objectives

By the end of this week, you will be able to:

- [ ] Explain the complete **defect lifecycle** — from discovery to closure
- [ ] Write a clear, **reproducible bug report** that developers can act on immediately without asking follow-up questions
- [ ] Use **Jira** to create, assign, prioritize, and track bugs
- [ ] Classify bugs correctly by **severity** and **priority** — and explain the critical difference
- [ ] Perform **5 Whys root cause analysis** on a discovered defect

---

## 📖 Key Topics & Theory

### 1. The Defect Lifecycle

Every bug goes through a defined lifecycle in a well-run QA process:

```
                        ┌──── Rejected (not a bug)
                        │
New → Assigned → Open ──┼──── Deferred (won't fix now)
                        │
                      Fixed → Retest ──┬── Closed ✅
                                       │
                                    Reopened → (back to Open)
```

| Status | Who Acts | What It Means |
|--------|----------|---------------|
| **New** | QA | Bug just logged; not yet reviewed |
| **Assigned** | Manager / TL | Bug assigned to a developer |
| **Open / In Progress** | Developer | Developer is actively working on the fix |
| **Fixed** | Developer | Developer claims it's resolved; build delivered to QA |
| **Retest** | QA | QA verifying if the fix actually works |
| **Closed** | QA | Confirmed fixed; issue resolved |
| **Reopened** | QA | Bug was "fixed" but QA still sees the problem |
| **Deferred** | Product Owner | Valid bug; won't be fixed in this release |
| **Rejected** | Developer / TL | Not a bug — works as designed, or cannot be reproduced |

---

### 2. Severity vs. Priority — The Critical Distinction

This is one of the most misunderstood topics in QA. Know it cold:

| | **Severity** | **Priority** |
|-|-------------|-------------|
| **Definition** | How badly does this impact system functionality? | How urgently does this need to be fixed? |
| **Set by** | QA / Tester | Product Owner / Business stakeholder |
| **Based on** | Technical impact on the system | Business value, schedule, visibility |

**Classic Matrix:**

| | High Priority | Low Priority |
|--|--------------|-------------|
| **High Severity** | Crash on the main checkout flow — fix *now* | Crash in an admin tool used by 2 people — schedule for next sprint |
| **Low Severity** | Company logo shown incorrectly on homepage — fix before tomorrow's launch | Tooltip has a typo — fix whenever |

**Severity Levels:**

| Level | Definition | Example |
|-------|-----------|---------|
| 🔴 **Critical / Blocker** | App crash, data loss, security breach; testing cannot continue | Clicking "Submit Order" crashes the app |
| 🟠 **Major** | Key feature doesn't work; workaround may exist | Users can't upload profile photos |
| 🟡 **Minor** | Feature partially works; deviation from spec | Dropdown shows options in wrong order |
| 🟢 **Trivial** | Cosmetic or very minor UI issue; no functional impact | Button text has inconsistent capitalization |

---

### 3. Anatomy of a Great Bug Report

This is the template every bug you write should follow. See the full template at [../templates/bug-report-template.md](../templates/bug-report-template.md).

| Field | Bad Example ❌ | Good Example ✅ |
|-------|--------------|----------------|
| **Title** | "Login broken" | "Login fails with valid credentials when 'Remember Me' is checked — Firefox 120 only" |
| **Environment** | N/A | macOS 14.3, Firefox 120.0, Staging v2.4.1, test account: qa_test_01 |
| **Steps** | "Go log in and it breaks" | 1. Navigate to `/login` 2. Enter `qa_test_01@test.com` 3. Enter `Password123!` 4. Check "Remember Me" 5. Click "Sign In" |
| **Expected** | "Should work" | "User is redirected to `/dashboard` and session persists after browser restart" |
| **Actual** | "It doesn't work" | "Page refreshes. User remains on `/login`. Console shows: `TypeError: Cannot read property 'token' of undefined`" |
| **Severity/Priority** | (blank) | Severity: Major / Priority: P1 |
| **Attachments** | (none) | `login_bug_recording.mp4` + `console_error.png` |
| **Reproducibility** | "sometimes" | 100% reproducible with steps above |

---

### 4. The 5 Whys — Root Cause Analysis

The **5 Whys** is a technique for drilling down to the real root cause of a defect, rather than addressing symptoms.

**Example:**

| Step | Question | Answer |
|------|----------|--------|
| Problem | Users can't complete checkout | — |
| Why 1 | Why can't users complete checkout? | The payment API call fails |
| Why 2 | Why does the payment API call fail? | The API endpoint URL is wrong in production config |
| Why 3 | Why is the URL wrong in production? | The config file was not updated during deployment |
| Why 4 | Why wasn't the config file updated? | There's no deployment checklist that includes config verification |
| Why 5 | Why is there no checklist? | We've never had a process for documenting deployment steps |
| **Root Cause** | **No deployment checklist** | **Action: Create and enforce a deployment checklist** |

> 💡 The goal is to find a **process failure**, not a **person failure**. "Bob forgot" is never a root cause — "There was no process to ensure Bob couldn't forget" is.

---

### 5. Jira Basics for QA Engineers

| Jira Feature | QA Use Case |
|-------------|-----------|
| **Issues** | Log bugs, tasks, stories |
| **Bug Issue Type** | Specifically for defect reports |
| **Projects** | Organize work by team/product |
| **Boards (Kanban/Scrum)** | Visualize workflow and bug status |
| **Filters / JQL** | Search: `issuetype = Bug AND status = Open AND priority = High` |
| **Labels & Components** | Tag bugs by module (Login, Cart, API) |
| **Attachments** | Add screenshots, videos, log files |
| **Comments** | Communicate with dev on the issue |
| **Transitions** | Move issues through workflow stages |

**Essential JQL (Jira Query Language) for Beginners:**
```sql
-- All open critical bugs on your project
project = MYPROJECT AND issuetype = Bug AND status != Closed AND priority = Critical

-- Bugs assigned to you
project = MYPROJECT AND issuetype = Bug AND assignee = currentUser()

-- Bugs marked for retest
project = MYPROJECT AND issuetype = Bug AND status = "Retest"

-- Bugs found this week
project = MYPROJECT AND issuetype = Bug AND created >= startOfWeek()
```

---

## 🛠️ Hands-on Tasks & Activities

| Day | Activity |
|-----|----------|
| **Monday** | Set up your Jira project (free tier): create project, configure bug workflow, explore the interface |
| **Tuesday** | Execute test cases from Week 3 on the demo app; log every bug found in Jira using the full template |
| **Wednesday** | Mentor provides 5 poorly written bug reports; rewrite all 5 professionally |
| **Thursday** | Triage 10 sample bugs (provided by mentor): assign severity + priority + written justification for each |
| **Friday** | Perform 5 Whys analysis on one bug; compile all deliverables and submit |

### Bug Writing Practice — Common Scenarios to Test
- What happens when you submit an empty form?
- What happens when you enter a very long string (500+ characters) into a text field?
- What happens when a required field contains only spaces?
- What happens when you try to submit the same form twice quickly (double-click)?
- What happens if you navigate directly to a protected page without being logged in?
- What happens at the session timeout — does the app handle it gracefully?

---

## 🖥️ Tools & Software

| Tool | Purpose | Cost |
|------|---------|------|
| **Jira Software** | Bug tracking, project management | Free for ≤10 users |
| **Loom** | Record bug reproduction as video | Free tier |
| **Lightshot / Greenshot** | Annotated screenshots | Free |
| **GitHub Issues** | Lightweight alternative bug tracker | Free |

### Jira Free Tier Setup
1. Go to [atlassian.com/software/jira](https://www.atlassian.com/software/jira)
2. Sign up with your email
3. Create a new Scrum or Kanban project
4. Add issue types: Bug, Task, Story
5. Add yourself and your mentor to the project
6. Log your first bug!

---

## 📚 Recommended Resources

- 📹 "How to Write a Professional Bug Report" — Software Testing Mentor YouTube
- 📹 "Jira Tutorial — Complete Beginner to Advanced" — Atlassian YouTube
- 📹 "5 Whys Root Cause Analysis" — Lean Enterprise Institute YouTube
- 📖 "Severity vs Priority — The Difference Explained" — browserstack.com
- 📖 "Defect Life Cycle in Software Testing" — guru99.com
- 🆓 **Jira Fundamentals Certification** (free) — [university.atlassian.com](https://university.atlassian.com)
- 📖 "Lessons Learned in Software Testing" — Chapter on Bug Reports (Kaner, Bach, Pettichord)

---

## 📝 Deliverables — Due Friday EOD

### Deliverable 1: Jira Bug Reports (10 minimum)
- Log 10 bugs found during this week's testing in your Jira project
- Every single field in the bug template must be filled
- At least 2 bugs must be Critical or Major severity
- At least 3 bugs must have a video reproduction (Loom link in the bug)
- Screenshot of your Jira board showing the bugs logged

### Deliverable 2: Bug Report Rewrite
- Original versions of 5 "bad" bug reports (provided by mentor)
- Your professionally rewritten versions
- For each: a brief explanation of *what* you improved and *why*

### Deliverable 3: Severity/Priority Matrix
Table with 10 bugs (provided by mentor):

| Bug # | Bug Description | Severity | Priority | Justification |
|-------|----------------|----------|----------|---------------|
| 1 | ... | ... | ... | ... |

### Deliverable 4: 5 Whys Root Cause Analysis
- Choose one bug found this week
- Document the full 5 Whys chain (minimum 4 levels deep)
- Identify the root cause
- Propose a process improvement to prevent recurrence
- Length: ~1 page

---

## ✅ Assessment & Feedback Criteria

| Criteria | Excellent (4) | Good (3) | Developing (2) | Needs Work (1) |
|----------|--------------|----------|---------------|----------------|
| **Bug report quality** | Developer could reproduce & fix without asking any questions | Minor clarification needed | Some ambiguity; steps incomplete | Unusable without significant help |
| **Jira proficiency** | Used boards, JQL, filters, attachments, transitions | Used basic features independently | Required mentor guidance | Could not use Jira independently |
| **Severity/Priority accuracy** | All correctly classified with solid justification | 8–10 correct | 5–7 correct | Fewer than 5 correct |
| **Root cause analysis** | Deep, insightful chain; process-level root cause identified | Adequate; reached root cause | Surface-level; stopped at symptoms | Not completed meaningfully |

---

## 💼 Real-World Application & Tips

> 🏢 **In real companies:** A QA engineer's bug reports are their most visible work product. Developers, product managers, and senior engineers form strong opinions about QA team members based on the quality and clarity of their defect reports. A well-written bug report that saves a developer 30 minutes of confused work is a career-building move.

> 💡 **Pro Tip:** Before logging a bug, always ask:
> 1. "Can I reproduce this consistently?" (If not, document how to reproduce it intermittently)
> 2. "Has this already been reported?" (Search Jira before logging — duplicates waste everyone's time)
> 3. "Do I have enough evidence?" (Screenshot at minimum; video preferred for UI bugs)

> ⚠️ **Common Mistake:** Setting every bug as "Critical / P1." This is called **priority inflation** and it causes the entire team to lose trust in the bug tracker because "everything is critical" means nothing actually gets treated as urgent.

---

*← [Week 3 — Test Case Design](../Week-3-Test-Case-Design/README.md) | [Week 5 — Agile & Scrum →](../Week-5-Agile-Scrum/README.md)*
