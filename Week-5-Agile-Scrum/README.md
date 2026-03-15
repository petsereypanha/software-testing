# 🔷 Week 5 — Agile, Scrum & QA in the SDLC

> **Week Goal:** Understand how QA integrates into modern Agile and Scrum environments — and practice the actual day-to-day workflows used in today's software teams.

---

## 📚 Learning Objectives

By the end of this week, you will be able to:

- [ ] Explain Agile principles and describe how they differ from the Waterfall methodology
- [ ] Describe all **Scrum roles**, **ceremonies**, and **artifacts** — and QA's specific role in each
- [ ] Write **acceptance criteria** for user stories using Given/When/Then (Gherkin) format
- [ ] Participate meaningfully in a **Sprint Planning** and **Retrospective** meeting
- [ ] Explain **Shift-Left Testing** and why it matters for quality and cost

---

## 📖 Key Topics & Theory

### 1. Waterfall vs. Agile — Side by Side

| Dimension | Waterfall | Agile |
|-----------|-----------|-------|
| **Structure** | Sequential, phase-by-phase | Iterative Sprints (1–4 weeks each) |
| **Requirements** | Fully specified and frozen upfront | Evolve continuously through collaboration |
| **When testing happens** | After all development is complete | Throughout every single Sprint |
| **Customer involvement** | Start (requirements) and end (UAT) | Continuous — every Sprint review |
| **Handling change** | Difficult and expensive | Embraced and expected |
| **QA role** | Post-development gatekeeper | Co-creator embedded in the team |
| **Feedback cycles** | Monthly or quarterly | Bi-weekly or weekly |
| **Risk** | High — you learn if it works late | Lower — validated continuously |

> 💡 **The majority of modern software companies use Agile/Scrum.** If you cannot work effectively in a Scrum environment, you cannot function on most modern software teams.

---

### 2. The Scrum Framework

```
Product Backlog
      │
      ▼
Sprint Planning (QA reviews stories, writes acceptance criteria, estimates test effort)
      │
      ▼
┌─────────────────────────────────────────┐
│                Sprint (1–4 weeks)        │
│                                          │
│  Daily Standups (15 min/day)             │
│  Dev builds → QA tests → Bugs logged    │
│  Continuous collaboration                │
└─────────────────────────────────────────┘
      │
      ▼
Sprint Review (QA demonstrates tested features; reports quality status)
      │
      ▼
Sprint Retrospective (QA contributes process improvements)
      │
      ▼
[Next Sprint Planning]
```

---

### 3. Scrum Roles — QA Perspective

| Role | Responsibilities | Where QA Interacts |
|------|----------------|-------------------|
| **Product Owner** | Owns the backlog; defines priorities; writes user stories | QA clarifies acceptance criteria with PO |
| **Scrum Master** | Facilitates process; removes blockers; protects the team | QA escalates blockers to Scrum Master |
| **Development Team** | Builds the product | QA works daily with devs; pair on bugs |
| **QA Engineer** | Tests, reports quality, writes automation | Embedded in the team; attends all ceremonies |

---

### 4. Scrum Ceremonies — QA's Specific Role

#### Sprint Planning
**Duration:** 2–4 hours for a 2-week sprint
**QA's Role:**
- Review each story and ask: "How will this be tested?"
- Write or refine acceptance criteria for each story
- Identify edge cases and potential risks
- Estimate testing effort for each story (in story points or hours)
- Flag stories that are not "testable" due to missing details

**Questions QA should ask in Sprint Planning:**
- "What's the expected behavior when the user enters invalid data?"
- "Is there a design mockup for this? Does the mockup match the story?"
- "How will we know this is done?"
- "What are the non-functional requirements? (performance, security?)"
- "Are there any dependent services or external APIs involved?"

#### Daily Standup (Scrum Standup)
**Duration:** 15 minutes maximum
**Format — 3 questions:**
1. What did I complete yesterday?
2. What will I work on today?
3. Are there any blockers?

**Example of a good QA standup:**
> "Yesterday I completed testing on Stories 34 and 35 — both pass. I found 2 bugs (TICKET-89 and TICKET-90, both logged in Jira). Today I'm starting testing on Story 37. I have a blocker: Story 38 hasn't been deployed to staging yet — can someone from dev confirm when that'll be ready?"

