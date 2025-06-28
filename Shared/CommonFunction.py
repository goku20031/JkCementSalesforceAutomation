from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException

class CommonFunction:

    @staticmethod
    def set_driver(driver):
        CommonFunction.driver = driver
    
    def click_element(self, locator, element):
        self.wait_element(locator, element)
        element_to_click = self.driver.find_element(locator, element)
        ActionChains(self.driver).move_to_element(element_to_click).perform()
        element_to_click.click()

    def type_element(self, locator, element, text):
        self.wait_element(locator, element)
        element_to_type = self.driver.find_element(locator, element)
        ActionChains(self.driver).move_to_element(element_to_type).perform()
        element_to_type.clear()
        element_to_type.send_keys(text)

    def wait_element(self, locator, element, timeout= 60):
        try:
            wait = WebDriverWait(self.driver, timeout, poll_frequency= 1, ignored_exceptions=[TimeoutException, ElementNotInteractableException])
            wait.until(EC.element_to_be_clickable((locator, element)))
        except TimeoutException as e:
            wait.until(EC.visibility_of_element_located((locator, element)))
        except Exception as e:
            print(f"Web element not fount {e}")

    def is_element_displayed(self, locator, element):
        return False
