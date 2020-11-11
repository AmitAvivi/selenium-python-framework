from pages.home.login_page import LoginPage
import unittest
import pytest
from utilities.teststatus import T_estStatus
from pages.courses.register_courses_page import RegisterCoursesPage

# chrome://version/
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = T_estStatus(self.driver)
        self.rc = RegisterCoursesPage(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1, "Title verified")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result2, "Login was successful")
        self.rc.logOut()
        self.rc.verifyUserLogOut()

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.rc.logOut()
        self.lp.login("test@email.com", "abcabcabc")
        result = self.lp.verifyLoginFailed()
        assert result == True
        self.lp.clearEmailField()
        self.lp.clearPasswordField()
