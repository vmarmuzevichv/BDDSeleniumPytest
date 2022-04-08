from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium import webdriver
from config.testdata import TestData


class HomePage(BasePage):
    driver = webdriver.Chrome(executable_path=TestData.CHROME_EX_PATH)

    @property
    def __init__(self, driver):
        super().__init__(driver)

    def get_title(self, title):
        return self.get_title(title)
