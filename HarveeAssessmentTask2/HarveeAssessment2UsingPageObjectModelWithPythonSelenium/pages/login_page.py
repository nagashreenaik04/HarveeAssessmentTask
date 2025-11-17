from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    #locators
    logIn_heading = (By.XPATH, "//span[text()='Log In']")
    email_field = (By.XPATH, '//input[@placeholder="Email Address"]')
    password_field = (By.XPATH, '//input[@placeholder="Password"]')
    logIn_btn = (By.ID, 'signinbutton')

    #logout
    dropdown = (By.ID, "logout")
    logout_btn = (By.LINK_TEXT, "Log out")

    def get_login_heading(self):
        return self.find_element(self.logIn_heading).text

    def enter_email(self, email):
        self.send_keys(self.email_field, email)

    def enter_password(self, password):
        self.send_keys(self.password_field, password)

    def click_login_btn(self):
        self.click(self.logIn_btn)

    def click_dropdown(self):
        self.click(self.dropdown)

    def click_logout(self):
        self.click(self.logout_btn)

