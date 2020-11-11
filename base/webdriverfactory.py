from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging

class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        baseUrl = "https://letskodeit.teachable.com/"
        if self.browser == "iexplorer":
            # set IE driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            # set chrome driver
            opt = webdriver.ChromeOptions()
            opt.add_argument("user-data-dir=C:\\Users\\Owner\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
            driver = webdriver.Chrome(options=opt)
        else:
            opt = webdriver.ChromeOptions()
            opt.add_argument("user-data-dir=C:\\Users\\Owner\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
            driver = webdriver.Chrome(options=opt)

        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseUrl)
        return driver





