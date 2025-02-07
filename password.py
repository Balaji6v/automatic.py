from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver_path = "C:\\Windows\\chromedriver-win64\\chromedriver.exe"
service = Service(driver_path)


driver = webdriver.Chrome(service=service)


driver.get("https://www.saucedemo.com/")
driver.maximize_window()


username_field = driver.find_element(By.ID, "user-name")
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

username_field.send_keys("standard_user")
password_field.send_keys("secret_sauce")
login_button.click()


time.sleep(3)


print("Page Title:", driver.title)


products = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
print("Available Products:")
for product in products:
    print("-", product.text)


driver.quit()



