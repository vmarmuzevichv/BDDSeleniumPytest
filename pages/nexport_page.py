from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium import webdriver
from config.testdata import TestData

class NexportPage(BasePage):
    driver = webdriver.Chrome(executable_path=TestData.CHROME_EX_PATH)


    loginButton = (By.LINK_TEXT, "login")
    usernameInput = (By.XPATH, "//input[@name='username']")
    passwordInput = (By.XPATH, "//input[@name='username']")
    enterButton = (By.XPATH, "//button[@type='submit']")
    def __init__(self, driver):
        super().__init__(driver)

    def do_login(self, username, password):
        self.do_send_keys(self.usernameInput, username)
        self.do_send_keys(self.passwordInput, password)
        self.do_click(self.enterButton)


