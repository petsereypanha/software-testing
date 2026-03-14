# 🔵 Week 2 — Software Testing Fundamentals

> **Week Goal:** Understand the full landscape of software testing types, levels, and methodologies — and begin hands-on manual testing of a real application.

---

## 📚 Learning Objectives

By the end of this week, you will be able to:

- [ ] Identify and distinguish all major **levels** of software testing (unit, integration, system, UAT)
- [ ] Categorize testing **types**: functional, non-functional, structural, and change-related
- [ ] Explain the difference between **black-box**, **white-box**, and **grey-box** testing
- [ ] Execute **exploratory testing** on a live application and document findings professionally
- [ ] Perform a **smoke test** and explain its purpose in the release process

---

## 📖 Key Topics & Theory

### 1. Testing Levels — The Testing Stack

Think of testing levels as layers — each builds on the one before:

```
┌─────────────────────────────────────────────┐
│         User Acceptance Testing (UAT)        │  ← Business/Client validates needs
├─────────────────────────────────────────────┤
│              System Testing                  │  ← QA tests the full application
├─────────────────────────────────────────────┤
│           Integration Testing                │  ← How modules interact together
├─────────────────────────────────────────────┤
│               Unit Testing                   │  ← Developers test individual functions
└─────────────────────────────────────────────┘
```

| Level | Who Performs It | Focus | Example |
|-------|----------------|-------|---------|
| **Unit** | Developer | Single function or class | `calculateTax(100)` returns `15` |
| **Integration** | Dev + QA | Module-to-module data flow | Login service correctly queries the user database |
| **System** | QA | Full end-to-end application behavior | User can register, log in, and place an order |
| **UAT** | Business / End User | Business requirements met | Stakeholder confirms the checkout flow matches business rules |

---

### 2. Testing Types

#### Functional Testing (Does the system do what it should?)

| Type | Purpose | When |
|------|---------|------|
| **Smoke Testing** | Quick sanity check: "Is the app alive and runnable?" | Before every test cycle begins |
| **Sanity Testing** | Verify a specific fix/change works | After a bug fix or minor build |
| **Regression Testing** | Ensure new changes didn't break old features | After every Sprint / deployment |
| **Functional Testing** | Verify each feature works per specification | Throughout development |
| **End-to-End Testing** | Test complete user workflows | Before release |

#### Non-Functional Testing (How well does it do it?)

| Type | Tests For |
|------|----------|
| **Performance Testing** | Speed, load capacity, response times |
| **Security Testing** | Vulnerabilities, unauthorized access |
| **Usability Testing** | Ease of use, user satisfaction |
| **Compatibility Testing** | Works across browsers, OS, devices |
| **Accessibility Testing** | Usable by people with disabilities |

#### Change-Related Testing

| Type | When to Use |
|------|------------|
| **Regression Testing** | After any code change to ensure no new breakage |
| **Confirmation Testing** | After a specific bug is fixed — verify the exact fix works |

---

### 3. Black-box vs. White-box vs. Grey-box

| Method | Tester Knows | Tests | Best For |
|--------|-------------|-------|---------|
| **Black-box** | Only inputs and expected outputs; no code | External behavior | Functional, UAT, System testing |
| **White-box** | Full source code and internal structure | Logic paths, branches, conditions | Unit testing, code coverage |
| **Grey-box** | Partial knowledge (e.g., API contracts or DB schema) | Mixed | Integration, API testing |

> 💡 **Most QA engineers work primarily in black-box testing** — you test the application as a user would, without needing to read the source code.

---

### 4. Static vs. Dynamic Testing

| Type | Definition | Examples |
|------|-----------|---------|
| **Static Testing** | Review without executing the software | Code reviews, requirement walkthroughs, design reviews, inspections |
| **Dynamic Testing** | Execute the software and observe its behavior | Manual testing, automated tests, exploratory testing |

---

### 5. Exploratory Testing

Exploratory testing is **simultaneous learning, test design, and execution**. Unlike scripted testing, there's no predefined step-by-step script. Instead, a tester uses:
- **Skill** — knowledge of testing heuristics and techniques
- **Intuition** — "something feels off here"
- **Domain knowledge** — understanding how the feature is *supposed* to work

**Session-Based Exploratory Testing (SBET):**
Structure your session with a **charter** (goal + timeframe):

```
Charter: Explore the login functionality for security and input handling issues
Time Box: 90 minutes
Focus Areas: Input validation, session management, error messages, edge-case credentials
```

During the session: take notes, capture screenshots, log issues.
After the session: write up your findings.

---

### 6. Smoke Testing vs. Sanity Testing

| | **Smoke Test** | **Sanity Test** |
|-|---------------|----------------|
| **What** | Broad, shallow check: is the build stable? | Narrow, deep check: does this one fix work? |
| **When** | Beginning of every test cycle | After a targeted bug fix |
| **Coverage** | All major features, briefly | One specific feature or fix |
| **Time** | 5–15 minutes | 10–30 minutes |
| **Analogy** | Turn on power and see if smoke appears | Open the hood and check the specific part you repaired |

---

## 🛠️ Hands-on Tasks & Activities

