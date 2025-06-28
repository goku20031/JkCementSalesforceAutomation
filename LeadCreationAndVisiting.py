from Shared.WebDriverBase import WebDriverBase
from Shared.CommonFunction import CommonFunction
from Shared.CustomBy import By
from Pages.Leads import LeadsPage
from Pages.Tobbar import TopBarPage, TopBarStrings
from Constants.Literels import urls
import random, os
import pandas as pd

class LeadCreationAndVisiting(WebDriverBase):

    @classmethod
    def setupClass(self):
        self.cf = CommonFunction()
        self.obj_leads = LeadsPage()
        self.obj_topBar = TopBarPage()

    def enter_entries_in_google_form(self):
        month = '05'
        year = '2025'
        fileName = os.path.join(os.getcwd(), "Resources/SalesForceLeadData.xlsx")
        try:
            self.get_chrome_driver()
            # self.open_url(urls.googleForm)

            df = pd.read_excel(fileName)

            for index, row in df.iterrows():
                leadSourceType = row['Source of Lead']
                leadPhoneNo = row['Enter phone number']
                customerType = row['Customer type']
                ihbName = row['ihb name']
                phoneNo = row['ihb phone number ']
                pincode = row['pincode']
                NoofSlab = row['no. of slab']
                projectType = row['project type']
                projectSize = row['project size']
                projectStage = row['project stage']
                bagQty = row['bag qty']
                potentialBrand = row['potential brand']
                potentialProduct = row['potential product']
                currentBrand = row['current brand']
                slabDate = int(row['upcoming slab date'])
                conversionProbability = row['conversion probability']


                # self.obj_topBar.navigate_to_tobbar(TopBarStrings.LEADS)

                # self.obj_leads.input_ihb_site_details_form(leadSourceType, leadPhoneNo, customerType, ihbName, phoneNo, pincode, 
                #                                             NoofSlab, projectType, projectSize, projectStage, bagQty, potentialBrand, 
                #                                             potentialProduct, currentBrand, slabDate, conversionProbability)


            
        except Exception as e:
            print(e)
        finally:
            self.quit_driver()

if __name__ == "__main__":
    LeadCreationAndVisiting.setupClass()
    LeadCreationAndVisiting().enter_entries_in_google_form()

    print("ssss")