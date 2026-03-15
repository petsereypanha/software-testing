# 🌐 Week 6 — API Testing & Web QA

> **Week Goal:** Understand how APIs work and gain practical skills in testing web services using Postman — a critical and highly sought-after skill in modern QA roles.

---

## 📚 Learning Objectives

By the end of this week, you will be able to:

- [ ] Explain what a REST API is and how HTTP methods, status codes, and JSON work together
- [ ] Use **Postman** to send requests and inspect API responses
- [ ] Write **Postman test scripts** to automate assertions in JavaScript
- [ ] Test common API scenarios: authentication, CRUD operations, and error handling
- [ ] Identify common API defects: wrong status codes, missing validation, incorrect data types, information exposure

---

## 📖 Key Topics & Theory

### 1. What Is an API?

An **API (Application Programming Interface)** is how software components communicate with each other. A **REST API** uses HTTP, making it accessible from any client (browser, mobile app, or testing tool like Postman).

Think of an API like a restaurant menu:
- The **menu** = API documentation (tells you what you can order)
- The **waiter** = the API (takes your request, delivers the response)
- The **kitchen** = the backend (actually does the work)

---

### 2. HTTP Methods (CRUD Operations)

| HTTP Method | CRUD Action | What It Does | Example |
|-------------|-------------|-------------|---------|
| **GET** | Read | Retrieve data | `GET /users/123` → Returns user data |
| **POST** | Create | Create new resource | `POST /users` with JSON body |
| **PUT** | Update (replace) | Replace entire resource | `PUT /users/123` with full new data |
| **PATCH** | Update (partial) | Update specific fields | `PATCH /users/123` with `{"email": "new@test.com"}` |
| **DELETE** | Delete | Remove resource | `DELETE /users/123` |

---

### 3. HTTP Status Codes — Know These Cold

| Code | Name | Meaning | Test Scenario |
|------|------|---------|---------------|
| **200** | OK | Successful request | GET returns data |
| **201** | Created | Resource successfully created | POST creates a new user |
| **204** | No Content | Success, no body returned | DELETE successful |
| **400** | Bad Request | Client sent invalid data | Missing required field |
| **401** | Unauthorized | Not authenticated | No token / expired token |
| **403** | Forbidden | Authenticated but no permission | Regular user accessing admin endpoint |
| **404** | Not Found | Resource doesn't exist | `GET /users/9999999` |
| **409** | Conflict | Resource already exists | Registering with duplicate email |
| **422** | Unprocessable Entity | Validation error | Email format invalid |
| **500** | Internal Server Error | Server-side bug | Crash on backend |

---

### 4. JSON — The Data Format for APIs

Most REST APIs exchange data in **JSON (JavaScript Object Notation)**:

```json
{
  "id": 42,
  "name": "Jane Smith",
  "email": "jane@example.com",
  "role": "admin",
  "active": true,
  "createdAt": "2026-01-15T09:30:00Z",
  "profile": {
    "avatarUrl": "https://cdn.example.com/avatars/42.jpg",
    "bio": "QA Lead"
  },
  "tags": ["qa", "automation", "lead"]
}
```

**What to validate in a JSON response:**
- Keys exist (no missing fields)
- Values have correct data types (`id` is a number, not a string)
- Values are in the expected range/format (`email` contains `@`)
- Null/empty values are handled appropriately
- Sensitive data is NOT exposed (`password`, `ssn`, `credit_card`)

---

### 5. What to Test in an API

Every API test should verify multiple dimensions:

| Dimension | What to Check |
|-----------|--------------|
| **Status Code** | Is it the correct code for this scenario? |
| **Response Body** | All expected fields present? Correct values? Correct types? |
| **Response Headers** | Content-Type: application/json? Auth headers present? |
| **Response Time** | Under acceptable SLA? (usually < 500ms for most APIs) |
| **Error Handling** | Do invalid inputs return 400/422 with helpful error messages? |
| **Authentication** | Does 401 appear when the token is missing or expired? |
| **Authorization** | Can user A access user B's private data? (Should not be possible) |
| **Data Integrity** | Does the data created/updated match what was sent? |
| **Idempotency** | Does calling the same GET/DELETE twice produce the same result? |