**Practice Application Options (choose one or use your company's staging environment):**
- 🔗 [The Internet (Heroku)](https://the-internet.herokuapp.com/) — various test scenarios
- 🔗 [OrangeHRM Demo](https://opensource-demo.orangehrmlive.com/) — HR management app
- 🔗 [DemoQA](https://demoqa.com/) — form inputs, widgets, interactions
- 🔗 [SauceDemo](https://www.saucedemo.com/) — e-commerce app (user: `standard_user` / pass: `secret_sauce`)

### Daily Schedule

| Day | Activity | Deliverable |
|-----|----------|-------------|
| **Monday** | Perform 90-min exploratory testing on a login page; document all findings | Session charter + notes |
| **Tuesday** | Test form inputs (file upload, date picker, dropdown, number range) using boundary values | Findings log |
| **Wednesday** | Create and execute a 10–15 step smoke test checklist for the whole app | Smoke test checklist |
| **Thursday** | Test a full user workflow (register → login → perform action → logout); document all steps | End-to-end test notes |
| **Friday** | Compile all deliverables; write comparison report; submit | All 4 deliverables |

### Exploratory Testing Heuristics (Use These as Guides)
Use the **SFDIPOT** heuristic to guide your exploratory sessions:
- **S**tructure — can you break the app structure?
- **F**unction — does each function work correctly?
- **D**ata — what happens with unusual/extreme data?
- **I**nterface — UI elements, navigation, consistency
- **P**latform — different browsers/OS behavior
- **O**perations — what if multiple things happen at once?
- **T**ime — what happens after inactivity? Date/time edge cases?

---

## 🖥️ Tools & Software to Learn This Week

| Tool | Purpose | Cost | Setup |
|------|---------|------|-------|
| **Chrome DevTools** | Inspect elements, console errors, network requests | Free (built-in) | Press F12 in Chrome |
| **Loom** | Record bug reproduction videos | Free | loom.com |
| **Lightshot / Greenshot** | Annotated screenshots | Free | app.prntscr.com |
| **Google Sheets** | Manual test log/tracking | Free | sheets.google.com |
| **BrowserStack** | Cross-browser testing | 30-day free trial | browserstack.com |

### Chrome DevTools — Quick Reference for Testers

| Tab | What to Check |
|-----|--------------|
| **Console** | JavaScript errors (red errors = bugs!) |
| **Network** | API calls, HTTP status codes, response payloads |
| **Elements** | DOM structure, CSS issues |
| **Application** | Cookies, localStorage, session data |
| **Performance** | Page load times, rendering issues |

---

## 📚 Recommended Resources

### Videos
- 📹 "Types of Software Testing — Full List Explained" — Software Testing Help YouTube
- 📹 "Manual Testing Tutorial for Beginners" — Naveen AutomationLabs YouTube
- 📹 "Exploratory Testing: A Tutorial" — Ministry of Testing YouTube

### Reading
- 📖 "Software Testing Types — Complete Guide" — guru99.com
- 📖 "Exploratory Testing Explained" — James Bach — satisfice.com
- 📖 "How to Use Chrome DevTools for QA" — browserstack.com blog

### Courses (Free)
- 🆓 "Introduction to Software Testing" — Coursera, University of Minnesota (audit free)
- 🆓 "Software Testing Tutorial" — uTest Academy — academy.utest.com

---

## 📝 Deliverables — Due Friday EOD

### Deliverable 1: Exploratory Session Notes
Using the [Session Charter Template](../templates/session-charter-template.md):
- Completed charter (goal, time box, areas covered)
- Structured notes: what you clicked, what you observed, what you found
- At least 5 findings documented (bugs, unexpected behavior, potential risks)

### Deliverable 2: Smoke Test Checklist
**Format:** Google Sheet or table
- Application name and version tested
- 10–15 test steps covering all major features
- Pass/Fail column with notes
- Overall smoke test verdict: PASS / FAIL

### Deliverable 3: End-to-End Workflow Test
**Format:** Numbered steps document
- Full workflow tested (e.g., register → login → perform key action → logout)
- Screenshots at each key step
- Any deviations from expected behavior noted

### Deliverable 4: Black-box vs. White-box Comparison Report
**Length:** ~1 page
**Content:**
- Define both approaches in your own words
- When would you choose black-box? Provide a real example.
- When would you choose white-box? Provide a real example.
- Which approach do QA engineers use most, and why?

---

## ✅ Assessment & Feedback Criteria

| Criteria | Excellent (4) | Good (3) | Developing (2) | Needs Work (1) |
|----------|--------------|----------|---------------|----------------|
| **Testing vocabulary** | All terms used correctly throughout | Mostly correct; minor misuse | Some misuse of terms | Frequent or fundamental errors |
| **Test coverage depth** | Found 8+ issues including edge cases | Found 5–7 issues | Found 2–4 issues | Found 0–1 issues |
| **Documentation quality** | Clear, reproducible, professional format | Adequate; minor gaps | Vague or missing steps | Unusable without help |
| **Critical thinking** | Proactively tested edge cases and negatives | Tested main flows + some edge cases | Only happy-path testing | Minimal or random testing |

**Scoring:** Max = 16 points. Target: ≥ 12 points.

---

## 💼 Real-World Application & Tips

> 🏢 **In real companies:** QA engineers spend roughly 40% of their time doing exploratory testing, especially during early Sprint phases before formal test cases are written. Skilled exploratory testers find the bugs that scripted testers miss because scripts can't anticipate every possible user behavior.

> 💡 **Pro Tip:** Always test the **negative path** (wrong passwords, empty fields, invalid formats, extreme numbers, special characters). That's where 70% of real bugs hide — not in the happy path.

> 💡 **Pro Tip:** Open Chrome DevTools before you start testing. A red error in the Console that the user would never notice could indicate a serious underlying problem.

> ⚠️ **Common Mistake:** Testing only what's explicitly mentioned in the requirements. A QA engineer's job includes testing what's *implied* — if a banking app doesn't say "you shouldn't be able to transfer $-1," that doesn't mean you shouldn't test it.

---

*← [Week 1 — QA Foundations](../Week-1-QA-Foundations/README.md) | [Week 3 — Test Case Design →](../Week-3-Test-Case-Design/README.md)*
