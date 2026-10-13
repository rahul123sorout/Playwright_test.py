Playwright Automation Framework – WidgetBrowser

Project Overview

This project automates the testing of the [qooxdoo WidgetBrowser](https://qooxdoo.org/qxl.widgetbrowser/) application using **Python, Playwright, and Pytest

The project started with UI automation using different selectors and was then organized into a **Page Object Model (POM)** framework. Excel-based data-driven testing was added to make test inputs reusable and easier to maintain.

Project Objectives

- Automate UI interactions across different WidgetBrowser sections.
- Practice and implement CSS and XPath selectors.
- Organize automation code using the Page Object Model (POM).
- Use Pytest fixtures for browser setup and test-data management.
- Read test data from Excel using OpenPyXL.
- Validate form inputs using assertions.
- Execute and maintain tests using Pytest.

Project Structure

```text
WidgetBrowser_POM/
│
├── pages/
│   ├── basic_page.py
│   ├── combo_page.py
│   ├── control_page.py
│   ├── embed_page.py
│   ├── embedframe_page.py
│   ├── form_page.py
│   ├── list_page.py
│   ├── misc_page.py
│   ├── tab_page.py
│   ├── table_page.py
│   ├── toolbar_menu_page.py
│   ├── tree_page.py
│   └── window_page.py
│
├── tests/
│   └── test_widgetbrowser.py
│
├── conftest.py
├── requirement.txt
├── test_data.xlsx
└── README.md
```

1. Selector Implementation

Implemented UI element identification using Playwright locators.

- CSS selectors: Used to locate elements through CSS attributes, classes, IDs, and other supported selector patterns.
- XPath selectors: Used to locate elements based on DOM relationships and attributes.
- Playwright locators: Used to interact with UI elements and perform actions such as filling fields and clicking controls.

The selectors are maintained within the relevant page object classes to keep test logic separate from element identification.

2. Page Object Model (POM)

The project follows the Page Object Model design pattern.

Each page object class manages the locators and actions for a particular WidgetBrowser section.

Examples:

- `form_page.py` – Form-related locators and actions.
- `combo_page.py` – Combo-box interactions.
- `table_page.py` – Table-related interactions.
- `tree_page.py` – Tree-related interactions.
- `window_page.py` – Window-related interactions.

Benefits of POM

- Reduces code duplication.
- Improves readability and maintainability.
- Separates UI interactions from test execution logic.
- Makes future updates easier when locators change.

3. Excel-Based Data-Driven Testing

Test data is maintained in `test_data.xlsx` instead of hardcoding input values directly in the test.

Excel test-data format

| username | password |
| Rahul | Test@123 |
| Amit | Demo@123 |

These are sample test values.

The Excel file is read using OpenPyXL. The first row contains column headers, and the remaining rows contain test data.

The `excel_data` fixture in `conftest.py` reads the workbook and provides the data to the test function.

The test iterates through the rows, fills the corresponding form fields, and validates the entered values using assertions.

Example

```python
for data in excel_data:
    form.fill_required_field(data["username"])
    form.fill_password(data["password"])

    assert form.required_field.input_value() == data["username"]
    assert form.password_field.input_value() == data["password"]
```

This approach allows multiple sets of test data to be tested without changing the test logic.

4. Pytest Fixtures

The project uses fixtures to separate setup and test-data preparation from test logic.

page fixture

- Starts Playwright.
- Launches Microsoft Edge.
- Creates a browser page.
- Opens the WidgetBrowser application.
- Provides the page to the test.
- Closes the browser after execution.

excel_data fixture

- Locates `test_data.xlsx`.
- Reads the active worksheet.
- Converts rows into dictionaries using the column headers.
- Returns the test data to the test function.

5. Assertions and Test Execution

Assertions are used to verify that the values entered into the form match the expected Excel data.

Run the tests with:

```bash
pytest -v -s
```

- `-v` displays detailed test names and results.
- `-s` displays print statements in the terminal.

A successful test is reported as `PASSED`. The terminal output can also be used to verify that each Excel row is processed.

Setup and Installation

Prerequisites

- Python installed
- Microsoft Edge installed
- Git installed
- Internet connection to access the WidgetBrowser application

Install dependencies

Clone the repository and open the project directory:

```bash
git clone <repository-url>
cd WidgetBrowser_POM
```

Install the dependencies:

```bash
pip install -r requirement.txt
```

Run the tests

```bash
pytest -v -s
```



