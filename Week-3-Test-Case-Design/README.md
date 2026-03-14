# 🟡 Week 3 — Test Case Design & Documentation

> **Week Goal:** Master the art of writing precise, reproducible, and maintainable test cases — the foundational document of any QA process.

---

## 📚 Learning Objectives

By the end of this week, you will be able to:

- [ ] Write well-structured test cases using the industry-standard template
- [ ] Apply test design techniques: **Equivalence Partitioning (EP)**, **Boundary Value Analysis (BVA)**, and **Decision Tables**
- [ ] Create a complete **Test Plan** for a small feature
- [ ] Organize test cases into logical **test suites** by feature and priority
- [ ] Distinguish between **Test Strategy**, **Test Plan**, and **Test Case**

---

## 📖 Key Topics & Theory

### 1. Test Case Anatomy — Every Field Explained

A complete test case contains all of the following fields:

| Field | Description | Example |
|-------|-------------|---------|
| **Test Case ID** | Unique, consistent identifier | `TC_LOGIN_001` |
| **Title / Summary** | Short, specific description of what is tested | "Verify login with valid email and correct password" |
| **Module / Feature** | Where this test belongs | Login, Checkout, User Profile |
| **Priority** | P1 (Critical) → P4 (Low) | P1 |
| **Test Type** | Positive, Negative, Edge Case | Negative |
| **Preconditions** | What must be true before the test | User account exists; app is running; user is logged out |
| **Test Steps** | Numbered, atomic, unambiguous actions | 1. Navigate to `/login`... |
| **Test Data** | The exact inputs to use | `user@test.com` / `Password123!` |
| **Expected Result** | What **should** happen (specific, measurable) | User is redirected to `/dashboard`. "Welcome back, Jane!" is displayed. |
| **Actual Result** | What **actually** happened (filled during execution) | *(leave blank until executing)* |
| **Status** | Outcome of execution | Pass / Fail / Blocked / N/A / Not Run |
| **Notes / Evidence** | Screenshots, logs, video links | `[login_screenshot.png]` |
| **Created By** | Author | Your name |
| **Last Updated** | Date of last revision | 2026-03-15 |

---

### 2. Writing the Expected Result — The Most Common Mistake

The expected result must be **specific, measurable, and observable**. Vague expected results are useless.

| ❌ Bad Expected Result | ✅ Good Expected Result |
|----------------------|------------------------|
| "System should work correctly" | "User is redirected to `/dashboard` and a 'Welcome back, Jane!' message is displayed at the top" |
| "Login should succeed" | "HTTP 200 response is returned; session cookie `auth_token` is set; user name appears in header" |
| "Error is shown" | "A red banner displays: 'Invalid email or password. Please try again.' No account information is revealed." |

**Rule:** If a developer needed to ask you "but what exactly should happen?", your expected result is too vague.

---

### 3. Test Design Techniques

#### Equivalence Partitioning (EP)
Divide the input domain into **partitions** where all values in the partition are expected to behave the same way. Test one representative value from each partition.

**Example — Age field (valid range: 18–100):**

| Partition | Values | Test Value | Expected |
|-----------|--------|-----------|---------|
| Below minimum | < 18 | `17` | Validation error |
| Valid range | 18–100 | `35` | Accepted |
| Above maximum | > 100 | `150` | Validation error |
| Non-numeric | Letters/symbols | `"abc"` | Validation error |

---

#### Boundary Value Analysis (BVA)
Test at the **edges** of partitions — bugs cluster at boundary conditions.

**For a valid range of 1–100:**

| Boundary | Test Values |
|----------|------------|
| Just below minimum | `0` |
| At minimum | `1` |
| Just above minimum | `2` |
| Just below maximum | `99` |
| At maximum | `100` |
| Just above maximum | `101` |

> 💡 Both EP and BVA should usually be applied together for any numeric or range input.

---

#### Decision Table Testing
Use when behavior depends on **combinations of conditions**. List all possible condition combinations and their expected actions.

**Example — Discount eligibility (Member + Purchase > $100):**

| Condition | Test 1 | Test 2 | Test 3 | Test 4 |
|-----------|--------|--------|--------|--------|
| Is a member? | ✅ Yes | ✅ Yes | ❌ No | ❌ No |
| Purchase > $100? | ✅ Yes | ❌ No | ✅ Yes | ❌ No |
| **Expected: Discount Applied?** | **✅ Yes** | **❌ No** | **❌ No** | **❌ No** |

---

#### State Transition Testing
Used when a system moves through different **states** based on actions.

**Example — Order status:**
```
[Pending] → (payment received) → [Processing]
[Processing] → (shipped) → [Shipped]
[Shipped] → (delivered) → [Delivered]
[Any state] → (cancellation) → [Cancelled]
[Delivered] → (return requested) → [Return Pending]
```

Test each valid transition **and** invalid transitions (e.g., can an order jump from Pending to Delivered?).

---

### 4. Test Strategy vs. Test Plan vs. Test Case

| Document | Level | Written By | Answers |
|----------|-------|-----------|---------|
| **Test Strategy** | Organization | QA Lead / Manager | How does QA work here overall? (tools, environments, types, ownership) |
| **Test Plan** | Project | QA Lead | What are we testing on this project? (scope, schedule, resources, risks) |
| **Test Case** | Feature/Scenario | QA Engineer | How exactly do we test this one specific thing? |

---

### 5. Test Suite Organization

Organize your test cases into logical suites:

```
📁 Test Suite: E-Commerce App
  📂 Authentication
    📄 TC_AUTH_001 – Login with valid credentials
    📄 TC_AUTH_002 – Login with incorrect password
    📄 TC_AUTH_003 – Login with unverified email
    📄 TC_AUTH_004 – Password reset flow
  📂 Product Search
    📄 TC_SEARCH_001 – Search by keyword
    📄 TC_SEARCH_002 – Search with no results
  📂 Shopping Cart
    📄 TC_CART_001 – Add item to cart
    📄 TC_CART_002 – Remove item from cart
```

