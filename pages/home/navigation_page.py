import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _my_courses = "My Courses" # link text
    _all_courses = "All Courses"  # link text
    _practice = "Practice"  # link text
    _user_icon = "//*[@id='navbar']//a[@aria-expanded='false']"  # xpath

    def navigateToAllCourses(self):
        self.elementClick(locator=self._all_courses, locatorType="link")

    def navigateToMyCourses(self):
        self.elementClick(locator=self._my_courses, locatorType="link")

    def navigateToPractice(self):
        self.elementClick(locator=self._practice, locatorType="link")

    def navigateToUserSettingsIcon(self):
        self.elementClick(locator=self._all_courses, locatorType="xpath")
