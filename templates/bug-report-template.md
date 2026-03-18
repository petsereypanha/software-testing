# Bug Report Template

> Use this template for every bug you log — in Jira, GitHub Issues, or any other tracker.
> A bug report is only as good as its clarity. A developer should be able to fix the bug using ONLY your report.

---

## Quick Reference: Bug Report Fields

| Field | Required? | Guidance |
|-------|-----------|---------|
| **Title** | ✅ | Specific, searchable; include: WHAT fails + WHEN + WHERE |
| **Environment** | ✅ | OS, browser + version, app version, environment (staging/prod) |
| **Steps to Reproduce** | ✅ | Numbered, atomic, reproducible by a stranger |
| **Expected Result** | ✅ | What SHOULD happen per spec/requirement |
| **Actual Result** | ✅ | What ACTUALLY happens — be specific |
| **Severity** | ✅ | Critical / Major / Minor / Trivial |
| **Priority** | ✅ | P1–P4 (set with Product Owner if needed) |
| **Reproducibility** | ✅ | Always / Intermittent (X% of attempts) / Only once |
| **Attachments** | ✅ | Screenshot minimum; video preferred for UI bugs |
| **Test Data Used** | ✅ | Exact data that triggered the bug |
| **Related Test Case** | Recommended | TC_LOGIN_002, etc. |
| **Assigned To** | When known | Developer responsible |

---

## Bug Title Formula

```
[Feature/Feature Area] — [What fails] — [Condition/Platform/Context]

Examples:
✅ "Login — Session not maintained when 'Remember Me' checked — Firefox 120"
✅ "Checkout — Order total incorrect when discount code applied multiple times"
✅ "User Profile — Profile photo upload fails with .png files > 2MB"
✅ "API POST /users — Returns 500 instead of 400 when email field is missing"

❌ "Login is broken"
❌ "Bug in checkout"
❌ "Something's wrong with the API"
```

---

## Full Bug Report Template

```
TITLE:
[Feature] — [What fails] — [When/Condition]

ENVIRONMENT:
- OS: macOS 14.3 / Windows 11 / Ubuntu 22.04
- Browser: Chrome 122.0 / Firefox 120.0 / Safari 17
- App Version / Build: v2.4.1 (staging)
- Test URL: https://staging.example.com
- Test Account: qa_test_01@example.com (credentials in team vault)

SEVERITY: Critical / Major / Minor / Trivial
PRIORITY: P1 / P2 / P3 / P4
REPRODUCIBILITY: 100% / Intermittent / Once

STEPS TO REPRODUCE:
1. Navigate to https://staging.example.com/login
2. Enter email: qa_test_01@example.com
3. Enter password: Password123!
4. Check the "Remember Me" checkbox
5. Click the "Sign In" button
6. Close the browser completely
7. Reopen the browser and navigate to https://staging.example.com/dashboard

EXPECTED RESULT:
User is automatically logged in and sees the dashboard without re-entering credentials.
(Session should persist per the "Remember Me" feature specification)

ACTUAL RESULT:
User is redirected to the login page and must log in again.
Console shows error: "TypeError: Cannot read properties of undefined (reading 'token')" 
The "Remember Me" checkbox has no effect.

TEST DATA USED:
- Account: qa_test_01@example.com / Password123!
- Account type: Standard user (not admin, not locked)

ATTACHMENTS:
- [remember_me_bug_recording.mp4] — 45-second screen recording showing full reproduction
- [console_error_screenshot.png] — DevTools console showing the error

RELATED TEST CASE: TC_LOGIN_005
FOUND IN BUILD: v2.4.1 (deployed 2026-03-15)
RELATED USER STORY: TICKET-234 "Remember Me functionality"

ADDITIONAL NOTES:
- Tested on Chrome 122: SAME ISSUE
- Tested on Private/Incognito mode: SAME ISSUE  
- The issue did NOT exist in build v2.3.9 (regression)
- Tested with 3 different user accounts — all exhibit same behavior
```

---

## Severity Guide

| Severity | Definition | Examples |
|----------|-----------|---------|
| 🔴 **Critical** | App crash, data loss, security breach, major feature completely broken | Payment processing fails; login bypass; data deleted unexpectedly |
| 🟠 **Major** | Key feature broken but workaround exists; wrong results returned | Search returns no results; profile photos not saving |
| 🟡 **Minor** | Feature partially works; deviation from spec with low user impact | Dropdown shows options in wrong order; error message text is generic |
| 🟢 **Trivial** | Cosmetic/UI issue only; no functional impact | Button text capitalization inconsistent; tooltip content is slightly off |

## Priority Guide

| Priority | Definition | Examples |
|----------|-----------|---------|
| P1 | Fix immediately (deploy hotfix if needed) | Blocks all users; security issue; release is ready but this bug is critical |
| P2 | Fix in current sprint | Impacts significant user workflow; no acceptable workaround |
| P3 | Fix in next sprint | Minor user impact; workaround exists |
| P4 | Fix when convenient | Cosmetic; very rare scenario; low user impact |

---

## Common Mistakes to Avoid

| ❌ Mistake | ✅ Correct Approach |
|------------|-------------------|
| Vague title: "Login broken" | Specific title: "Login — 'Remember Me' does not persist session — Firefox" |
| Steps say "log in with valid credentials" | Steps say "enter `qa_test_01@example.com` and `Password123!`" |
| Expected result: "should work" | Expected result: "user redirected to /dashboard; session cookie set" |
| No attachments | Screenshot + video for every UI bug |
| Filed as P1/Critical for a tooltip typo | Severity: Trivial; Priority: P4 |
| Not checking for duplicates | Always search Jira before filing a new bug |
| Filed after testing on only one browser | Test on 2+ browsers/OS before filing |
