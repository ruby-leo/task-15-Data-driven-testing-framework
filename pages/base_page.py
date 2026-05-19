from selenium.common import TimeoutException, ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_webdriver_wait(self):
        return WebDriverWait(self.driver, self.driver.explicit_wait)

    def enter_text(self, locator, text):
        try:
            element = self.get_webdriver_wait().until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
        except TimeoutException:
            print("Timed out: Element not visible or disabled")
            raise

    def click(self, locator):
        def click_action(driver):
            try:
                element = EC.element_to_be_clickable(locator)(driver)
                if element:
                    element.click()
                    return True
            except (ElementClickInterceptedException, StaleElementReferenceException):
                return False
            return False

        try:
            self.get_webdriver_wait().until(click_action)
        except TimeoutException:
            print("Timed out: Element was not clickable")
            raise

    def does_url_contain(self, expected_text):
        try:
            self.get_webdriver_wait().until(EC.url_contains(expected_text))
            return True
        except TimeoutException:
            return False