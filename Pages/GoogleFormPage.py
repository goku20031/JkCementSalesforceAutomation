from Shared.CommonFunction import CommonFunction
from Shared.CustomBy import By
import time

class GoogleFormLocator:
    dropDownState = "//div[@role= 'option']//span[text()= 'Choose'][1]"
    txtAreaOffice = "//span[contains(text(), '{}')]//ancestor::div[@jscontroller]//input"
    btnSubmit = "//span[text() = 'Submit']"
    btnSwitchAccount = "//a[text()= 'Switch accounts']"
    currentAccount = "//a[text()= 'Switch accounts']/parent::div//span"
    btnSignIn = "//a[text() = 'Sign in to Google']"

class GoogleFormPage(CommonFunction):
    def select_dropdown(self, field_label, value):
        time.sleep(2)
        self.click_element(By.XPATH, f"//span[contains(text(), '{field_label}')]//ancestor::div[@jscontroller]//span[text() = 'Choose']")
        self.click_element(By.XPATH, f"//span[contains(text(), '{field_label}')]//ancestor::div[@jscontroller]//div[@role= 'option' and @data-value = '{value}']")
        time.sleep(2)

    def enter_value_in_textbox(self, label, value):
        self.type_element(By.XPATH, f"//span[contains(text(), '{label}')]//ancestor::div[@jscontroller]//input", value)

    def submit_form(self):
        self.click_element(By.XPATH, GoogleFormLocator.btnSubmit)

    def sign_in_to_google_account(self, email):
        if self.get_signed_in_google_account():
            pass
        self.click_element(By.XPATH, GoogleFormLocator.btnSignIn)

    def submit_another_response(self):
        pass

    def get_all_accounts_displayed(self):
        pass

    def get_signed_in_google_account(self):
        return None

    def switch_account(self, email):
        self.click_element(By.XPATH, GoogleFormLocator.btnSwitchAccount)

    def is_form_displayed(self, form_title):
        self.is_element_displayed(By.XPATH, f"//div[text()= {form_title}]")

