# 🏆 Week 10 — Capstone Project & Career Readiness

> **Week Goal:** Synthesize all 10 weeks of learning into a comprehensive, real-world QA capstone project — and prepare yourself for a professional QA career.

---

## 📚 Learning Objectives

By the end of this week, you will be able to:

- [ ] Execute a **complete quality assurance cycle** independently on a real or realistic application
- [ ] Produce professional-grade QA artifacts: test plan, test cases, bug reports, automation, API tests, metrics
- [ ] Deliver a **15–20 minute professional presentation** to stakeholders
- [ ] Confidently discuss your QA experience in a **simulated job interview**
- [ ] Identify your strengths, gaps, and continued learning path in QA

---

## 🎯 Capstone Project Options

Choose one option in agreement with your mentor:

| Option | Application | Notes |
|--------|------------|-------|
| **Option A** (Preferred) | Company's internal staging environment or upcoming Sprint feature | Most realistic; most valuable to the team |
| **Option B** | [SauceDemo](https://www.saucedemo.com) or [OpenCart Demo](https://demo.opencart.com/) | Publicly available; good for full coverage |
| **Option C** | Personal portfolio app or approved open-source project | Requires mentor approval; must have explicit authorization |

---

## 📦 Required Deliverables (All 7 Must Be Completed)

### Deliverable 1: Test Plan Document (3–5 pages)
Use the template at [../templates/test-plan-template.md](../templates/test-plan-template.md)

**Must include:**
- [ ] Project name, version, application under test
- [ ] Scope: features **in** scope and features **out** of scope (with justification)
- [ ] Testing types to be performed and rationale for each
- [ ] Test environment details (OS, browser, app version, URLs)
- [ ] Entry criteria (conditions that must be met before testing begins)
- [ ] Exit criteria (conditions that must be met for testing to be considered complete)
- [ ] Risk assessment table (minimum 5 risks: description, likelihood, impact, mitigation)
- [ ] Test schedule (which tests run on which days)
- [ ] Resources needed

---

### Deliverable 2: Test Case Suite (Minimum 50 Test Cases)
Use the template at [../templates/test-case-template.md](../templates/test-case-template.md)

**Must include:**
- [ ] Organized into logical test suites by feature/module
- [ ] Proper coverage: positive, negative, edge cases, boundary values
- [ ] Test design techniques applied (label which technique was used per case)
- [ ] All test cases executed (Actual Result + Status filled in)
- [ ] Coverage breakdown by feature and type included in a summary table

**Coverage Targets:**
| Type | Minimum % |
|------|----------|
| Positive (happy path) | 30% |
| Negative / error cases | 40% |
| Boundary / edge cases | 20% |
| Exploratory findings | 10% |

---

### Deliverable 3: Bug Report Portfolio (Minimum 10 Bugs)
All bugs logged in Jira with fully completed fields.

**Must include:**
- [ ] Minimum 2 **Critical or Major** severity bugs
- [ ] At least 3 bugs with **video reproduction** (Loom link attached in Jira)
- [ ] Full bug lifecycle demonstrated for at least 3 bugs (New → Assigned → Fixed → Closed or Reopened)
- [ ] Severity/Priority correctly assigned with justification
- [ ] Screenshot/evidence for every bug

---

### Deliverable 4: Automated Test Suite
Extend your Week 8 project OR create a new one for this capstone application.

**Must include:**
- [ ] Minimum **15 automated test cases** using Selenium + Python
- [ ] Page Object Model implemented (minimum 3 page classes)
- [ ] Tests run with pytest; HTML report generated
- [ ] All tests passing (or failing tests documented with known-issue labels)
- [ ] GitHub repository with clear README.md
- [ ] CI pipeline (GitHub Actions) running on push
- [ ] Test report uploaded as CI artifact

---

### Deliverable 5: API Test Collection
If the application has an API (or use a related public API):

**Must include:**
- [ ] Postman collection with minimum 20 requests
- [ ] All 4 CRUD operations covered + authentication + error scenarios
- [ ] Test scripts: minimum 15 assertions
- [ ] Newman run completed; HTML report exported
- [ ] Exported collection committed to GitHub

---

### Deliverable 6: Quality Metrics Report
**Must include:**
- [ ] Test execution metrics for the full capstone run:
  - Total test cases, executed, passed, failed, blocked
  - Pass rate %
  - Defect density (bugs per major feature)
  - Defect escape rate (if any production defects found)
- [ ] Defect distribution chart by severity and by module (Pareto chart)
- [ ] Performance test results (at least one load test with 50+ virtual users)
- [ ] Lighthouse scores for the application (4 categories)
- [ ] Written interpretation: what is the overall quality status? Is it ready to release?

---

### Deliverable 7: Final Presentation (15–20 minutes)

Deliver this presentation to your mentor, team, or stakeholders on Friday of Week 10.

**Presentation Structure:**

| Section | Time | Content |
|---------|------|---------|
| **Introduction** | 1 min | Your name, the application tested, and the scope |
| **Testing Approach** | 3 min | Your test plan: what you tested, what you skipped, why |
| **Key Findings** | 3 min | Top 3 bugs found; show Jira tickets and video evidence |
| **Automation Demo** | 3 min | Live run (or recording) of your Selenium test suite |
| **Quality Dashboard** | 2 min | Show your metrics: pass rate, defect distribution, performance results |
| **Lessons Learned** | 2 min | What you learned during these 10 weeks; what surprised you |
| **Q&A** | 5 min | Answer questions from the audience |

**Presentation Tips:**
- Use slides (Google Slides, PowerPoint, or Notion)
- Have Jira board open as a live demonstration
- Have a terminal ready for the automation demo
- Prepare for these questions:
  - "Why did you choose these 50 test cases?"
  - "How did you decide what to automate vs. what to test manually?"
  - "If you had 2 more weeks, what would you test next?"
  - "What was the most interesting bug you found?"

---

## 📅 Week 10 Daily Schedule

| Day | Morning (9am–1pm) | Afternoon (2pm–6pm) |
|-----|-------------------|---------------------|
| **Monday** | Final test execution; close and verify all open test cases | Complete automation suite; push final CI run |
| **Tuesday** | Finalize API collection; export Newman report | Start quality metrics report; gather all data |
| **Wednesday** | Build quality dashboard (charts, metrics, Pareto); write report | Draft presentation slides |
| **Thursday** | Refine presentation; mentor dry-run rehearsal | Incorporate feedback; prepare demo environment |
| **Friday** | Final preparation; dry-run solo | **FINAL PRESENTATION** to team/stakeholders |

---

## 🎤 Post-Presentation Job Interview Simulation

After the presentation, your mentor will conduct a 15-minute mock interview. Prepare answers for:

**Technical Questions:**
- Walk me through how you would test a new user registration feature from scratch.
- What's the difference between severity and priority? Give me a real example.
- How do you decide what test cases to add to your regression suite?
- You've found a critical bug 30 minutes before a release. What do you do?
- Explain the Page Object Model — why do we use it?
- What's the difference between load testing and stress testing?
- How does Agile/Scrum change the way QA works vs. Waterfall?

**Behavioral Questions:**
- Tell me about a challenging bug you found during this internship.
- Describe a time you had a disagreement with a team member about whether something was a bug.
- How do you handle testing pressure under tight deadlines?
- What's the biggest lesson you learned during these 10 weeks?

**Questions to Ask Your Interviewer (the Mentor):**
- What does the QA team's biggest quality challenge look like right now?
- How does the team measure QA effectiveness?
- What does the career growth path look like for a QA engineer here?

---

## 📚 Career Readiness Resources

- 📖 "How to Build a QA Portfolio on GitHub" — testingmind.com
- 📹 "Top 50 QA Testing Interview Questions" — SDET-QA YouTube
- 📖 ISTQB Foundation Level Syllabus (free PDF) — [istqb.org](https://www.istqb.org)
- 🆓 **Free Certification:** Postman Student Expert — [postman.com/student-expert](https://www.postman.com/student-expert/)
- 🆓 **Free Certification:** Atlassian Jira Fundamentals — [university.atlassian.com](https://university.atlassian.com)
- 🆓 **Free Certification:** OWASP Top 10 fundamentals — OWASP Training resources
- 📱 **Community:** Ministry of Testing — [ministryoftesting.com](https://www.ministryoftesting.com) (largest QA community)
- 📱 **Community:** r/QualityAssurance — reddit.com/r/QualityAssurance

---

## 🗺️ Your Continued Learning Path After This Internship

| Interest | Next Steps |
|----------|-----------|
| **Test Automation** | Learn Cypress or Playwright; learn Java + TestNG; get ISTQB certification |
| **API Testing** | Learn REST Assured (Java); explore GraphQL testing; try Karate framework |
| **Performance Testing** | Deep-dive JMeter; learn k6 scripting; study AWS/Azure load testing |
| **Security Testing** | PortSwigger Academy (free); OWASP Security Testing Guide; learn Burp Suite |
| **QA Leadership** | ISTQB Advanced Level; learn QA metrics and reporting; study risk-based testing |
| **DevOps / Quality Engineering** | Learn CI/CD (GitHub Actions, Jenkins); containerization basics (Docker); monitoring (Grafana) |

---

## ✅ Final Assessment

See the full rubric at [../evaluation/rubric.md](../evaluation/rubric.md)

| Category | Max Points |
|----------|-----------|
| Technical Skills (all tools and concepts) | 50 |
| Soft Skills (communication, teamwork) | 30 |
| Capstone Project (all 7 deliverables) | 20 |
| **Total** | **100** |

**Minimum passing score: 70/100**

---

## 💼 Real-World Application & Tips

> 🏢 **In real companies:** Your capstone project is essentially your QA portfolio. Many companies will ask: "What experience do you have testing real applications?" Having a GitHub repository with a working automation suite, a documented test plan, and a professional bug report portfolio sets you apart from 90% of applicants at the junior level.

> 💡 **Pro Tip:** Ask your mentor for a LinkedIn recommendation focused specifically on your technical growth — what you could do on Day 1 vs. Day 70. Specificity in recommendations is far more valuable than generic praise.

> 💡 **Pro Tip:** Keep all your artifacts. Your test plans, bug reports, and automation code are your portfolio. Clean them up, put them on GitHub, and link to them on your resume and LinkedIn.

---

*← [Week 9 — Advanced QA](../Week-9-Advanced-QA/README.md)*
