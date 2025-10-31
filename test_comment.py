# Test Case: Write a Comment
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# function to wait for system
def wait_system():
    time.sleep(2)

# Step 1. Open Chrome Browser
def open_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

# Step 2. Go to the home page
def go_to_homepage(driver):
    driver.get("https://ecommerce-playground.lambdatest.io")

# Step 3. Choose first product and go to its page
def choose_first_product(driver):
    driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=product/category&path=20")
    first_product = driver.find_elements(By.CSS_SELECTOR, ".product-thumb")[0] # First product
    first_product.click()

# Step 4. Clikc 5 stars and write a comment
def write_comment(driver):
    element = driver.find_element(By.CSS_SELECTOR, "input[value='5']")
    driver.execute_script("arguments[0].click();", element)
    driver.find_element(By.CSS_SELECTOR, "input[id='input-name']").send_keys("Test User")
    driver.find_element(By.CSS_SELECTOR, "textarea[id='input-review']").send_keys("This is a test comment for the product. This review should surpass 25 characters in this test case.")
    
# Step 5. Submit commit
def submit_comment(driver):
    driver.find_element(By.CSS_SELECTOR, "button[id='button-review']").click()

# Step 6. Capture success message
def capture_msg(driver):
    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert-success"))
    )
    return success_message
    
# Step 7. Run the test
def run_test(success_message):
    if "Thank you for your review. It has been submitted to the webmaster for approval." in success_message.text:
        print("Test passed: Comment submitted successfully.")
    else:
        print("Test failed: Comment submission unsuccessful.")

# Step 8. Quit the browser
def close_browser(driver):
    driver.quit()

if __name__ == "__main__":
    try:
        driver = webdriver.Chrome()
        wait_system()
        go_to_homepage(driver)
        wait_system()
        choose_first_product(driver)
        wait_system()
        write_comment(driver)
        wait_system()
        submit_comment(driver)
        wait_system()
        success_msg = capture_msg(driver)
        run_test(success_msg)
    finally:
        close_browser(driver)