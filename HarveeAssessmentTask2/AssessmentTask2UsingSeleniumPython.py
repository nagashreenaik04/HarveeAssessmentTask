import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class TestLoginMedycn:

    url = "https://jithya.sandboxtrial.com/login?&chkie=true"
    email = "nagashreenaik040@gmail.com"
    password = "Shree@123"
    expected_dashboard_url = "https://jithya.sandboxtrial.com/dashboard"

    # Set up Chrome options
    options = Options()
    options.add_experimental_option("detach", True)  # Keep browser open after tests

    # Set up WebDriver
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    # Go to Login Page
    driver.get(url)
    print("Navigated to Login Page")

    # Maximize Window
    driver.maximize_window()
    print("Browser maximized")

    # Enter Email
    driver.find_element(By.XPATH, '//input[@placeholder="Email Address"]').send_keys(email)

    # Enter Password
    driver.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys(password)

    # Click Login Button
    driver.find_element(By.ID, "signinbutton").click()
    time.sleep(5)

    # ---- Verify Login ----
    current_url = driver.current_url
    print(f"Current URL After Login: {current_url}")

    assert current_url == expected_dashboard_url, "Login Failed"
    print(" Login Successful")

    # ---- Logout Section ----
    # Click Dropdown Button
    driver.find_element(By.ID, "logout").click()
    time.sleep(2)

    # Click Logout
    driver.find_element(By.LINK_TEXT, "Log out").click()
    time.sleep(5)

    # ---- Verify Logout ----
    current_url_after_logout = driver.current_url
    print(f"URL after logout: {current_url_after_logout}")
    assert current_url_after_logout == url, "Logout failed: Not redirected to login page"
    print("Logout verified successfully.")

    # Close browser
    driver.quit()
