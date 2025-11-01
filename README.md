# Enterprise Software Testing Assignment3

This project was created for the **Enterprise Software Testing** course.  
It focuses on **automated UI testing** using **Python** and **Selenium WebDriver**.

We tested basic **e-commerce features** — like adding comments, comparing products, and managing a wishlist — on [LambdaTest’s E-commerce Playground](https://ecommerce-playground.lambdatest.io/).

## Project Files

```
├── test_comment.py        # Test for submitting a product review/comment
├── test_comparison.py     # Test for comparing multiple products
├── test_wishlist.py       # Test for adding products to wishlist
└── README.md              # Project info
```

## Setup & Requirements

Before running the tests, make sure you have the following:

### 1. Python & Browser

- Python **3.12.3**
- Google Chrome browser
- ChromeDriver (make sure it matches your Chrome version)

### 2. Install Packages

Use pip to install the needed libraries:

```bash
pip install selenium pandas lxml
```

## Test Descriptions

Each test file automates one main feature of the e-commerce site.  
They use Selenium to open Chrome, find web elements, and check if everything works as expected.

### 1. `test_comment.py` — Product Review Test

**What it does:**  
Checks if users can leave a review on a product.

**Steps:**

1. Open the homepage.  
2. Go to a product page.  
3. Click 5 stars, fill in the name and review.  
4. Submit the review.  
5. Check that the message appears:  
   _“Thank you for your review. It has been submitted to the webmaster for approval.”_

**Expected result:**  
`Test passed: Comment submitted successfully.`

### 2. `test_comparison.py` — Product Comparison Test

**What it does:**  
Tests whether the product comparison page works correctly.

**Steps:**

1. Go to the homepage.  
2. Add **three products** to comparison.  
3. Open the comparison page.  
4. Use **pandas** to read the comparison table.  
5. Make sure the names and prices match what was selected.

**Expected result:**  
`Test passed: Comparison function works successfully.`

### 3. `test_wishlist.py` — Wishlist Test

**What it does:**  
Checks if a logged-in user can add products to their wishlist.

**Steps:**

1. Open Chrome in incognito mode.  
2. Log in using the test account:  
   - Email: `testtesttest123@gmail.com`  
   - Password: `test123`  
3. Add **three products** to wishlist.  
4. Go to the wishlist page.  
5. Use **pandas** to read the table and compare data.

**Expected result:**  
`Test passed: Wishlist function works successfully.`

## How to Run

You can run each test one by one like this:

```bash
python test_comment.py
python test_comparison.py
python test_wishlist.py
```

## Notes

- Chrome will open and close automatically for each test.  
- You can change the login info in `test_wishlist.py` if needed.  
- The code uses **explicit waits (WebDriverWait)** so the elements load properly.  
- **pandas.read_html()** is used to get table data from the pages.  
- Selenium interacts with the site using **CSS selectors** and **ActionChains**.

## Learning Goals

By doing this project, I learned how to:

- Automate website testing using Selenium.  
- Select and verify UI elements.  
- Perform end-to-end (E2E) testing.  
- Use Pandas to read and compare web data.

## Author

**Name:** Kai-Hsiang Chuang  
**Course:** Enterprise Software Testing  
**Date:** 25 October 2025  
