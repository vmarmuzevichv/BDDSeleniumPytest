from pytest_bdd import scenarios, given, when, then
from pages.login_page import NexportPage

nexportPage = NexportPage()
#basePage = BasePage()

scenarios('../features/login.feature')
#web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EX_PATH)



#@pytest.mark.usefixtures("init_driver")
#@scenarios("Login")
@given("User on the Nexport login page")
def test_user_on_the_nexport_page():
    print("Hello world")
    #basePage.driver.get(TestData.BASE_URL)

@when('User uses correct credentials')
def test_login_nexport():
    print("Hello world1")
    #nexportPage.do_login(TestData.LOGIN, TestData.PASSWORD )

@then("User should see home page")
def test_title_assertions():
    print("Hello world3")
    #title = nexportPage.get_title(TestData.HOME_PAGE_TITLE)
    #assert title == TestData.HOME_PAGE_TITLE




