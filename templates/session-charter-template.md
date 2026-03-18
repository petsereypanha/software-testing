# Exploratory Testing Session Charter Template

> Session-Based Exploratory Testing (SBET) is a structured way to conduct unscripted testing.
> Complete this charter BEFORE your session. Fill in the results DURING and AFTER the session.

---

## Pre-Session Setup

| Field | Value |
|-------|-------|
| **Session ID** | SESSION_[DATE]_[FEATURE] (e.g., SESSION_20260315_LOGIN) |
| **Tester Name** | |
| **Date** | |
| **Start Time** | |
| **End Time** | |
| **Planned Duration** | 90 minutes (adjust as needed; 90 min is ideal) |
| **Application** | |
| **Version / Build** | |
| **Environment** | Staging / Production |

---

## Charter (Define BEFORE the Session)

### Mission Statement
*Complete this sentence: "Explore [area] to discover [what you're looking for]"*

> Example: "Explore the user registration flow to discover security vulnerabilities, input validation failures, and edge cases in the email and password fields."

### Focus Areas
*List 3–5 specific areas or questions you want to investigate:*

1. 
2. 
3. 
4. 
5. 

### Out of Scope for This Session
*What are you deliberately NOT exploring this session? (Stay focused — breadth over depth leads to shallow sessions)*

-
-

### Setup Required
*What do you need before starting?*
- [ ] Application accessible at: _______________
- [ ] Test account(s) prepared
- [ ] Screen recording tool running (Loom / OBS)
- [ ] Browser DevTools open (Console + Network tabs)
- [ ] Note-taking document open

---

## Session Notes (Fill During the Session)

Use time-stamped notes. Write EVERYTHING you observe — even things that seem irrelevant. You can filter later.

| Time | Action Taken | Observation | Worth Investigating? |
|------|-------------|-------------|---------------------|
| 0:00 | Opened application login page | Page loads in ~1.2 seconds; 3 network requests | No |
| 0:05 | Entered valid credentials and logged in | Redirected to dashboard as expected | No |
| 0:08 | Tried empty password field + submit | Error: "Password is required" — good | No |
| 0:12 | Tried `<script>alert(1)</script>` in username | Alert executed! 🐛 XSS vulnerability | **YES — file bug** |
| *(continue...)* | | | |

### Quick Findings Log
Log potential bugs quickly during the session (full bug report written after):

| Finding # | Area | Description | Severity Guess |
|-----------|------|-------------|---------------|
| F1 | Registration | XSS in username field executes JavaScript | Critical |
| F2 | Login | No lockout after 10+ failed attempts | Major |
| *(add more)* | | | |

---

## Session Debrief (Fill After the Session)

### What Did I Cover?
*List the areas you actually explored (vs. what you planned):*

-
-
-

### What Interesting Things Did I Find?
*Summarize your most significant discoveries:*

-
-
-

### Bugs Found
| Bug # | Title | Jira Ticket # |
|-------|-------|---------------|
| | | |

### What Did I NOT Get To Test?
*List what was in scope but not covered (so you can plan a follow-up session):*

-
-

### What Should Be Explored Next?
*New questions or areas that emerged during this session:*

-
-

---

## Session Metrics

| Metric | Value |
|--------|-------|
| **Actual Duration** | |
| **Areas Covered** | |
| **Total Findings** | |
| **Bugs Logged** | |
| **Open Questions Generated** | |
| **Percentage of Charter Completed** | |

---

## Heuristics Used This Session
Check all that you applied:

- [ ] **SFDIPOT** — Structure, Function, Data, Interface, Platform, Operations, Time
- [ ] **CRUD** — Create, Read, Update, Delete for every entity
- [ ] **Error Guessing** — What inputs are most likely to cause errors?
- [ ] **Boundary Testing** — Fields at their min/max limits
- [ ] **Negative Testing** — What happens with invalid/unexpected inputs?
- [ ] **Security** — XSS, SQLi, IDOR, auth bypass
- [ ] **Session Testing** — Long sessions, timeouts, concurrent logins
- [ ] **Back button** — Does navigating back cause issues?
- [ ] **Rapid fire** — Submit forms multiple times rapidly