---

### 6. Postman Test Script Examples

Write these in the **Tests** tab of a Postman request. They run automatically after the response arrives.

```javascript
// Test 1: Check status code
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

// Test 2: Response body has expected field
pm.test("Response body has 'id' field", function () {
    const jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property('id');
});

// Test 3: Field has correct type
pm.test("id is a number", function () {
    const jsonData = pm.response.json();
    pm.expect(jsonData.id).to.be.a('number');
});

// Test 4: Response time is acceptable
pm.test("Response time is under 500ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(500);
});

// Test 5: Content-Type header is JSON
pm.test("Content-Type is application/json", function () {
    pm.expect(pm.response.headers.get('Content-Type')).to.include('application/json');
});

// Test 6: List response is not empty
pm.test("Response array is not empty", function () {
    const jsonData = pm.response.json();
    pm.expect(jsonData).to.be.an('array').that.is.not.empty;
});

// Test 7: Store response value as environment variable (for chaining)
const jsonData = pm.response.json();
pm.environment.set("userId", jsonData.id);
```

---

### 7. Postman Environments & Collections

**Environments:** Store variables like base URLs and auth tokens so you can switch between staging/production easily.
```
Environment: Staging
  BASE_URL = https://staging-api.example.com
  AUTH_TOKEN = (set by login test)
  USER_ID = (set dynamically)
```

**Collections:** Organized groups of API requests. Structure yours like this:
```
📁 Collection: E-Commerce API Tests
  📂 Authentication
    POST /auth/register
    POST /auth/login      ← Sets AUTH_TOKEN env variable
    POST /auth/logout
    POST /auth/refresh-token
  📂 Users
    GET /users (all)
    GET /users/:id
    PATCH /users/:id
    DELETE /users/:id
  📂 Products
    GET /products
    POST /products
  📂 Error Scenarios
    POST /auth/login (wrong password) → expect 401
    GET /users/99999 → expect 404
    POST /users (missing email) → expect 400
```

---

## 🛠️ Hands-on Tasks & Activities

