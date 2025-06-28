from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from Shared.CommonFunction import CommonFunction
import os
import sys

class WebDriverBase:

    def get_chrome_driver(self):
        # Setup Chrome options
        options = webdriver.ChromeOptions()
        
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        # if self.headless:
        #     options.add_argument("--headless")

        # Setup Chrome driver
        try:
            self.driver = webdriver.Chrome(options=options)
            self.driver.implicitly_wait(60)
            self.driver.maximize_window()

            CommonFunction.set_driver(self.driver)
            print("[INFO] Chrome browser launched successfully.")
        except Exception as e:
            print(f"[ERROR] Failed to start Chrome: {e}")
            sys.exit(1)


    def open_url(self, url):
        if self.driver is None:
            print("[ERROR] WebDriver is not initialized.")
            return
        self.driver.get(url)
        print(f"[INFO] Opened URL: {url}")

    def quit_driver(self):
        if self.driver:
            self.driver.quit()
            print("[INFO] Chrome browser closed.")

# Example usage
if __name__ == "__main__":
    browser = WebDriverBase(headless=False)
    driver = browser.get_chrome_driver()
    browser.open_url("https://example.com")
    # Do something with the driver...
    browser.quit_driver()