# 🏭 Week 7 — Quality Standards, Process Improvement & General QA

> **Week Goal:** Understand the broader discipline of Quality Management — covering ISO standards, PDCA, Six Sigma basics, and quality metrics — applicable to both software and manufacturing QA.

---

## 📚 Learning Objectives

By the end of this week, you will be able to:

- [ ] Explain **ISO 9001** quality management principles and how they apply to a software team
- [ ] Describe the **ISO/IEC 25010** software quality model and its 8 characteristics
- [ ] Use the **PDCA cycle** to propose and measure a process improvement
- [ ] Apply **Six Sigma DMAIC** methodology to a quality problem
- [ ] Build a **quality metrics dashboard** and interpret defect density, escape rate, and pass rate

---

## 📖 Key Topics & Theory

### 1. ISO 9001 — Quality Management Systems (QMS)

ISO 9001 is the world's most recognized standard for **Quality Management Systems**. It describes *what* a quality system should achieve, not *how* to do it. Over 1 million organizations worldwide are certified.

**7 Quality Management Principles of ISO 9001:**

| # | Principle | Meaning for a Software QA Team |
|---|-----------|-------------------------------|
| 1 | **Customer Focus** | Every QA decision should trace back to what the customer actually needs |
| 2 | **Leadership** | QA leadership creates an environment where quality is everyone's responsibility |
| 3 | **Engagement of People** | QA engineers at every level contribute to quality improvement |
| 4 | **Process Approach** | QA activities are managed as interconnected processes, not isolated tasks |
| 5 | **Improvement** | Continuous improvement is a permanent objective (retrospectives, metrics review) |
| 6 | **Evidence-based Decisions** | Quality decisions are made using data (metrics, defect reports) — not gut feeling |
| 7 | **Relationship Management** | QA builds strong relationships with dev, product, and operations teams |

**For software teams, ISO 9001 requires:**
- Documented processes (test plans, bug workflows, release checklists)
- Defined roles and responsibilities
- Controlled changes (change management, version control)
- Regular internal audits and management reviews
- Continuous improvement cycles

---

### 2. ISO/IEC 25010 — Software Quality Model

This standard defines 8 main **software product quality characteristics** — the complete framework for what "quality software" looks like:

| Characteristic | What It Means | QA Tests For |
|---------------|--------------|-------------|
| **Functional Suitability** | Does it do what it's supposed to? | Functional test cases |
| **Performance Efficiency** | Is it fast enough? Does it scale? | Load/performance tests |
| **Compatibility** | Works with other systems and environments? | Cross-browser, integration tests |
| **Usability** | Easy to use? Learnable? Accessible? | UX testing, accessibility audits |
| **Reliability** | Works consistently? Recovers from failures? | Stress tests, fault injection |
| **Security** | Safe from unauthorized access and attacks? | Security testing, OWASP checklist |
| **Maintainability** | Can it be modified and understood easily? | Code reviews, static analysis |
| **Portability** | Can it run in different environments? | Environment/platform testing |

> 💡 Use this model as a **test planning checklist**. For any feature or release, ask: have we tested all 8 dimensions that apply?

---

### 3. PDCA Cycle — Plan-Do-Check-Act

The PDCA cycle is the foundation of continuous quality improvement. It is used in manufacturing, software, healthcare, and every industry.

```
        ┌──────── PLAN ────────┐
        │ Define the problem    │
        │ Set measurable goal   │
        │ Identify root cause   │
        │ Design solution       │
        └──────────────────────┘
               ↑              ↓
           ACT               DO
    ┌──────────────┐   ┌───────────────┐
    │ Standardize  │   │ Implement the │
    │ if improved  │   │ solution on a │
    │ OR revise    │   │ small scale   │
    │ and retry    │   │               │
    └──────────────┘   └───────────────┘
               ↑              ↓
        ┌──────── CHECK ───────┐
        │ Measure results       │
        │ Compare to goal       │
        │ Analyze what happened │
        └──────────────────────┘
```

**Example Applied to QA:**

| Phase | What We Did |
|-------|------------|
| **Plan** | Problem: 15% of bugs escape to production. Goal: Reduce to < 5%. Root cause: no mandatory code review for hotfixes. Solution: add code review to hotfix workflow |
| **Do** | Implemented mandatory code review for hotfixes over 2 Sprints |
| **Check** | Measured escape rate: dropped from 15% to 6% |
| **Act** | Not quite at 5% goal. Add pre-deploy smoke tests and repeat cycle |

---

### 4. Six Sigma — DMAIC Framework

