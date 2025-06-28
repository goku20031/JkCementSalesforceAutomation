from Shared.CommonFunction import CommonFunction
from Shared.CustomBy import By
from Pages.Tobbar import TopBarPage
import os, datetime

class LeadsLocator:
    btnAddNew = "//h3[text()= 'Leads']/following-sibling::button[text()= ' + Add New']"
    btnNewSite = "//h3[text()= 'Search']/following-sibling::button[text()= ' + New Site']"
    btnNewInfluencer = "//h3[text()= 'Search']/parent::div//button[text()= ' + New Influencer']"
    btnSubmit = "//span[text()= 'Submit']"
    btnScheduleVisit = "//button[text()= 'Schedule Visit']"

    txtSourceOfLead = "//div[@aria-label= 'Search for Lead Source Type']//input"
    txtSourceOfLeadName = "//div[@aria-label= 'Search for Lead Source']//input"
    txtIHBName = "//input[@placeholder= 'Enter Name']"
    txtIHBPhone = "//label[text()= 'IHB Phone Number']/following-sibling::input[@name= 'phone']"
    txtPincode = "//input[@name= 'pincode']"
    txtProjectSize = "//label[text()= 'Project Size']/following-sibling::input[1]"
    txtBalanceQty = "//label[text()= 'Balance Quantity']/following-sibling::input[1]"
    txtUpcommingSlabDate = "//label[text()= 'Upcoming Slab Date']/following-sibling::input[1]"
    txtNoOfSlabs = "//label[text()= 'No of Slabs']/following-sibling::input[1]"

class LeadStrings:
    INFLUENCER = "Influencer"
    IHB = "IHB"

class ProjectStage:
    LAND = "Land"
    FOUNDATION = "Foundation"
    SLAB = "Slab"
    POSTSLAB = "Post-Slab"
    LINTEL = "Lintel"
    FINISHING = "Finishing"

class InputAriaLabels:
    POTENTIAL_BRAND = "Search for Potential Brand"
    POTENTIAL_PRODUCT = "Search for Potential Product"
    CURRENT_BRAND= "Search for Current Brand"
    PROJECT_TYPE = "Search for Project Type"

class LeadsPage(CommonFunction):
    def click_on_add_new_lead(self):
        self.click_element(By.XPATH, LeadsLocator.btnAddNew)

    def click_on_radio(self, name):
        self.click_element(By.XPATH, f"//label[text()= '{name}']")

    def create_new_lead(self):
        self.click_element(By.XPATH, LeadsLocator.btnAddNew)
        # self.create_new_lead()
        self.click_on_radio(LeadStrings.IHB)
        self.click_element(By.XPATH, LeadsLocator.btnNewSite)

    def enter_source_of_lead(self, source_type, source_name):
        self.type_element(By.XPATH, LeadsLocator.txtSourceOfLead, source_type)
        self.click_element(By.XPATH, f"//div[@aria-label= 'Search for Lead Source Type']/following-sibling::ul//li[text()= '{source_type}']")

        self.type_element(By.XPATH, LeadsLocator.txtSourceOfLeadName, source_name)
        self.click_element(By.XPATH, f"//div[@aria-label= 'Search for Lead Source Type']/following-sibling::ul//li")

    def enter_customer_details(self, customer_type, name, phone, pincode):
        self.click_element(By.XPATH, f"//input[@name= 'Customer Type']/following-sibling::div//div[text()= '{customer_type}']")
        self.type_element(By.XPATH, LeadsLocator.txtIHBName, name)
        self.type_element(By.XPATH, LeadsLocator.txtIHBPhone, phone)
        self.type_element(By.XPATH, LeadsLocator.txtPincode, pincode)

    def select_value_from_dropdown(self, input_label, value):
        self.type_element(By.XPATH, f"//div[@aria-label= '{input_label}']//input", value)
        self.click_element(By.XPATH, f"//div[@aria-label= '{input_label}']/following-sibling::ul//li[text()= '{value}']")

    def select_tags(self, label, tag_name):
        self.click_element(By.XPATH, f"//label[text()= '{label}']/following-sibling::div[@class= 'tags']//div[text()= '{tag_name}']")

    def enter_cement_details(self, no_of_slabs, project_type, project_size, project_stage, balance_qty, potential_brand, potential_product, current_brand, no_of_days, conversion_probability):
        self.type_element(By.XPATH, LeadsLocator.txtNoOfSlabs, no_of_slabs)

        self.select_value_from_dropdown(InputAriaLabels.PROJECT_TYPE, project_type)

        self.type_element(By.XPATH, LeadsLocator.txtProjectSize, project_size)
        self.select_tags("Project Stage", project_stage)
        self.type_element(By.XPATH, LeadsLocator.txtBalanceQty, balance_qty)

        self.select_value_from_dropdown(InputAriaLabels.POTENTIAL_BRAND, potential_brand)
        if potential_brand == 'JK Super':
            self.select_value_from_dropdown(InputAriaLabels.POTENTIAL_PRODUCT, potential_product)

        self.select_value_from_dropdown(InputAriaLabels.CURRENT_BRAND, current_brand)

        upcommingDate = self.add_days_to_today(no_of_days)
        self.type_element(By.XPATH, LeadsLocator.txtUpcommingSlabDate, upcommingDate)

        self.select_tags("Conversion Probability", conversion_probability)

    def click_submit(self):
        self.click_element(By.XPATH, LeadsLocator.btnSubmit)

    def schedule_visit(self, date= None, time= None):
        self.click_element(By.XPATH, LeadsLocator.btnScheduleVisit)
        if date == None:
            date = self.add_days_to_today(0, '%b %d, %Y')

        self.type_element(By.XPATH, "//label[text()= 'Date']/following-sibling::div//input[@name= 'Visit Date']", date)
        
        if time != None:
            time = datetime.strptime(time, "%H:%M").strftime("%I:%M %p").lstrip("0")

            self.type_element(By.XPATH, "//label[text()= 'Time']/following-sibling::div//input[@name= 'Visit Date']", time)

        self.click_element(By.XPATH, "//span[@label= 'Schedule Visit']")
    
    def input_ihb_site_details_form(self, lead_source_type, lead_phone_no, customer_type, 
                                    ihb_name, phone_no, pincode, no_of_slab, project_type, project_size, 
                                    project_stage, balance_qty, potential_brand, potential_product, current_brand, 
                                    slab_date, conversion_probability):
        self.enter_source_of_lead(lead_source_type, lead_phone_no)

        self.enter_customer_details(customer_type, ihb_name, phone_no, pincode)

        self.enter_cement_details(no_of_slab, project_type, project_size, project_stage, balance_qty, potential_brand, potential_product, current_brand,slab_date, conversion_probability)