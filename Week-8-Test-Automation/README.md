# 🤖 Week 8 — Test Automation Basics

> **Week Goal:** Build foundational test automation skills using Selenium WebDriver with Python — the most widely used combination for browser automation in the QA industry.

---

## 📚 Learning Objectives

By the end of this week, you will be able to:

- [ ] Explain the benefits and **limitations** of test automation — and know when *not* to automate
- [ ] Set up a complete **Selenium WebDriver + Python** environment
- [ ] Write automated tests that locate, interact with, and assert on web elements
- [ ] Apply the **Page Object Model (POM)** design pattern to organize automation code
- [ ] Run tests with **pytest** and generate an HTML report
- [ ] Set up a basic **GitHub Actions** CI pipeline to run tests on every push

---

## 📖 Key Topics & Theory

### 1. Why Automate? When to Automate?

Test automation is a **force multiplier**, not a replacement for manual testing.

#### When to Automate

| Automate These | Don't Automate These |
|---------------|---------------------|
| Regression tests (run every sprint) | Exploratory testing |
| Smoke / sanity tests | One-time or rarely-run tests |
| Data-driven tests (same steps, many datasets) | Features that change constantly |
| Performance/load tests | Highly visual/subjective UX evaluation |
| API tests (fast, stable, easy to assert) | Brand-new, unstable features |
| Long overnight regression runs | Scenarios requiring human judgment |

#### The Testing Pyramid — Automation Strategy

```
         /\
        /  \
       / UI \          ← Few, slow, expensive (Selenium/Cypress)
      /──────\            Test critical user journeys
     /  API   \        ← Medium (Postman / pytest + requests)
    /──────────\          Test business logic at service level
   /  Unit Tests\      ← Many, fast, cheap (pytest, JUnit)
  /──────────────\        Test individual functions/methods
```

**Rule:** Automate at the lowest level possible. UI automation for unit-testable logic is wasteful.

---

### 2. Environment Setup

```bash
# Step 1: Verify Python installation
python3 --version  # Should be 3.8+

# Step 2: Create a virtual environment (always use one!)
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

# Step 3: Install dependencies
pip install selenium pytest pytest-html

# Step 4: Selenium >= 4.6 manages ChromeDriver automatically — no manual download needed!
# Just make sure Google Chrome is installed.

# Step 5: Verify setup
python -c "from selenium import webdriver; print('Selenium installed successfully')"
```

---

### 3. Your First Selenium Test

```python
# tests/test_google.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_google_search():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://www.google.com")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Python testing")
    search_box.send_keys(Keys.RETURN)

    time.sleep(2)  # Don't use time.sleep in real tests! Use WebDriverWait instead.

    assert "Selenium" in driver.title

    driver.quit()
```

---

### 4. Element Locators — Finding Things on the Page

| Strategy | Selenium Code | Best For | Stability |
|----------|--------------|---------|-----------|
| **By ID** | `By.ID, "username"` | Unique IDs | ⭐⭐⭐⭐⭐ (best) |
| **By CSS Selector** | `By.CSS_SELECTOR, "#username"` | Flexible, fast | ⭐⭐⭐⭐ |
| **By XPath** | `By.XPATH, "//input[@id='username']"` | Complex queries | ⭐⭐⭐ |
| **By Name** | `By.NAME, "username"` | Form fields | ⭐⭐⭐ |
| **By Class Name** | `By.CLASS_NAME, "btn-primary"` | Not unique | ⭐⭐ |
| **By Tag Name** | `By.TAG_NAME, "h1"` | Very generic | ⭐ |
| **Absolute XPath** | `By.XPATH, "/html/body/div/..."` | Never use this | ❌ (fragile) |

**CSS Selector Quick Reference:**
```css
#id              → Input with id="id"
.classname       → Elements with class="classname"
button[type='submit']  → Button with type='submit'
.form input      → Input inside element with class 'form'
```

---

### 5. Explicit Waits — No More `time.sleep()`

`time.sleep()` is unreliable and slow. Use **WebDriverWait** instead — it waits until a condition is true (or times out):

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Wait up to 10 seconds for an element to be clickable
wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.ID, "submit-btn")))
button.click()

