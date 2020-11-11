from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import T_estStatus
from pages.home.login_page import LoginPage
from utilities.util import Util
import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
from pages.home.navigation_page import NavigationPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = T_estStatus(self.driver)
        self.lg = LoginPage(self.driver)
        self.util = Util()
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.nav.navigateToAllCourses()

    @pytest.mark.run(order=1)
    @data(*getCSVData(r"C:\Users\Owner\workspace_python\letskodeit\testdata.csv"))
    @unpack
    def test_invalidEnrollment(self, course_name, country_name, postal_code):
 #       self.lg.login("test@email.com", "abcabc")
    #    self.courses.clickAllCoursesButton()
        self.courses.enterCourseName(courseName=course_name)
        self.courses.clickJavaScriptCourse()
        self.courses.scrollToBottom()
        self.courses.clickEnrollButton()
        self.courses.scrollToBottom()
        self.courses.selectCountryDropDown(countryName=country_name)
        self.courses.enterPostalCode(code=postal_code)
        self.courses.clickSubmitButton()
        self.courses.scrollToTop()
        self.util.sleep(3)
        result1 = self.courses.verifyTextOnPage("Sorry, there was an error completing your purchase -- please try again.")
    #    self.ts.mark(result1, "Text verified")
        self.ts.markFinal("test_invalidEnrollment", result1, "Text verified")

        self.driver.back()
   #     self.courses.logOut()
     #   result2 = self.courses.verifyUserLogOut()
    #    self.ts.markFinal("test_invalidEnrollment", result2, "logout successful")
      #  self.util.sleep(2)






