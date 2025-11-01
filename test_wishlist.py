# Test Case: Wishlist
import time
import pandas as pd
from io import StringIO
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Function to wait for system
def wait_system():
    time.sleep(3)

# Choose product functions
def choose_num_product(driver, num):
    choose_product = driver.find_elements(By.CSS_SELECTOR, ".product-thumb")[num]
    product_name = choose_product.find_element(By.CSS_SELECTOR, "h4 a").text
    product_price = choose_product.find_element(By.CSS_SELECTOR, ".price").text
    ActionChains(driver).move_to_element(choose_product).perform()
    comp_button = WebDriverWait(choose_product, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[title*='Wish'], i.fa-heart"))
    )
    comp_button.click()
    return product_name, product_price

# Step 1. Open Chrome Browser
def open_browser():
    options = Options()
    # open incognito window
    options.add_argument("--incognito")  
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver

# Step 2. Go to the home page
def go_to_homepage(driver):
    driver.get("https://ecommerce-playground.lambdatest.io")

# Step 3. Login for my test account to test wishlist feature
def login_account(driver, email, password):
    driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")
    driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys(email)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(password)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "input[value='Login']").click()
    wait_system()

# Step 4. Check wishlist if exists, delete the item
def check_wishlist(driver):
    driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/wishlist")
    time.sleep(3)
    items = driver.find_elements(By.CSS_SELECTOR, "table[class='table table-hover border']")
    check_url = []
    for item in items:
        links = item.find_elements(By.TAG_NAME, "a")
        for link in links:
            if "remove" in link.get_attribute("href"):
                check_url.append(link.get_attribute("href"))
    for i in check_url:
        driver.get(i)
        wait_system()

# Step 5. Choose first three product and click wishlist button
def choose_first_three_product(driver):
    choose_product_dict = {}
    driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=product/category&path=20")
    time.sleep(5)
    for i in range(3):
        product_name, product_price = choose_num_product(driver, i)
        choose_product_dict[f"Product{i+1}"] = {
            "name": product_name,
            "price": product_price
        }
        print(f"Product{i+1} added to wishlist: {product_name} - {product_price}")
        time.sleep(2)
    return choose_product_dict

# Step 6. Naviagte to wishlist page
def nav_wishlist(driver):
    driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/wishlist")

# Step 7. Use pandas to capture wishlist table
def get_table_info(driver):
    html = driver.page_source
    tables = pd.read_html(StringIO(html))
    return tables[1]

# Step 8. Capture need information from table
def get_table_information(w_table):
    wish_dict = {}
    for i in range(w_table.shape[0]):
        product_name = w_table["Product Name"][i]
        product_price = w_table["Unit Price"][i]
        wish_dict[f"Product{i+1}"] = {
            "name": product_name,
            "price": product_price
        }
    return wish_dict

# Step 9. Run the test
def run_test(choose_dict, comp_dict):
    if choose_dict == comp_dict:
        print("Test passed: Wishlist function works successfully.")
    else:
        print("Test failed: Wishlist function works unsuccessful.")


# Step 10. Quit the browser
def close_browser(driver):
    driver.quit()

if __name__ == "__main__":
    try:
        driver = open_browser()
        wait_system()
        go_to_homepage(driver)
        wait_system()
        login_account(driver, "testtesttest123@gmail.com", "test123")
        wait_system()
        check_wishlist(driver)
        wait_system()
        choose_dict = choose_first_three_product(driver)
        wait_system()
        nav_wishlist(driver)
        wait_system()
        w_table = get_table_info(driver)
        wait_system()
        wish_dict = get_table_information(w_table)
        wait_system()
        run_test(choose_dict, wish_dict)
    finally:
        close_browser(driver)