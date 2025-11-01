# Test Case: Write a Comment
import time
import pandas as pd
from io import StringIO
from selenium import webdriver
from selenium.webdriver.common.by import By
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
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[title*='Compare'], i.fa-exchange"))
    )
    comp_button.click()
    return product_name, product_price

# Step 1. Open Chrome Browser
def open_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

# Step 2. Go to the home page
def go_to_homepage(driver):
    driver.get("https://ecommerce-playground.lambdatest.io")

# Step 3. Choose first three product and click compare button
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
        print(f"Product{i+1} added to comparison: {product_name} - {product_price}")
        time.sleep(2)
    return choose_product_dict

# Step 4. Click comparison button
def click_comparison(driver):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[aria-label='Compare']"))
    ).click()
    
# Step 5. Use pandas to capture comparison table
def get_table_info(driver):
    html = driver.page_source
    tables = pd.read_html(StringIO(html))
    return tables[1]

# Step 6. Capture need information from table
def get_table_information(c_table):
    comparison_dict = {}
    for i in range(c_table.shape[1] - 1):
        product_name = c_table[f"Product Details.{i+1}"][0]
        product_price = c_table[f"Product Details.{i+1}"][2]
        comparison_dict[f"Product{i+1}"] = {
            "name": product_name,
            "price": product_price
        }
    return comparison_dict
    
# Step 7. Run the test
def run_test(choose_dict, comp_dict):
    if choose_dict == comp_dict:
        print("Test passed: Comparison function works successfully.")
    else:
        print("Test failed: Comparison function works unsuccessful.")

# Step 8. Quit the browser
def close_browser(driver):
    driver.quit()

if __name__ == "__main__":
    try:
        driver = open_browser()
        wait_system()
        go_to_homepage(driver)
        wait_system()
        choose_dict = choose_first_three_product(driver)
        wait_system()
        click_comparison(driver)
        wait_system()
        table = get_table_info(driver)
        wait_system()
        comp_dict = get_table_information(table)
        wait_system()
        run_test(choose_dict, comp_dict)
    finally:
        close_browser(driver)