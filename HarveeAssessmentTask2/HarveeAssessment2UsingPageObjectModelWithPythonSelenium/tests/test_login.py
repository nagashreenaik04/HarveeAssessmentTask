import pytest
from pages.login_page import LoginPage
from utilities.custom_logger import LogGen
import time

logger = LogGen.loggen()

@pytest.mark.usefixtures("driver")  # Assumes you have a driver fixture
class TestLogin:

    url = "https://jithya.sandboxtrial.com/login?&chkie=true"
    email = "nagashreenaik040@gmail.com"
    password = "Shree@123"
    expected_dashboard_url = "https://jithya.sandboxtrial.com/dashboard"  # Replace with actual URL after login

    def test_login_and_logout(self, driver):
        # Navigate to login page
        logger.info("Navigating to login page...")
        driver.get(self.url)
        logger.info(f"Current URL: {driver.current_url}")

        # Login
        login_page = LoginPage(driver)
        logger.info("Entering email...")
        login_page.enter_email(self.email)
        logger.info("Entering password...")
        login_page.enter_password(self.password)
        logger.info("Clicking login button...")
        login_page.click_login_btn()

        # Wait for dashboard to load
        time.sleep(5)
        dashboard_url = driver.current_url
        logger.info(f"Dashboard URL: {dashboard_url}")

        # Verify login success
        assert dashboard_url == self.expected_dashboard_url, "Login failed: Dashboard URL mismatch"
        logger.info("Login verified successfully.")

        # Logout
        logger.info("Clicking user dropdown for logout...")
        login_page.click_dropdown()
        time.sleep(2)  # Wait for dropdown to open
        logger.info("Clicking logout button...")
        login_page.click_logout()
        time.sleep(3)  # Wait for logout to complete

        # Verify logout success by checking current URL
        current_url_after_logout = driver.current_url
        logger.info(f"URL after logout: {current_url_after_logout}")
        assert current_url_after_logout == self.url, "Logout failed: Not redirected to login page"
        logger.info("Logout verified successfully.")
