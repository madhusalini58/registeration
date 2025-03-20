from selenium import webdriver
from selenium.webdriver.common.by import By
import time

test_cases = [
    {
        "fullName": "User MissingPhone",
        "username": "usernopho",
        "email": "nopho@example.com",
        "phoneNumber": "",
        "password": "password123",
        "confirmPassword": "password123",
        "gender": "male"  # Use actual values from the HTML
    },
    {
        "fullName": "User ShortPass",
        "username": "shortpassuser",
        "email": "shortpass@example.com",
        "phoneNumber": "9999999992",
        "password": "123",
        "confirmPassword": "123",
        "gender": "female"  # Use actual values from the HTML
    },
    {
        "fullName": "Mismatch User",
        "username": "mismatchuser",
        "email": "mismatch@example.com",
        "phoneNumber": "9999999993",
        "password": "password123",
        "confirmPassword": "different123",
        "gender": "other"  # Use actual values from the HTML
    },
    {
        "fullName": "Success User",
        "username": "successuser",
        "email": "success@example.com",
        "phoneNumber": "9999999994",
        "password": "validpass123",
        "confirmPassword": "validpass123",
        "gender": "male"  # Use actual values from the HTML
    }
]

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5000/")

for test in test_cases:

    driver.refresh()
    time.sleep(1)

    # Fill out the form fields based on the test data
    driver.find_element(By.ID, "fullname").send_keys(test["fullName"])
    driver.find_element(By.ID, "username").send_keys(test["username"])
    driver.find_element(By.ID, "email").send_keys(test["email"])
    driver.find_element(By.ID, "phone").send_keys(test["phoneNumber"])
    driver.find_element(By.ID, "password").send_keys(test["password"])
    driver.find_element(By.ID, "confirmPassword").send_keys(test["confirmPassword"])

    # Select the gender radio button
    gender_radio = driver.find_element(By.ID, test["gender"])  # Use the gender value directly
    gender_radio.click()

    # Click the submit button
    driver.find_element(By.CSS_SELECTOR, ".fullbut").click()
    time.sleep(2)

    # Check for error or success message
    try:
        msg = driver.find_element(By.ID, "errorMessages").text
    except:
        msg = "No error message found"
    
    print(f"Test for {test['fullName']} - Result: {msg}")

    time.sleep(3)

driver.quit()