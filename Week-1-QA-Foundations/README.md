# 🟢 Week 1 — Introduction to Quality Assurance

> **Week Goal:** Build a solid conceptual foundation of what QA is, why it matters, and how it fits into the broader world of software and product development.

---

## 📚 Learning Objectives

By the end of this week, you will be able to:

- [ ] Define Quality Assurance (QA), Quality Control (QC), and Testing — and clearly explain the difference
- [ ] Describe the **cost of poor quality** and cite at least one real-world example of a software bug with major consequences
- [ ] Identify the role of a QA engineer within a cross-functional software team
- [ ] Explain the difference between **Verification** and **Validation**
- [ ] Summarize and apply the **7 Principles of Software Testing** (ISTQB)

---

## 📖 Key Topics & Theory

### 1. What Is Quality?

Quality means a product or service meets its specified requirements **and** satisfies the customer's needs. In software, quality has multiple dimensions:

| Dimension | Question It Answers |
|-----------|---------------------|
| **Functionality** | Does it do what it's supposed to? |
| **Reliability** | Does it work consistently, every time? |
| **Usability** | Is it easy to use? |
| **Performance** | Is it fast enough? |
| **Security** | Is it safe from unauthorized access? |
| **Maintainability** | Can it be updated and fixed easily? |

---

### 2. QA vs. QC vs. Testing

These three terms are often confused. Understand the distinction:

| Term | Definition | Focus | When |
|------|-----------|-------|------|
| **QA (Quality Assurance)** | Process-oriented; prevent defects from occurring | How we *build* it | Throughout the entire SDLC |
| **QC (Quality Control)** | Product-oriented; find defects in what was built | What we *built* | After development |
| **Testing** | Execution-based; verify actual behavior | Does it *work*? | During QC phase |

> 💡 **Analogy:** QA is the food safety regulations and kitchen procedures at a restaurant. QC is the head chef tasting the dish before it goes out. Testing is checking the final plate at the pass.

---

### 3. The Cost of Poor Quality

Defects cost far more to fix the later they are discovered:

```
Requirements  →  Design  →  Development  →  Testing  →  Production
    $1             $5           $10            $50         $100+
           Cost to fix a defect increases at each stage
```

**Famous Examples:**

| Incident | Year | Bug | Cost |
|----------|------|-----|------|
| Therac-25 Radiation Machine | 1985–1987 | Race condition caused massive overdoses | 6 patient deaths |
| Ariane 5 Rocket | 1996 | Integer overflow in guidance code | $370M rocket self-destructed |
| Knight Capital | 2012 | Deprecated trading code accidentally reactivated | $440M lost in 45 minutes |
| Mars Climate Orbiter | 1999 | Metric vs. imperial unit mismatch | $327M spacecraft lost |

---

### 4. The 7 Principles of Software Testing (ISTQB)

1. **Testing shows the presence of defects, not their absence**
   → Testing reduces risk; it cannot prove zero bugs exist.

2. **Exhaustive testing is impossible**
   → Test based on risk and priority; focus on what matters most.

3. **Early testing saves time and money (Shift-Left)**
   → Start QA activity during requirements — not after development.

4. **Defects cluster together (Pareto Principle)**
   → 80% of bugs are typically found in 20% of modules.

5. **The Pesticide Paradox**
   → Running the same tests repeatedly stops finding new bugs. Refresh your test suite.

6. **Testing is context-dependent**
   → Testing a medical device is very different from testing a social media feed.

7. **Absence-of-errors fallacy**
   → A completely bug-free product can still be a failure if it doesn't meet user needs.

---

### 5. Verification vs. Validation

| | **Verification** | **Validation** |
|-|-----------------|---------------|
| **Question** | "Are we building the product *right*?" | "Are we building the *right* product?" |
| **Focus** | Process; does it match specifications? | Customer; does it meet actual user needs? |
| **How** | Reviews, inspections, walkthroughs | User testing, UAT, demos |
| **Example** | Code review checks logic matches design doc | End user confirms the feature is actually useful |

---

### 6. The Role of a QA Engineer on a Software Team

A QA engineer wears many hats throughout a project:

| Phase | QA Responsibilities |
|-------|---------------------|
| Requirements | Review requirements; flag ambiguities; ask "how will we test this?" |
| Design | Review UI/UX designs; identify testability concerns |
| Development | Write test cases; prepare test data and environments |
| Testing | Execute tests; log defects; report status daily |
| Release | Sign off on release quality; execute regression suite |
| Post-release | Monitor production defects; update regression suite |

---

## 🛠️ Hands-on Tasks & Activities

### Daily Schedule

| Day | Activity | Time Estimate |
|-----|----------|---------------|
| **Monday** | Read 3 bug case studies (Therac-25, Ariane 5, Knight Capital); write a reflection | 3–4 hrs |
| **Tuesday** | Conduct an interview with a team QA engineer (prepare 5+ questions in advance); document answers | 2–3 hrs + interview |
| **Wednesday** | Explore the team's staging app as a user; write down 10 quality observations | 2–3 hrs |
| **Thursday** | Map out the team's SDLC; create a diagram showing where QA fits in each phase | 3–4 hrs |
| **Friday** | Compile all deliverables; self-review; submit by EOD | 4–5 hrs |

