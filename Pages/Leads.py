from Shared.CommonFunction import CommonFunction
from Shared.CustomBy import By
from Pages.Tobbar import TopBarPage

class LeadsLocator:
    btnAddNew = "//h3[text()= 'Leads']/following-sibling::button[text()= ' + Add New']"
    btnNewSite = "//h3[text()= 'Search']/following-sibling::button[text()= ' + New Site']"
    btnNewInfluencer = "//h3[text()= 'Search']/parent::div//button[text()= ' + New Influencer']"

class LeadStrings:
    INFLUENCER = "Influencer"
class LeadsPage(CommonFunction):
    def click_on_add_new_lead(self):
        self.click_element(By.XPATH, LeadsLocator.btnAddNew)

    def click_on_radio(self, name):
        self.click_element(By.XPATH, f"//label[text()= '{name}']")

    def create_new_lead(self):
        self.click_element(By.XPATH, LeadsLocator.btnAddNew)
        self.create_new_lead()
        self.click_on_radio(LeadStrings.INFLUENCER)

    def input_ihb_site_details_form(self, lead_source, ihb_name, phone_no, pincode, project_size, project_stage, balance_qty, potential_brand, potential_product, current_brand, slab_date):
        pass