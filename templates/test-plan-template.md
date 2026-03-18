# Test Plan Template

> **Instructions:** Fill out every section. Delete any section that is genuinely not applicable and note why. Incomplete test plans are not acceptable — stakeholders and team members depend on this document to understand the testing scope, approach, and readiness.

---

## Document Information

| Field | Value |
|-------|-------|
| **Document Title** | Test Plan — [Project/Feature Name] |
| **Project Name** | |
| **Application Under Test** | |
| **Version / Build** | |
| **Environment** | Staging / Production / UAT |
| **Author** | |
| **Reviewer** | |
| **Date Created** | |
| **Last Updated** | |
| **Status** | Draft / In Review / Approved |

---

## 1. Introduction

### 1.1 Purpose
*State the purpose of this test plan in 2–3 sentences. What feature or release is being tested? What is the goal of this testing effort?*

> Example: "This test plan defines the testing strategy, scope, resources, and schedule for testing the User Authentication feature (login, registration, password reset) of the MyApp web application version 3.0. The goal is to ensure all authentication flows work correctly and securely before the Sprint 12 release."

### 1.2 Application Overview
*Briefly describe what the application does and its intended users.*

---

## 2. Scope

### 2.1 Features In Scope
List all features/modules that WILL be tested:
- [ ] Feature 1: (e.g., User login)
- [ ] Feature 2: (e.g., User registration)
- [ ] Feature 3: (e.g., Password reset via email)

### 2.2 Features Out of Scope
List features/modules that will NOT be tested, and briefly explain why:

| Feature | Reason for Exclusion |
|---------|---------------------|
| Admin dashboard | No changes in this release |
| Billing module | Tested by a separate team |
| Mobile app | Separate test plan |

---

## 3. Testing Approach

### 3.1 Testing Types
List each testing type you will perform and why:

| Testing Type | Included? | Rationale |
|-------------|-----------|-----------|
| Functional Testing | ✅ Yes | Verify all features work per requirements |
| Regression Testing | ✅ Yes | Ensure new changes haven't broken existing features |
| Exploratory Testing | ✅ Yes | Discover unexpected behaviors |
| API Testing (Postman) | ✅ Yes | Test backend independently of UI |
| Performance Testing | ✅ Yes | Validate response times under load |
| Security Testing | ⚠️ Basic | Verify OWASP Top 5 checklist |
| Accessibility Testing | ✅ Yes | WCAG 2.1 Level AA compliance |
| Cross-browser Testing | ✅ Yes | Chrome, Firefox, Safari |
| Mobile Testing | ❌ No | Out of scope for this release |
| Automation | ✅ Yes | Automate regression suite using Selenium + Python |

---

## 4. Test Environment

### 4.1 Hardware
| Component | Specification |
|-----------|--------------|
| Testing Machine | MacBook Pro M2, 16GB RAM |

### 4.2 Software
| Component | Version | Notes |
|-----------|---------|-------|
| OS | macOS 14.3 | Could also note Windows 11 |
| Browser (primary) | Chrome 122 | |
| Browser (secondary) | Firefox 120 | |
| Application version | v3.0.0-rc1 | Release candidate |
| Test environment URL | https://staging.example.com | |

### 4.3 Test Data
| Data Category | How Provided |
|--------------|-------------|
| Valid user accounts | Created in staging DB by dev team |
| Invalid/edge case accounts | Created manually by QA |
| Payment data | Use Stripe test cards only |
| File uploads | Test files provided in /test-assets/ folder |

---

## 5. Entry and Exit Criteria

### 5.1 Entry Criteria
Testing will begin ONLY when ALL of the following are true:
- [ ] Feature is deployed to the staging environment
- [ ] Feature passes developer smoke test
- [ ] Test environment is accessible and stable
- [ ] Test data is prepared and verified
- [ ] All user stories have written acceptance criteria
- [ ] Required test cases are written and reviewed

### 5.2 Exit Criteria
Testing is considered complete and ready for release when ALL of the following are true:
- [ ] ≥ 95% of test cases have been executed
- [ ] 100% of P1 (Critical) test cases have passed
- [ ] 0 open defects with Critical severity
- [ ] 0 open defects with Major severity (or documented/accepted exceptions with PO sign-off)
- [ ] Regression suite passes at ≥ 95%
- [ ] Performance benchmarks met (P95 response time < 500ms)
- [ ] Product Owner has approved final build

---

## 6. Risk Assessment

| # | Risk | Likelihood | Impact | Mitigation |
|---|------|-----------|--------|------------|
| 1 | Staging environment unavailable | Medium | High | Notify DevOps 24h in advance; have backup schedule |
| 2 | Test data corrupted | Low | High | Backup test data; document data setup procedure |
| 3 | Feature delivered late | Medium | High | Begin test case writing from user stories (shift-left) |
| 4 | Integration with third-party service unstable | High | Medium | Use mocked service for core testing; test real integration separately |
| 5 | Browser compatibility issues | Low | Medium | Test on Chrome first; cross-browser on final day |
| *(Add more as needed)* | | | | |

---

## 7. Test Schedule

| Date | Activity | Effort (hrs) | Owner |
|------|----------|-------------|-------|
| Day 1 | Test case review and finalization | 4h | QA Intern |
| Day 1–2 | Functional testing (core features) | 16h | QA Intern |
| Day 2–3 | Negative / edge case testing | 12h | QA Intern |
| Day 3 | API testing (Postman) | 6h | QA Intern |
| Day 4 | Automation execution + report | 4h | QA Intern |
| Day 4 | Performance and security tests | 6h | QA Intern |
| Day 5 | Regression testing | 4h | QA Intern |
| Day 5 | Final report and sign-off | 2h | QA Intern |

---

## 8. Roles and Responsibilities

| Role | Person | Responsibilities |
|------|--------|----------------|
| QA Intern | [Your Name] | Write and execute test cases; log bugs; report status daily |
| QA Mentor | [Mentor Name] | Review test plan; provide guidance; sign off on quality |
| Developer | [Dev Name] | Fix reported bugs; provide test environment |
| Product Owner | [PO Name] | Provide acceptance criteria; sign off on features |

---

## 9. Deliverables

| Deliverable | Due Date | Owner |
|-------------|----------|-------|
| This Test Plan | [Date] | QA Intern |
| Test Case Suite | [Date] | QA Intern |
| Daily test status updates | Daily | QA Intern |
| Bug reports (as found) | Ongoing | QA Intern |
| Final Test Summary Report | [Date] | QA Intern |

---

## 10. Test Metrics to Track

| Metric | Target | Notes |
|--------|--------|-------|
| Test Coverage | > 90% | Planned vs executed cases |
| Test Pass Rate | > 95% | At release sign-off |
| Defect Escape Rate | < 5% | Bugs found in prod after release |
| Critical/Blocker open at release | 0 | Non-negotiable |

---

## 11. Approval Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| QA Intern | | | |
| QA Mentor | | | |
| Product Owner | | | |
