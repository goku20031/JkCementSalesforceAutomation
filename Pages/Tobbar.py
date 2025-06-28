from Shared.CommonFunction import CommonFunction
from Shared.CustomBy import By
import time

class TopBarLocator:
    btnHome = "//a[@title= 'Home']"

class TopBarStrings:
    LEADS = "Leads"


class TopBarPage(CommonFunction):
    def navigate_to_tobbar(self, name):
        self.click_element(By.XPATH, f"//a[@title= '{name}]")

    def navigate_to_submenu(self, menu, submenu_name, sleep_time= 2):
        self.click_element(By.XPATH, f"//a[@title= '{menu}]/following=sibling::one-app-nav-bar-item-dropdown")
        self.click_element(By.XPATH, f"//a[@title= '{menu}]/following=sibling::one-app-nav-bar-item-dropdown//span[text()= '{submenu_name}']")
        time.sleep(sleep_time)