**Example of a bad QA standup:**
> "I'm testing stuff." ← Gives zero visibility to the team

#### Sprint Review (Demo)
**QA's Role:**
- Report on test coverage: how many test cases ran, pass/fail/blocked counts
- Demonstrate tested features — show they work **and** show what you found / fixed
- Report any known issues that will carry into next Sprint
- Confirm the Definition of Done was met for each story

#### Sprint Retrospective
**Format — 3 questions:**
- **What went well?** (Celebrate wins — both big and small)
- **What could be improved?** (Be honest; no finger-pointing)
- **What action items do we commit to?** (Specific, assigned, measurable)

**Examples of good QA contributions in a retrospective:**
- "The test environment was unstable for 2 days — we should add environment health checks to our DoD"
- "We found 3 bugs in production that we should have caught in testing — let's review our regression checklist"
- "I got stories 2 days before they were done — gave me no time to prepare tests. Can we agree on a 'ready for testing' definition?"

---

### 5. Acceptance Criteria — Given/When/Then (Gherkin Format)

Acceptance criteria define the **specific conditions** that must be met for a user story to be considered "done." The Gherkin format makes them directly usable as automated test scenarios.

**Structure:**
```gherkin
Feature: [Feature name]

Scenario: [Descriptive name of this specific scenario]
    GIVEN [initial context / precondition]
    AND [additional context]
    WHEN [the action taken]
    AND [additional action]
    THEN [the expected outcome]
    AND [additional expected outcome]
```

**Example — User Login:**
```gherkin
Feature: User Authentication

Scenario: Successful login with valid credentials
    GIVEN a registered user with email "user@example.com" and password "Password123!"
    AND the user is on the /login page
    WHEN the user enters "user@example.com" in the email field
    AND enters "Password123!" in the password field
    AND clicks the "Sign In" button
    THEN the user is redirected to /dashboard
    AND sees a "Welcome back, Alex!" message in the header
    AND a session cookie "auth_token" is set with httpOnly flag

Scenario: Failed login with incorrect password
    GIVEN a registered user with email "user@example.com"
    AND the user is on the /login page
    WHEN the user enters "user@example.com" in the email field
    AND enters "WrongPassword!" in the password field
    AND clicks the "Sign In" button
    THEN the user remains on the /login page
    AND sees the message "Invalid email or password. Please try again."
    AND no session cookie is created
```

---

### 6. Definition of Done (DoD)

Every Scrum team should have a shared **Definition of Done** — a checklist of quality criteria that every story must meet before being called complete. QA owns and enforces this.

**Example DoD for a software team:**
- [ ] Feature works according to acceptance criteria
- [ ] Unit tests written and all passing (>80% coverage)
- [ ] All QA test cases passed (no open P1 or P2 bugs)
- [ ] Regression tests run and passing
- [ ] Code reviewed and approved by at least 1 peer
- [ ] Feature deployed to staging and smoke tested
- [ ] Test cases updated in test management system
- [ ] API documentation updated (if endpoints changed)
- [ ] Product Owner has accepted the feature

---

### 7. Shift-Left Testing

"Shift-left" means **moving testing activities earlier in the development process** — before code is even written.

```
Traditional:  [Requirements] → [Design] → [Dev] → [TEST] → [Deploy]
                                                    ^
                                               Testing starts here

Shift-Left:   [Requirements] → [Design] → [Dev] → [Test] → [Deploy]
              ^                ^           ^
              QA reviews       QA reviews  QA tests in parallel
              requirements     designs     with development
```

**Why it matters:**
- A bug caught in requirements costs $1 to fix
- The same bug caught in production costs $100+ to fix
- Shift-left prevents defects instead of just finding them

---

## 🛠️ Hands-on Tasks & Activities

| Day | Activity |
|-----|----------|
| **Monday** | Attend (or simulate) Sprint Planning: review 5 user stories, write acceptance criteria for each |
| **Tuesday** | Participate in Daily Standups all week. Write your standup update in the journal before the meeting. |
| **Wednesday** | Write 10 Gherkin scenarios for the Sprint feature; peer review with mentor |
| **Thursday** | Review and organize the sprint backlog in Jira; estimate test effort (hours) for each story |
| **Friday** | Participate in (or write a mock) Sprint Retrospective; compile all deliverables |

