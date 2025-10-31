# Enterprise Software Testing Course

This project is part of the **Enterprise Software Testing Course**, focused on **automated UI testing** using **Python and Selenium WebDriver**.  
The goal is to test major e-commerce functionalities (comment, comparison, and wishlist) on [LambdaTest’s E-commerce Playground](https://ecommerce-playground.lambdatest.io/).

## Project Structure

```
├── test_comment.py        # Test case for submitting a product review/comment
├── test_comparison.py     # Test case for comparing multiple products
├── test_wishlist.py       # Test case for adding products to wishlist
└── README.md              # Project documentation
```

## Requirements

Before running the tests, make sure the following dependencies are installed:

### 1. Python Environment

- Python **3.8+**
- Google Chrome browser
- ChromeDriver

### 2. Install Required Packages

```bash
pip install selenium pandas lxml
```

## Test Overview

Each test script automates an e-commerce feature using Selenium with waits and verification logic.

### 1. `test_comment.py` — Product Review Test

**Purpose:**  
Validates that users can successfully submit a review for a product.

**Test Flow:**

1. Open Chrome and navigate to homepage.
2. Go to the product category page.
3. Select the first product.
4. Click on 5 stars, enter a name and review message.
5. Submit the review form.
6. Verify the success message:  
   _“Thank you for your review. It has been submitted to the webmaster for approval.”_

**Expected Output:**  
`Test passed: Comment submitted successfully.`

---

### 2. `test_comparison.py` — Product Comparison Test

**Purpose:**  
Ensures that the **product comparison** feature works correctly and data matches across views.

**Test Flow:**

1. Open Chrome and visit homepage.
2. Navigate to product category page.
3. Select and add **three products** to the comparison list.
4. Click on the comparison button.
5. Scrape the comparison table using **Pandas**.
6. Validate product names and prices between selected products and the comparison table.

**Expected Output:**  
`Test passed: Comparison function works successfully.`

---

### 3. `test_wishlist.py` — Wishlist Functionality Test

**Purpose:**  
Verifies that logged-in users can add products to their wishlist and view them correctly.

**Test Flow:**

1. Launch Chrome in incognito mode.
2. Log in to the test account:
   - Email: `testtesttest123@gmail.com`
   - Password: `test123`
3. Add **three products** to the wishlist.
4. Navigate to the Wishlist page.
5. Scrape wishlist data using **Pandas**.
6. Compare selected product data with displayed wishlist items.

**Expected Output:**  
`Test passed: Comparison function works successfully.`

## How to Run the Tests

Run each test file individually:

```bash
python test_comment.py
python test_comparison.py
python test_wishlist.py
```

## Notes

- Each script opens and closes Chrome automatically.
- Modify login credentials in `test_wishlist.py` if you use your own account.
- Some steps use explicit waits (`WebDriverWait`) to ensure page elements load correctly.
- Data extraction uses **pandas.read_html()** for HTML table parsing.
- All scripts use the **CSS selectors** and **ActionChains** for reliable interaction.

---

## Learning Objectives

Through this project, learners will:

- Practice **enterprise-grade automated testing** using Selenium.
- Gain experience in **UI element selection** and **test data validation**.
- Understand **E2E testing workflows** with web automation.
- Learn **data validation and table parsing** via Pandas.

## Author

This repository was created for educational purposes in the **Enterprise Software Testing Course**.  
Developed by: _Kai-Hsiang Chuang_  
Date: _October 2025_
