from selenium.webdriver.common.by import By
import time
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging
import os


class SeleniumDriver():
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screenShot(self, resultMessage):
        """
        takes screenshot of the current open web page
        """
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "..\\screenshots\\"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot save to directory: " + destinationFile)
        except:
            self.log.error("### Exception occurred")
            print_stack()

    def getTitle(self):
        return self.driver.title

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator Type" + locatorType + "is not Supported!")
            return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element Found with locator: " + locator +
                          " and locator type: " + locatorType)
        except:
            self.log.info("Element not Found with locator: " +
                          locator + " and locator type: " + locatorType)
        return element

    def getElementList(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info("Element list found with locator: " + locator +
                          " and locatorType: " + locatorType)
        except:
            self.log.info("Element list not found with locator: " + locator +
                          "and locatorType: " + locatorType)
        return element

    def elementClick(self, locator="", locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Element clicked successfully with locator: " +
                          locator + " with locator type: " + locatorType)
        except:
            self.log.info("Cannot click on the element with locator: " +
                          locator + " with locator type: " + locatorType)
            print_stack()

    def sendKeys(self, data, locator="", locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("data sent to element successfully with locator: " +
                          locator + " with locator type: " + locatorType)
        except:
            self.log.info("Cannot sent data to element with locator: " +
                          locator + " with locator type: " + locatorType)
            print_stack()

    def getText(self, locator="", locatorType="id", element=None, info=""):
        try:
            if locator:
                self.log.debug("In locator condition")
                element = self.getElement(locator, locatorType)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element")
            print_stack()
            text = None
        return text

    def isElementPresent(self, locator, locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + locatorType)
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + locatorType)
                return False
        except:
            self.log.info("Element not Found!")
            return False

    def isElementDisplayed(self, locator="", locatorType="id", element=None):
        isDisplayed = False
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator +
                              " locatorType: " + locatorType)
            else:
                self.log.info("Element not displayed with locator: " + locator +
                              " locatorType: " + locatorType)
            return isDisplayed
        except:
            print("Element not found")
            return False

    def elementPresentCheck(self, locator, byType):
        try:
            elementsList = self.driver.find_elements(byType, locator)
            if len(elementsList) > 0:
                self.log.info("Element Found!")
                return True
            else:
                return False
        except:
            self.log.info("Element not Found!")
            return False

    def waitForElement(self, locator, locatorType="id", timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                     ElementNotSelectableException])

            element = wait.until(EC.presence_of_element_located((byType, "stops-0")))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element

    def clearField(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator)
            element.clear()
            self.log.info("Element cleared successfully by locator: " + locator +
                          " and locator type: " + locatorType)
        except:
            self.log.info("Element could not be found or could not br cleared by locator: " + locator +
                          " and locator type: " + locatorType)

    def webScroll(self, direction="up"):
        if direction == "up":
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            self.driver.execute_script("window.scrollBy(0, 1000);")

    def selectDropDownElement(self, dropDownValue="", locator="", locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            sel = Select(element)
            sel.select_by_value(dropDownValue)
            self.log.info("'{}' selected successfully!".format(dropDownValue))
        except:
            self.log.info("'{}' could not be selected in the dropdown element!".format(dropDownValue))
            print_stack()

    def verifyTextOnPage(self, text=""):
        try:
            locator = "//*[contains(text(),'" + text + "')]"
            list = self.getElementList(locator, locatorType="xpath")
            if len(list) > 0:
                self.log.info("Text Found On Page!!!")
                return True
            else:
                self.log.info("Text Not Found On Page!!!")
                return False
        except:
            self.log.error("### An exception occurred!")
            print_stack()
            return False



