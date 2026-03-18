# Selenium Test Automation Project

A beginner-friendly Selenium + Python test automation project built during Week 8 of the QA Internship Program. Tests the [SauceDemo](https://www.saucedemo.com) application.

![Tests](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/tests.yml/badge.svg)

---

## 📁 Project Structure

```
selenium_project/
├── conftest.py           ← pytest fixtures (WebDriver setup/teardown)
├── pytest.ini            ← pytest configuration
├── requirements.txt      ← Python dependencies
├── pages/
│   ├── __init__.py
│   ├── base_page.py      ← Base class with common browser methods
│   ├── login_page.py     ← Login page object
│   └── inventory_page.py ← Products page object
└── tests/
    ├── __init__.py
    ├── test_login.py     ← 9 login test cases
    └── test_inventory.py ← 7 inventory test cases
```

---

## 🚀 Setup & Run

### Prerequisites
- Python 3.8+ installed
- Google Chrome (latest) installed

### 1. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate    # macOS/Linux
# venv\Scripts\activate     # Windows
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run all tests
```bash
pytest
```

### 4. Run with HTML report
```bash
pytest --html=report.html --self-contained-html
# Open report.html in your browser
```

### 5. Run specific test file
```bash
pytest tests/test_login.py -v
```

### 6. Run by marker
```bash
pytest -m smoke     # Smoke tests only
pytest -m login     # Login tests only
```

---

## 🧪 Test Coverage

| File | Tests | Coverage Areas |
|------|-------|----------------|
| `test_login.py` | 9 | Valid login, invalid passwords, locked user, empty fields, logout |
| `test_inventory.py` | 7 | Page load, product count, add to cart, sorting |
| **Total** | **16** | |

---

## 🔑 Test Users (SauceDemo)

| Username | Password | Expected Behavior |
|----------|----------|------------------|
| `standard_user` | `secret_sauce` | Normal login |
| `locked_out_user` | `secret_sauce` | Locked out error |
| `problem_user` | `secret_sauce` | Various UI bugs |
| `performance_glitch_user` | `secret_sauce` | Slow performance |

---

## 🏗️ Design Patterns Used

- **Page Object Model (POM):** All page interactions are in `pages/` classes. Test files only call page methods — no locators in tests.
- **pytest Fixtures:** `conftest.py` provides `driver` and `logged_in_driver` fixtures for clean setup/teardown.
- **Parametrize:** Multiple data sets tested in a single test function using `@pytest.mark.parametrize`.
- **Explicit Waits:** All element waits use `WebDriverWait` — no `time.sleep()` calls.
