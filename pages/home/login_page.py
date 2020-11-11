import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _Login_Link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"


    def clickLoginLink(self):
        self.elementClick(self._Login_Link, locatorType="link")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//*[@id='navbar']//span[text()='Test Account']",
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[contains(text(),'Invalid email or password')]",
                                     locatorType="xpath")
        return result

    def clearEmailField(self):
        self.clearField(self._email_field)

    def clearPasswordField(self):
        self.clearField(self._password_field)

    def verifyLoginTitle(self):
        return self.verifyPageTitle("let's kode it")

