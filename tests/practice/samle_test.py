from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#nexportPage = NexportPage('chrome')
#scenarios('../features/login.feature')
#driver = webdriver.Chrome(executable_path="/Users/vmarmuzevich/Downloads/chromedriver")
driver = webdriver.Chrome(ChromeDriverManager().install())



def test_0():
    driver.get()