# Wait for URL to change
wait.until(EC.url_contains("/dashboard"))

# Wait for element to appear
wait.until(EC.visibility_of_element_located((By.ID, "success-message")))

# Wait for element to disappear (loading spinner)
wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "loading-spinner")))
```

---

### 6. Page Object Model (POM)

POM separates **test logic** from **page interaction code**. Benefits:
- If the UI changes, you update ONE page class — not dozens of test files
- Tests are readable and maintainable
- Promotes code reuse

**Project structure with POM:**
```
selenium_project/
├── conftest.py          ← pytest fixtures (driver setup/teardown)
├── pytest.ini           ← pytest configuration
├── requirements.txt     ← dependencies
├── pages/
│   ├── __init__.py
│   ├── base_page.py     ← common methods for all pages
│   ├── login_page.py    ← Login page elements + actions
│   └── dashboard_page.py ← Dashboard page elements + actions
└── tests/
    ├── __init__.py
    └── test_login.py    ← Test cases (use page classes, no locators here)
```

See the complete implementation in the [selenium_project/](./selenium_project/) folder.

---

### 7. pytest Basics

pytest is the most widely used Python test runner. Key features:

```python
# Test functions start with "test_"
def test_valid_login():
    # Arrange: set up
    # Act: do the thing
    # Assert: check the result
    assert result == expected

# Fixtures provide reusable setup/teardown
@pytest.fixture
def driver():
    d = webdriver.Chrome()
    yield d
    d.quit()

# Parametrize: run one test with multiple datasets
@pytest.mark.parametrize("username,password,expected", [
    ("valid@test.com", "password123", True),
    ("wrong@test.com", "password123", False),
    ("valid@test.com", "wrongpass", False),
])
def test_login(username, password, expected):
    result = perform_login(username, password)
    assert result == expected
```

**Run tests:**
```bash
pytest                          # Run all tests
pytest tests/test_login.py      # Run specific file
pytest -v                       # Verbose output
pytest --html=report.html       # Generate HTML report
pytest -k "login"               # Run only tests with "login" in the name
pytest -m smoke                 # Run only tests marked as @pytest.mark.smoke
```

---

### 8. GitHub Actions — CI Pipeline

Create `.github/workflows/tests.yml` in your repository to automatically run tests on every push:

```yaml
name: Selenium Tests

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'

    - name: Install Chrome
      uses: browser-actions/setup-chrome@v1

    - name: Install dependencies
      run: |
        pip install -r requirements.txt

    - name: Run tests
      run: |
        pytest --html=report.html --self-contained-html

    - name: Upload test report
      uses: actions/upload-artifact@v4
      if: always()
      with:
        name: test-report
        path: report.html