**Practice APIs (authorized for testing):**
- 🔗 [JSONPlaceholder](https://jsonplaceholder.typicode.com/) — fake REST API, no auth needed
- 🔗 [ReqRes.in](https://reqres.in/) — realistic responses including auth
- 🔗 [Swagger Petstore](https://petstore.swagger.io/) — full CRUD operations
- 🔗 Company staging API (if available and authorized)

| Day | Activity |
|-----|----------|
| **Monday** | Install Postman. Make 10 requests to JSONPlaceholder (GET, POST, PUT, DELETE). Explore response fields. |
| **Tuesday** | Test authentication flow: register → login → get token → use token in protected endpoint (ReqRes.in) |
| **Wednesday** | Write Postman test scripts: 3 assertions minimum per request; 10 requests total |
| **Thursday** | Test all error scenarios: missing fields, wrong token, wrong ID, duplicate registration |
| **Friday** | Export Postman collection; run with Newman CLI; write API test summary report |

### API Testing Checklist (Use Every Time)
- [ ] Tested with valid data (happy path)
- [ ] Tested with missing required fields → expect 400
- [ ] Tested with invalid data formats → expect 400/422
- [ ] Tested without authentication token → expect 401
- [ ] Tested with another user's resource ID → expect 403 or 404
- [ ] Tested response time → under 500ms?
- [ ] Checked for sensitive data in error messages (no stack traces, no passwords)
- [ ] Verified response body structure matches API documentation

---

## 🖥️ Tools & Software

| Tool | Purpose | Cost |
|------|---------|------|
| **Postman** | API testing, collections, environments | Free |
| **Newman** | Run Postman collections from command line | Free (npm) |
| **Swagger UI** | Read API documentation interactively | Free |
| **curl** | CLI API requests (no UI) | Built-in macOS/Linux |
| **JSON Formatter** | Chrome extension for readable JSON | Free |

### Install Newman (Postman CLI runner)
```bash
# Install Node.js first (nodejs.org), then:
npm install -g newman
npm install -g newman-reporter-htmlextra

# Run your collection
newman run MyCollection.json -e MyEnvironment.json \
  -r htmlextra --reporter-htmlextra-export report.html
```

---

## 📚 Recommended Resources

- 📹 "Postman Tutorial for Beginners — Complete Course" — Valentin Despa YouTube (highly recommended)
- 📹 "REST API Concepts and Examples" — WebConcepts YouTube
- 📹 "API Testing with Postman" — freeCodeCamp YouTube
- 📖 "API Testing Tutorial" — guru99.com
- 📖 "What is a REST API?" — restfulapi.net
- 🆓 **Postman Student Expert Program** (free badge) — [postman.com/student-program](https://www.postman.com/student-expert/)
- 📖 Postman Learning Center — [learning.postman.com](https://learning.postman.com)

---

## 📝 Deliverables — Due Friday EOD

### Deliverable 1: Postman Collection (exported JSON)
- Organized collection with folders: CRUD, Authentication, Error Scenarios
- Minimum 20 API requests with descriptive names
- Environment file with `BASE_URL` and `AUTH_TOKEN` variables
- README in your GitHub repo explaining how to import and run it

### Deliverable 2: Test Scripts
- Minimum 15 Postman test assertions spread across the collection
- Must include: status code checks, body field validation, data type checks, response time checks

### Deliverable 3: Newman Report
- Run your collection with Newman
- Export the HTML report (htmlextra reporter)
- Screenshot of the pass/fail summary

### Deliverable 4: API Test Summary Report (1 page)
- What API(s) did you test?
- How many requests tested? Pass/Fail breakdown?
- Top 3 observations or issues found
- What would you test next if you had more time?

---

## ✅ Assessment & Feedback Criteria

| Criteria | Excellent (4) | Good (3) | Developing (2) | Needs Work (1) |
|----------|--------------|----------|---------------|----------------|
| **Postman proficiency** | Collections, environments, scripts, Newman CI | Collections + test scripts | Basic requests only | Required frequent help |
| **Test coverage** | CRUD + Auth + Error + Performance ≥ 20 requests | CRUD + Auth | CRUD operations only | Fewer than 10 requests |
| **Test script quality** | All assertions valid, meaningful, and varied | Most assertions correct | Some assertions trivial or incorrect | No scripts written |
| **API bug identification** | Found 3+ real issues with clear impact | Found 1–2 issues | Identified potential issues | No issues found or reported |

---

## 💼 Real-World Application & Tips

> 🏢 **In real companies:** Modern applications are API-first — the backend and frontend are separate. This means a QA engineer who can test APIs can perform testing **before the UI even exists**. This shifts testing left and gives teams faster feedback cycles. API testing skill is one of the most consistently requested QA skills in job postings.

> 💡 **Pro Tip:** Always check what happens when you send a request **without a required field**. Many serious security vulnerabilities occur when servers return 500 errors (exposing stack traces and internal info) instead of clean 400 errors.

> 💡 **Pro Tip:** Use Postman environments for `BASE_URL` from day one. If you hardcode URLs in every request, changing from staging to production becomes a nightmare to manage.

> ⚠️ **Security Note:** Only test APIs on systems you have explicit authorization to test. Never test third-party or production APIs with potentially destructive operations (DELETE, POST with fake data).

---

*← [Week 5 — Agile & Scrum](../Week-5-Agile-Scrum/README.md) | [Week 7 — Quality Standards →](../Week-7-Quality-Standards/README.md)*
