

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def login_HomePage(self, username, password):


        element = self.driver.find_element_by_xpath("//a[contains(text(), 'Login')]")
        element.click()

        element = self.driver.find_element_by_id("user_email")
        element.send_keys(username)

        element = self.driver.find_element_by_id("user_password")
        element.send_keys(password)

        element = self.driver.find_element_by_name("commit")
        element.click()