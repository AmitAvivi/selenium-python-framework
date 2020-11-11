import utilities.custom_logger as cl
import logging
from traceback import print_stack
from base.basepage import BasePage
from utilities.util import Util


class RegisterCoursesPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        util = Util()


    # error message = "Sorry, there was an error completing your purchase -- please try again."
    # Locators

    _options_icon = "//*[@id='navbar']//a[@aria-expanded='false']"  # xpath
    _log_out_button = "//*[@id='navbar']//a[@href='/sign_out']"  # xpath
    _search_box = "search-courses"  # id
    _all_courses = "All Courses"  # link text
    _course = "//a[@href='/p/complete-javascript-guide']/div"  # xpath
    _enroll_button = "enroll-button"  # id
    _country_select = "cardCountry"  # id
    _postal_code_field = "billingPostalCode"  # id
    _submit_button = "//*[@data-test='confirm-enroll']"  # xpath

    def clickIconLink(self):
        self.elementClick(self._options_icon, locatorType="xpath")

    def clickLogOutButton(self):
        self.elementClick(self._log_out_button, locatorType="xpath")

    def logOut(self):
        self.clickIconLink()
        self.clickLogOutButton()
        self.util.sleep(3)

    def verifyUserLogOut(self):
        result = self.isElementDisplayed(self._options_icon, locatorType="xpath")
        if result:
            self.log.error("### User is Not Logged Out!")
            print_stack()
            return False
        else:
            self.log.info("### Log Out Verified!!!")
            return True

    def enterCourseName(self, courseName=""):
        self.sendKeys(data=courseName, locator=self._search_box)

    def clickAllCoursesButton(self):
        self.elementClick(locator=self._all_courses, locatorType="link")

    def clickJavaScriptCourse(self):
        self.elementClick(locator=self._course, locatorType="xpath")

    def clickEnrollButton(self):
        self.elementClick(locator=self._enroll_button)

    def selectCountryDropDown(self, countryName):
        self.selectDropDownElement(dropDownValue=countryName, locator=self._country_select)

    def enterPostalCode(self, code=""):
        self.sendKeys(code, locator=self._postal_code_field)

    def clickSubmitButton(self):
        self.elementClick(locator=self._submit_button, locatorType="xpath")

    def verifyErrorMessageExist(self, message=""):
        self.verifyTextOnPage(message)

    def scrollToBottom(self):
        for i in range(4):
            self.webScroll(direction="down")

    def scrollToTop(self):
        for i in range(4):
            self.webScroll(direction="up")