```

---

## 🛠️ Hands-on Tasks & Activities

| Day | Activity |
|-----|----------|
| **Monday** | Set up Python venv, install Selenium + pytest; write and run first 3 Selenium scripts on SauceDemo |
| **Tuesday** | Automate login (positive + negative) and navigation flows; write 6+ test cases |
| **Wednesday** | Refactor all scripts using Page Object Model; create LoginPage and InventoryPage classes |
| **Thursday** | Add pytest fixtures, parametrize login tests, generate HTML report |
| **Friday** | Push to GitHub; create GitHub Actions workflow; get CI badge in README |

### Starter Application for Practice
**SauceDemo** — [saucedemo.com](https://www.saucedemo.com)
- Valid user: `standard_user` / `secret_sauce`
- Locked user: `locked_out_user` / `secret_sauce`
- Problem user: `problem_user` / `secret_sauce`

**Test scenarios to automate:**
1. Login with valid credentials → assert redirected to inventory page
2. Login with invalid password → assert error message shown
3. Login with locked user → assert locked-out message shown
4. Add item to cart → assert cart count updates
5. Complete checkout flow → assert order confirmation page
6. Sort products by price → assert items in correct order

---

## 🖥️ Tools & Software

| Tool | Purpose | Cost |
|------|---------|------|
| **Python 3.11+** | Programming language | Free |
| **Selenium WebDriver 4.x** | Browser automation | Free (pip install) |
| **pytest** | Test runner | Free (pip install) |
| **pytest-html** | HTML test reports | Free (pip install) |
| **VS Code** | IDE | Free |
| **GitHuband GitHub Actions** | Version control + CI | Free |
| **Allure Report** (optional) | Beautiful test reports | Free |

---

## 📚 Recommended Resources

- 📹 "Selenium Python Tutorial Complete Course" — Mukesh Otwani (LambdaTest) YouTube
- 📹 "Page Object Model in Selenium" — Automation Step by Step YouTube
- 📹 "pytest Tutorial for Beginners" — Corey Schafer YouTube
- 📹 "GitHub Actions CI/CD for Python" — TechWorld with Nana YouTube
- 📖 Selenium Python Documentation — [selenium-python.readthedocs.io](https://selenium-python.readthedocs.io)
- 🆓 "Selenium WebDriver with Python" — Test Automation University (free) — [testautomationu.applitools.com](https://testautomationu.applitools.com)
- 📘 *"Python Testing with pytest"* — Brian Okken (excellent book)

---

## 📝 Deliverables — Due Friday EOD

### Deliverable 1: GitHub Repository
- Well-organized Selenium + Python project
- Clear README with: project description, how to install, how to run tests
- Minimum **15 automated test cases** covering login, navigation, and form interactions
- All tests organized in the `tests/` folder with descriptive names

### Deliverable 2: Page Object Model Implementation
- At least **3 page classes** implementing POM (`LoginPage`, `InventoryPage`, + 1 more)
- No locators or `find_element` calls in test files — all in page classes
- `conftest.py` with driver fixture for proper setup/teardown

### Deliverable 3: pytest HTML Report
- Run: `pytest --html=report.html --self-contained-html`
- Screenshot of the report showing test results
- Commit the latest report to your repo or attach it in your submission

### Deliverable 4: CI Pipeline
- `.github/workflows/tests.yml` in your repo
- Screenshot of a successful GitHub Actions run (green checkmark)
- README badge: `![Tests](https://github.com/yourusername/repo/actions/workflows/tests.yml/badge.svg)`

### Deliverable 5: Automation Decision Guide (1 page)
Your personal framework for deciding what to automate:
- What criteria do you use to decide "should this be automated?"
- Give 5 examples: 3 things you would automate + 2 things you would NOT automate (and why)

---

## ✅ Assessment & Feedback Criteria

| Criteria | Excellent (4) | Good (3) | Developing (2) | Needs Work (1) |
|----------|--------------|----------|---------------|----------------|
| **Environment & setup** | All tools configured; CI pipeline running; clean repo | Most tools working; repo organized | Basic setup; environment issues | Could not run tests independently |
| **Code quality** | Clean POM; descriptive names; DRY code; proper fixtures | POM used; minor issues | No POM; working but messy | Copied code without understanding |
| **Test coverage** | 15+ tests covering positive, negative, and edge cases | 10–14 tests | 6–9 tests | Fewer than 6 tests |
| **CI/CD** | Pipeline runs on push; report uploaded as artifact | Pipeline configured and running | Pipeline configured but issues remain | Git repo only; no CI |

---

## 💼 Real-World Application & Tips

> 🏢 **In real companies:** A well-maintained regression automation suite can run 500+ tests in under 30 minutes. That's equivalent to 2–3 days of manual testing effort run automatically every night or on every commit. This is how QA teams scale.

> 💡 **Pro Tip:** Don't automate flaky tests. A test that sometimes passes and sometimes fails without any change to the code is **worse than no test at all** — it trains engineers to ignore failing tests, eroding trust in the entire test suite. Fix instability first (use proper WebDriverWait, stable locators, clean test data).

> 💡 **Pro Tip:** Commit your automation code to the **same repository as the application code** (or a linked repo). This means automation can be updated by the same Pull Request that changes the feature — test and code stay in sync.

> ⚠️ **Common Mistake:** Writing tests that depend on each other (e.g., test 2 needs data created by test 1). Every test must be **independently executable** — in any order, from a clean state. Use fixtures to set up and tear down data.

---

*← [Week 7 — Quality Standards](../Week-7-Quality-Standards/README.md) | [Week 9 — Advanced QA →](../Week-9-Advanced-QA/README.md)*
