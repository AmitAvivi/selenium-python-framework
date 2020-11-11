import pytest
from pages.home.login_page import LoginPage
from base.webdriverfactory import WebDriverFactory
from pages.courses.register_courses_page import RegisterCoursesPage

@pytest.yield_fixture()
def setUp():
    print("running conftest method setUp")
    yield
    print("Running conftest method teardown")

@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("running one time setUp")
    wtf = WebDriverFactory(browser)
    driver = wtf.getWebDriverInstance()
    lp = LoginPage(driver)
    lp.login("test@email.com", "abcabc")

    if request.cls:
        request.cls.driver = driver

    yield driver
    coursesPage = RegisterCoursesPage(driver)
    coursesPage.logOut()
    driver.quit()
    print("Running one time teardown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")

