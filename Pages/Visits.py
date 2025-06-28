from Shared.CommonFunction import CommonFunction
from Shared.CustomBy import By

class VisitsLocator:
    btnCheckIn = "//button[text()= 'Check In']"
    btnCheckout = "//button[text()= 'Check Out']"
    btnCumpulsory = "(//h2[text()= 'Cover block and masking tape distribution'])[2]"
    btnSubmit = "//button[text()= 'Submit']"

class VisitPage(CommonFunction):
    def select_cover_block_and_masking_tape_distribution(self, cover_block, masking_tape):
        self.click_element(By.XPATH, VisitsLocator.btnCumpulsory)

        # cover block
        self.click_element(By.XPATH, f"//label[text()= 'Cover Blocks Distributed ?']/following-sibling::div//button")
        self.click_element(By.XPATH, f"//div[@aria-label= 'Cover Blocks Distributed ?']//span[text()= '{cover_block}']")
        
        # masking tape
        self.click_element(By.XPATH, f"//label[text()= 'Masking Tapes Distributed ?']/following-sibling::div//button")
        self.click_element(By.XPATH, f"//div[@aria-label= 'Masking Tapes Distributed ?']//span[text()= '{masking_tape}']")

        self.click_element(By.XPATH, VisitsLocator.btnSubmit)

    def check_in_visit(self):
        self.click_element(By.XPATH, VisitsLocator.btnCheckIn)

    def check_out_visit(self):
        self.click_element(By.XPATH, VisitsLocator.btnCheckout)