---

## 🛠️ Hands-on Tasks & Activities

**Your mentor will provide:** A set of user stories for a fictional e-commerce application (or a real team feature).

| Day | Activity | Deliverable |
|-----|----------|-------------|
| **Monday** | Analyze 3–4 user stories; brainstorm all test scenarios ("what-ifs") | Scenario list |
| **Tuesday** | Write 20 test cases for Login + Signup using the template | Test case spreadsheet |
| **Wednesday** | Apply BVA and EP to form fields; document your technique explicitly | Technique examples |
| **Thursday** | Organize all test cases into suites in Google Sheets or TestLink | Organized test suite |
| **Friday** | Peer-review a partner's test cases OR self-review using the checklist; compile deliverables | Review form + final submission |

### Test Case Self-Review Checklist
Before submitting your test cases, verify each one against this list:
- [ ] Test Case ID is unique and follows naming convention
- [ ] Title clearly describes what is being tested
- [ ] Priority is assigned
- [ ] Preconditions are explicit (not assumed)
- [ ] Test steps are numbered and atomic (one action per step)
- [ ] Test data uses real values (not "enter valid data")
- [ ] Expected result is specific and measurable
- [ ] At least one negative test case per feature
- [ ] At least one boundary/edge case per input field

---

## 🖥️ Tools & Software

| Tool | Purpose | Cost |
|------|---------|------|
| **Google Sheets** | Test case documentation (see template below) | Free |
| **TestLink** | Open-source test management system | Free / Open-source |
| **Confluence** | Writing Test Plans | Free tier |
| **Miro** | State transition diagrams, mind maps | Free |
| **draw.io** | Decision table / flowchart diagrams | Free |

### Google Sheets Test Case Template
Use the template at [../templates/test-case-template.md](../templates/test-case-template.md) or copy this column structure:

```
Test Case ID | Title | Module | Priority | Type | Preconditions | Steps | Test Data | Expected Result | Actual Result | Status | Notes
```

---

## 📚 Recommended Resources

- 📹 "How to Write Test Cases — Step by Step" — Software Testing Help YouTube
- 📹 "Boundary Value Analysis and Equivalence Partitioning" — ISTQB prep videos
- 📹 "Decision Table Testing Explained" — Guru99 YouTube
- 📖 "Test Design Techniques" — guru99.com/software-testing.html
- 📖 ISTQB Test Case Template — softwaretestinghelp.com (downloadable)
- 🆓 "Test Design Techniques" — uTest Academy — academy.utest.com

---

## 📝 Deliverables — Due Friday EOD

### Deliverable 1: Test Case Suite (Google Sheet)
- Minimum **20 test cases** for Login + Signup features
- All template fields must be filled (empty cells = incomplete)
- Must include: at least 5 positive tests, at least 8 negative tests, at least 4 boundary/edge cases

### Deliverable 2: Technique Demonstration Document
- **3 examples** of Equivalence Partitioning applied to real form fields
- **3 examples** of Boundary Value Analysis applied to real form fields
- One **Decision Table** for a multi-condition scenario
- For each: show the partition/boundary, list the test values, and explain why

### Deliverable 3: Mini Test Plan (1–2 pages)
Use the template at [../templates/test-plan-template.md](../templates/test-plan-template.md):
- Feature/project scope and out-of-scope items
- Testing types to be performed (and why)
- Testing environment details
- Entry criteria (when to start testing)
- Exit criteria (when testing is "done")
- Estimated effort (hours)
- Top 3 risks with mitigation strategies

### Deliverable 4: Peer Review Form
Review one set of test cases (yours or a partner's) using the self-review checklist above. For each checklist item not met, write a specific suggestion for improvement.

---

## ✅ Assessment & Feedback Criteria

| Criteria | Excellent (4) | Good (3) | Developing (2) | Needs Work (1) |
|----------|--------------|----------|---------------|----------------|
| **Test case completeness** | All fields filled; steps unambiguous; zero gaps | Most fields complete; minor omissions | Missing key fields (steps, expected results) | Template barely used |
| **Test coverage** | Positive + negative + boundary + edge cases | Positive + negative | Mostly positive path | Happy path only |
| **Technique application** | EP and BVA correctly and explicitly applied | Partially applied | Attempted but incorrect | Techniques not applied |
| **Test plan quality** | Professional; all sections complete; realistic | Adequate; minor gaps | Several sections missing | Missing key sections |

---

## 💼 Real-World Application & Tips

> 🏢 **In real companies:** Test cases are **living documents** — they must be updated every Sprint as the product evolves. A QA engineer who maintains a clean, well-organized test suite and keeps it up to date after every feature change is extremely valuable to the team.

> 💡 **Pro Tip:** Write test cases for a **stranger** — someone who has never seen the application should be able to follow your steps exactly, with no guesswork, and arrive at the same result you describe. If they'd need to ask you a question, your test case needs more detail.

> ⚠️ **Common Mistake:** Writing "Enter valid data" as a test step. What is valid data? Use real, explicit values: `user@test.com`, `Password123!`, `25`, `1990-01-01`.

> 💡 **Pro Tip:** ID your test cases consistently from day one: `TC_[MODULE]_[NUMBER]`. Consistent naming makes suite management, traceability matrices, and reporting 10x easier.

---

*← [Week 2 — Testing Fundamentals](../Week-2-Testing-Fundamentals/README.md) | [Week 4 — Bug Tracking →](../Week-4-Bug-Tracking/README.md)*