Six Sigma is a data-driven methodology for eliminating defects. The goal is to achieve processes with fewer than **3.4 defects per million opportunities**.

**DMAIC — The Core Six Sigma Improvement Methodology:**

| Phase | Key Question | Tools Used |
|-------|-------------|-----------|
| **D — Define** | What's the problem and what does success look like? | Project charter, Voice of Customer (VOC), SIPOC diagram |
| **M — Measure** | How bad is the problem right now? | Process maps, data collection plans, Pareto charts |
| **A — Analyze** | Why is the problem occurring? | Fishbone diagram, 5 Whys, root cause analysis |
| **I — Improve** | What's the best solution? | Pilot testing, design of experiments |
| **C — Control** | How do we make sure the improvement sticks? | Control charts, SOPs, monitoring dashboards |

---

### 5. Root Cause Analysis Tools

#### Fishbone (Ishikawa) Diagram
Visualize all potential causes of a problem organized into categories:

```
                              ┌─────────────────────────────────── EFFECT
  Machines/Tools ────────────►│
                              │
  Methods/Process ───────────►│   "High defect escape rate
                              │    to production"
  Materials/Requirements ────►│
                              │
  People/Skills ─────────────►│
                              │
  Environment ───────────────►│
                              │
  Measurement/Data ──────────►│
                              └─────────────────────────────────────────
```

For each "bone," brainstorm 3–5 contributing causes.

#### Pareto Analysis (80/20 Rule)
Create a Pareto chart to identify which defect causes are responsible for the most defects:

| Defect Type | Count | % of Total | Cumulative % |
|------------|-------|-----------|-------------|
| Missing input validation | 45 | 37.5% | 37.5% |
| Integration errors | 32 | 26.7% | 64.2% |
| UI/display issues | 22 | 18.3% | 82.5% |
| Performance issues | 12 | 10.0% | 92.5% |
| Security gaps | 9 | 7.5% | 100% |

> 💡 Focus improvement efforts on the top 2–3 categories (representing ~80% of defects) first.

---

### 6. Quality Metrics — What to Measure

| Metric | Formula | What Good Looks Like |
|--------|---------|---------------------|
| **Defect Density** | Total bugs ÷ Lines of code (per 1000) | Lower is better |
| **Defect Escape Rate** | Bugs found in production ÷ Total bugs found × 100% | Target: < 5% |
| **Test Coverage** | Test cases executed ÷ Total test cases × 100% | Target: > 90% |
| **Test Pass Rate** | Tests passed ÷ Tests executed × 100% | Target: > 95% before release |
| **Mean Time to Detect (MTTD)** | Average time from bug introduction to discovery | Lower is better |
| **Defect Removal Efficiency (DRE)** | Bugs found before release ÷ Total bugs (pre + post) × 100% | Target: > 95% |
| **Cost of Quality** | Cost of prevention + appraisal + internal failure + external failure | Track trend over time |

**Calculate your team's metrics using this formula:**
```
Example Sprint Data:
  - Total test cases: 150
  - Test cases executed: 140
  - Tests passed: 128
  - Bugs found in testing: 22
  - Bugs found in production: 3

Test Coverage    = 140/150 × 100 = 93.3%
Test Pass Rate   = 128/140 × 100 = 91.4%
Defect Escape Rate = 3/(22+3) × 100 = 12% ← Too high! Needs investigation
DRE              = 22/(22+3) × 100 = 88% ← Below target of 95%
```

---

## 🛠️ Hands-on Tasks & Activities

| Day | Activity |
|-----|----------|
| **Monday** | Research one ISO 9001–certified company; present how their QMS works (1-page write-up OR 10-min presentation) |
| **Tuesday** | Apply PDCA to improving one real or simulated QA process; write all 4 phases |
| **Wednesday** | Create a Fishbone diagram for a complex bug from a case study (provided by mentor) |
| **Thursday** | Calculate 5 quality metrics from provided Sprint data; build a Pareto chart in Google Sheets |
| **Friday** | DMAIC mini-project: work through all 5 phases for a simulated quality problem; compile all deliverables |

### Data Set for Metrics Exercise (Thursday)
Your mentor will provide a spreadsheet with this data (or use this sample):

| Sprint | Tests Run | Tests Passed | Bugs in Testing | Bugs in Production |
|--------|-----------|-------------|----------------|-------------------|
| Sprint 1 | 80 | 72 | 15 | 4 |
| Sprint 2 | 95 | 87 | 12 | 2 |
| Sprint 3 | 110 | 105 | 8 | 1 |

