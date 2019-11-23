from traceback import print_stack

from selenium.webdriver.common.by import By

class SeleniumDriver():

    def getByLocator(self, locatorType):
        locatorType = locatorType.lower()

        if(locatorType == "xpath"):
            return By.XPATH
        elif(locatorType == "css"):
            return By.CSS_SELECTOR
        elif(locatorType == "linktext"):
            return By.LINK_TEXT
        elif(locatorType == "id"):
            return By.ID
        elif(locatorType == "name"):
            return By.NAME
        elif(locatorType == "class"):
            return By.CLASS_NAME
        elif(locatorType == "partiallinktext"):
            return By.PARTIAL_LINK_TEXT
        elif(locatorType == "tagname"):
            return By.TAG_NAME
        else:
            print("Unauthorize Locator Type:" + locatorType + "mentioned.")
            return False

    def getlocator(self, driver, locatorValue, locator="id"):
        self.element = None
        try:
            self.locator = self.getByLocator(locator)
            self.element = driver.findElement(self.locator, locatorValue)
            print("Element with locator " + self.locator + " locator value " + locatorValue + " found")

        except:
            print("Element with locator " + self.locator + " locator value " + locatorValue + " not found")
        return self.element

    def clickOnElement(self, driver, locatorValue, locator="id"):
        try:
            self.element = self.getlocator(driver, locatorValue, locator)
            self.element.click()
            print("Element with locator " + self.locator + " locator value " + locatorValue + " clicked")
        except:
            print("Element with locator " + self.locator + " locator value " + locatorValue + " not clicked")
            print_stack()

    def getElementText(self, driver, locatorValue, locator="id"):
        self.element = None
        self.actualText = ""
        try:
            self.element = self.getlocator(driver, locatorValue, locator)
            self.actualText = self.element.getText()
            print("Element text with locator " + self.locator + " locator value " + locatorValue + " found")
        except:
            print("Element text with locator " + self.locator + " locator value " + locatorValue + " not found")
            print_stack()
        return self.actualText

    def isElementPresent(self, driver, locatorValue, locator):
        self.element = None
        try:
            self.element = self.getlocator(driver, locator, locatorValue)
            if self.element is not None:
                print("Element " + self.element + " found")
                return True
            else:
                print("Element " + self.element + " not found")
                return False
        except:
            print("Element " + self.element + " not found")
            return False