from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    username_textbox = (By.NAME, "username")
    password_textbox = (By.NAME, "password")
    login_button = (By.CLASS_NAME, "orangehrm-login-button")

    def enter_username(self, username):
        self.enter_text(self.username_textbox, username)

    def enter_password(self, password):
        self.enter_text(self.password_textbox, password)

    def click_login(self):
        self.click(self.login_button)