Calculate: Test Pass Rate, Defect Escape Rate, and DRE for each Sprint. Identify trends.

---

## 🖥️ Tools & Software

| Tool | Purpose | Cost |
|------|---------|------|
| **Google Sheets / Excel** | Quality metrics, Pareto charts | Free |
| **Lucidchart / draw.io** | Fishbone diagrams, process maps, SIPOC | Free |
| **Minitab** | Statistical analysis, control charts | 30-day trial |
| **Google Data Studio / Looker** | Metrics dashboards | Free |

### Creating a Pareto Chart in Google Sheets
1. Enter your defect category data in two columns (category, count)
2. Sort descending by count
3. Add a cumulative % column
4. Insert → Chart → Combo chart
5. Bar series: defect counts; Line series: cumulative %
6. Add a horizontal reference line at 80% to identify the "vital few"

---

## 📚 Recommended Resources

- 📹 "ISO 9001:2015 — What It Is and Why It Matters" — Advisera YouTube
- 📹 "Six Sigma DMAIC in 9 Minutes" — IASSC YouTube
- 📹 "PDCA Cycle Explained with Examples" — Juran Institute YouTube
- 📹 "Fishbone Diagram Tutorial" — MindTools YouTube
- 📖 "Root Cause Analysis Methods" — [asq.org](https://asq.org/quality-resources/root-cause-analysis)
- 📖 "Key Software Quality Metrics" — guru99.com
- 🆓 "Introduction to Six Sigma" — Coursera (audit free, University of… multiple options)
- 📘 *"The Lean Six Sigma Pocket Toolbook"* — George, Rowlands, Price, Maxey (excellent reference)
- 🆓 Free Resources: ASQ.org — free quality tools, templates, and articles

---

## 📝 Deliverables — Due Friday EOD

### Deliverable 1: ISO/PDCA Report (1–2 pages)
- Part A: Explain 3 ISO 9001 principles and give a concrete example of how each applies to your current team/internship
- Part B: Propose a complete PDCA improvement cycle for one real QA process you've observed (all 4 phases fully written out; include how you would measure success)

### Deliverable 2: Fishbone Diagram
- Completed Fishbone diagram for the provided case study problem
- At least 4 "bones" with 3+ contributing causes each
- Root causes circled/highlighted
- Top 2 recommended areas to investigate further

### Deliverable 3: Quality Metrics Dashboard (Google Sheet)
- 5+ metrics calculated from the provided Sprint data
- Charts: trend lines for pass rate and escape rate over time; one Pareto chart
- Written interpretation: what story does the data tell? what action would you recommend?

### Deliverable 4: DMAIC Mini-Report (1 page)
Work through a provided (or real) quality problem:
- **D:** Problem statement, goal, key stakeholders
- **M:** Current state data, how you would measure
- **A:** Root causes identified (use Fishbone + 5 Whys)
- **I:** Proposed solution with expected impact
- **C:** How you would sustain the improvement (monitoring plan)

---

## ✅ Assessment & Feedback Criteria

| Criteria | Excellent (4) | Good (3) | Developing (2) | Needs Work (1) |
|----------|--------------|----------|---------------|----------------|
| **Standards knowledge** | ISO + Six Sigma correctly applied with specific examples | Generally correct, minor gaps | Some confusion or misapplication | Significant knowledge gaps |
| **Root cause analysis** | Multi-level, insightful; reached process-level root cause | Adequate analysis | Surface level; stopped at symptoms | Not meaningfully completed |
| **Metrics accuracy** | All calculations correct; trends identified; actionable insights | Most correct | Some calculation errors | Formulas incorrect |
| **DMAIC application** | Thorough, practical, data-driven through all phases | Adequate | 1–2 phases incomplete | Not completed |

---

## 💼 Real-World Application & Tips

> 🏢 **In real companies:** QA is not just about finding bugs — it's about building **systems that prevent bugs**. The most senior QA engineers don't just run test cases; they look at the process, measure what's wrong, and propose changes that improve quality permanently. That's the Six Sigma mindset.

> 💡 **Pro Tip:** Every time a critical bug escapes to production, treat it as a **process failure**, not a human failure. Ask: "What process could we add or improve so that this physically cannot slip through again?" That question transforms your team's quality culture.

> 💡 **Pro Tip:** Learn to read a defect trend chart. If your defect escape rate is consistently above 10%, that's a signal — not bad luck. Data tells stories. Learn to listen.

---

*← [Week 6 — API Testing](../Week-6-API-Testing/README.md) | [Week 8 — Test Automation →](../Week-8-Test-Automation/README.md)*
