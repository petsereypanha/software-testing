## Test Case Template
### How to Use
Copy the table below into a new Google Sheet or Confluence page.
One row = one test case.
**Never leave "Test Steps", "Test Data", or "Expected Result" blank.**

---

| Field | Value |
|-------|-------|
| **Test Case ID** | TC_[MODULE]_[NUMBER] (e.g., TC_LOGIN_001) |
| **Title** | Short, specific: "Verify [action] when [condition]" |
| **Module / Feature** | Login / Checkout / Profile / etc. |
| **Priority** | P1 (Critical) / P2 (High) / P3 (Medium) / P4 (Low) |
| **Test Type** | Positive / Negative / Edge Case / Boundary |
| **Technique Used** | EP / BVA / Decision Table / State Transition / Exploratory |
| **Preconditions** | All conditions that must be true BEFORE this test runs |
| **Test Steps** | (See numbered steps below) |
| **Test Data** | Exact, specific values — NEVER "enter valid data" |
| **Expected Result** | Specific, measurable, observable outcome |
| **Actual Result** | (Fill during test execution) |
| **Status** | Pass / Fail / Blocked / N/A / Not Run |
| **Notes / Evidence** | Screenshot link, Jira ticket, video link |
| **Created By** | Your name |
| **Date Created** | YYYY-MM-DD |
| **Last Updated** | YYYY-MM-DD |

---

## Test Steps Format
Steps must be:
- **Numbered** (1, 2, 3...)
- **Atomic** (one action per step)
- **Unambiguous** (a stranger could follow them exactly)

**Example (Good):**
```
1. Open Chrome browser and navigate to https://staging.example.com/login
2. Wait for the login page to fully load
3. Click in the "Email" field
4. Type: user@test.com
5. Click in the "Password" field
6. Type: Password123!
7. Click the "Sign In" button
8. Observe the result
```

**Example (Bad):**
```
1. Go to the login page and try to log in with valid credentials
2. See what happens
```

---

## Expected Result Format — The 3 Questions Rule
A good expected result answers **all 3 questions**:
1. **Where** are you after the action? (URL, page, modal)
2. **What do you see?** (specific text, element, state)
3. **What happened behind the scenes?** (status code, cookie set, email sent?)

**Example:**
> "User is redirected to `https://staging.example.com/dashboard`.
> The header displays 'Welcome back, Jane Smith!'
> A session cookie named `auth_token` is set with the `HttpOnly` flag.
> The browser title changes to 'Dashboard — MyApp'."

---

## Test Case Example

| Field | Value |
|-------|-------|
| **Test Case ID** | TC_LOGIN_001 |
| **Title** | Verify login with valid email and correct password |
| **Module** | Authentication |
| **Priority** | P1 |
| **Test Type** | Positive |
| **Technique** | N/A (standard positive scenario) |
| **Preconditions** | 1. A user account exists with email `qa_test@example.com` and password `Password123!` 2. The account email is verified 3. The user is NOT currently logged in 4. Browser: Chrome latest, staging environment v2.4.1 |
| **Test Steps** | 1. Navigate to https://staging.example.com/login 2. Enter `qa_test@example.com` in the Email field 3. Enter `Password123!` in the Password field 4. Click the "Sign In" button |
| **Test Data** | Email: `qa_test@example.com` / Password: `Password123!` |
| **Expected Result** | 1. User is redirected to `/dashboard` 2. Header shows "Welcome back, QA Test!" 3. Auth session cookie is created 4. The back button does not return to login page (session maintained) |
| **Actual Result** | *(Fill during execution)* |
| **Status** | Not Run |
| **Notes** | TC-001 in regression smoke suite |
| **Created By** | [Your name] |
| **Date Created** | 2026-03-15 |

---

## Test Suite Template (Google Sheets Column Headers)

Copy this as the header row in your test case spreadsheet:

```
Test Case ID | Title | Module | Priority | Test Type | Preconditions | Test Steps | Test Data | Expected Result | Actual Result | Status | Bug ID (if failed) | Notes | Created By | Last Updated
```