---

## 🖥️ Tools & Software

| Tool | Purpose | Cost |
|------|---------|------|
| **Jira Software** | Scrum board, sprint management, backlog refinement | Free tier |
| **Confluence** | Sprint notes, DoD documentation, acceptance criteria | Free tier |
| **Miro** | Retrospective boards (async or real-time) | Free |
| **Cucumber Studio** | Gherkin scenario management | Free trial |

---

## 📚 Recommended Resources

- 📹 "Agile Methodology Explained" — Simplilearn YouTube
- 📹 "Scrum in Under 5 Minutes" — Atlassian YouTube
- 📹 "QA Testing in an Agile/Scrum Environment" — QAFox YouTube
- 📖 **Official:** Scrum Guide 2020 (free PDF) — [scrumguides.org](https://scrumguides.org)
- 📖 "Agile Testing: A Practical Guide" — Lisa Crispin & Janet Gregory (Chapters 1–4)
- 📖 "Writing Good Given/When/Then Scenarios" — cucumber.io/docs
- 🆓 **Free Course:** Agile Testing — LinkedIn Learning (free 1-month trial)

---

## 📝 Deliverables — Due Friday EOD

### Deliverable 1: Gherkin Scenarios (10)
- Well-formatted Given/When/Then scenarios for a Sprint feature
- Must include: at least 4 positive scenarios, at least 4 negative/edge scenarios
- Scenarios should be independently executable (each self-contained)
- Use realistic test data in the scenarios

### Deliverable 2: Acceptance Criteria Document
- Fully written acceptance criteria (in Gherkin or plain text) for 5 user stories
- Each story must have at least 2 scenarios (happy path + at least one failure/edge case)
- Submitted as a Confluence page or Google Doc

### Deliverable 3: Sprint Planning Notes + Standup Journal
- Notes from your Sprint Planning participation (questions asked, stories reviewed, effort estimates)
- Daily standup journal: your prepared update for each of the 5 days this week (use the 3-question format)

### Deliverable 4: Retrospective Reflection (1 page)
Personal retrospective on your own week:
- **What went well** for you this week in your learning and work?
- **What could you improve** — be specific and honest
- **3 concrete action items** you commit to doing differently next week

---

## ✅ Assessment & Feedback Criteria

| Criteria | Excellent (4) | Good (3) | Developing (2) | Needs Work (1) |
|----------|--------------|----------|---------------|----------------|
| **Agile/Scrum knowledge** | All roles, ceremonies, and artifacts explained accurately | Most correct; minor gaps | Basic understanding only | Significant confusion |
| **Gherkin scenario quality** | All scenarios testable, unambiguous, and independently executable | Most are clear | Some ambiguity or interdependency | Not written in Gherkin format |
| **Meeting participation** | Active contributions; asked insightful questions | Engaged and present | Mostly observed | Did not actively participate |
| **Acceptance criteria quality** | Specific, measurable, testable; covers negative cases | Adequate | Vague or missing negative scenarios | Incomplete |

---

## 💼 Real-World Application & Tips

> 🏢 **In real companies:** Being visible and valuable in Scrum ceremonies is one of the fastest ways to build your reputation as a QA engineer. Developers and product owners remember the QA colleague who asked the smart question in Sprint Planning that saved two days of rework.

> 💡 **Pro Tip:** In standups, never just say "I'm testing." Always be specific: "I'm testing Story 42 — I'm 15/20 test cases in, found 2 bugs (TICKET-101 and 102), on track to finish by today 3pm."

> 💡 **Pro Tip:** If a user story reaches you without clear acceptance criteria, do not start testing it. Send it back: "I can't test this without knowing what 'success' looks like. Here's a draft acceptance criteria — can you confirm this is right?" This protects the team from wasted testing effort.

> ⚠️ **Common Mistake:** "That's not my problem to fix." In Agile, QA engineers are part of the team — not a separate gate. If you see a process problem, raise it in the retrospective. The whole team owns quality.

---

*← [Week 4 — Bug Tracking](../Week-4-Bug-Tracking/README.md) | [Week 6 — API Testing →](../Week-6-API-Testing/README.md)*