### Interview Question Guide (for Tuesday)
Prepare at least 5 questions from this list before the interview:

1. What does a typical day look like for you as a QA engineer?
2. What's the most critical bug you've ever found? How did you find it?
3. How does your team decide what to test vs. what to automate?
4. What do you wish you'd known when you first started in QA?
5. How do you balance speed (sprint timelines) with quality (thorough testing)?
6. What's the biggest quality challenge your team faces right now?
7. What does a "good QA engineer" look like to you?

---

## 🖥️ Tools & Software to Learn This Week

| Tool | Purpose | Cost | Setup Link |
|------|---------|------|-----------|
| **Google Docs** | Write reflections and deliverables | Free | docs.google.com |
| **draw.io (diagrams.net)** | SDLC diagrams | Free | diagrams.net |
| **Trello** | Personal task tracking (optional) | Free | trello.com |
| **Jira** (read-only) | Explore team's existing issues | Free tier | atlassian.com |

---

## 📚 Recommended Resources

### Videos (Watch This Week)
- 📹 "What is Software Testing?" — Guru99 YouTube (~15 min)
- 📹 "QA vs QC vs Testing — Key Differences Explained" — Simplilearn YouTube
- 📹 "7 Principles of Software Testing" — ISTQB Foundation Level YouTube

### Reading
- 📖 **ISTQB Glossary** — [glossary.istqb.org](https://glossary.istqb.org) (review first 30 terms)
- 📖 **Article:** "The 7 Principles of Software Testing" — softwaretestinghelp.com
- 📖 **Article:** "What is QA?" — guru99.com/software-testing.html
- 📰 **Case Study:** "Software Horror Stories" — theregister.com

### Book (Optional but Recommended)
- 📘 *"Lessons Learned in Software Testing"* — Kaner, Bach, Pettichord (Chapter 1)

---

## 📝 Deliverables — Due Friday EOD

Submit all 4 deliverables to your mentor via Google Doc share or Confluence page.

### Deliverable 1: QA Concept Summary
**Length:** ~500 words
**Format:** Google Doc
**Content:**
- In your own words: what is QA? why does it matter?
- Explain the difference between QA, QC, and Testing
- Explain the difference between Verification and Validation

### Deliverable 2: Bug Case Study Analysis
**Length:** ~1 page
**Format:** Google Doc
**Content:**
- Choose one: Ariane 5, Knight Capital, Therac-25, or Mars Orbiter
- What happened? What was the root cause?
- How could QA have prevented or minimized this?
- Personal reflection: what does this teach you about the importance of QA?

### Deliverable 3: Team Interview Notes
**Format:** Structured notes document
**Content:**
- List of your 5+ prepared questions
- Answers as noted during interview
- 2–3 key takeaways from the conversation

### Deliverable 4: SDLC Diagram
**Format:** draw.io diagram (exported as PNG or PDF)
**Content:**
- Diagram showing all SDLC phases (requirements → design → dev → test → deploy → maintain)
- QA activities labeled at each phase
- One sentence description of QA's role at each stage

---

## ✅ Assessment & Feedback Criteria

| Criteria | Excellent (4) | Good (3) | Developing (2) | Needs Work (1) |
|----------|--------------|----------|---------------|----------------|
| **Conceptual accuracy** | All definitions precise and correct | Most correct; minor errors | Some inaccuracies | Significant gaps or confusion |
| **Written clarity** | Well-structured, clear, no errors | Mostly clear; minor issues | Some confusion or poor organization | Hard to follow |
| **Critical thinking** | Insightful analysis; real implications drawn | Solid analysis | Surface-level observations | Minimal effort |
| **Completeness** | All 4 deliverables submitted in full | 3 of 4 complete | 2 of 4 submitted | Fewer than 2 submitted |

**Scoring:** Each criterion is worth 4 points. Max = 16 points. Target: ≥ 12 points.

---

## 💼 Real-World Application & Tips

> 🏢 **In real companies:** QA engineers are involved from the very beginning of a project — reviewing requirements documents, attending sprint planning, and asking "what could go wrong?" before a single line of code is written. The earlier a defect is caught, the cheaper it is to fix.

> 💡 **Pro Tip:** The best QA engineers are **curious by nature**. Train yourself to ask "But what if the user does X instead?" about everything you encounter. That instinct is the core of what makes a great tester.

> ⚠️ **Common Mistake:** Many beginners confuse "testing" with "QA." Remember: Testing finds bugs. QA builds the *systems* that prevent bugs from happening in the first place.

> 📌 **Mentor Note:** This week is heavily conceptual — that's intentional. Strong foundational knowledge prevents expensive misconceptions later. Don't rush; make sure the intern can explain these concepts in their own words before moving on.

---

*← [Week 0 — Onboarding](../Week-00-Onboarding/README.md) | [Week 2 — Testing Fundamentals →](../Week-2-Testing-Fundamentals/README.md)*
