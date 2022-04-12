from selenium.webdriver.common.by import By
from config.testdata import TestData
from pages.base_page import BasePage


class LoginPage(BasePage):

    LOGIN_BUTTON = (By.LINK_TEXT, "login")
    USERNAME_INPUT = (By.XPATH, "//input[@name='username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='username']")
    ENTER_BUTTON = (By.XPATH, "//button[@type='submit']")

    """constructor for the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

        """Page Actions"""

    """this is used to log in"""
    def do_login(self, username, password):
        self.do_send_keys(self.USERNAME_INPUT, username)
        self.do_send_keys(self.PASSWORD_INPUT, password)
        self.do_click(self.ENTER_BUTTON)

    """this is used to get the page title"""
    def get_login_page_title(self, title):
        return self.get_title(title)

    """this is used to check enter button"""
    def is_enter_button_exit(self):
        return self.is_visible(self.ENTER_BUTTON)



