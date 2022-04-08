import pytest
from pytest_bdd import scenario, scenarios, given, when, then, parser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from config.testdata import TestData
from pages.nexport_page import NexportPage
#nexportPage = NexportPage('chrome')
#scenarios('../features/login.feature')
driver = webdriver.Chrome(executable_path="/Users/vmarmuzevich/Downloads/chromedriver")



def test_0():
    driver.get("https://www.google.com/")