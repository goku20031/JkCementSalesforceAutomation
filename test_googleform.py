from Shared.WebDriverBase import WebDriverBase
from Shared.CommonFunction import CommonFunction
from Shared.CustomBy import By
from Pages.GoogleFormPage import GoogleFormPage
from Constants.Literels import urls
import random

class GoogleFormTest(WebDriverBase):

    @classmethod
    def setupClass(self):
        self.cf = CommonFunction()
        self.obj_googleForm = GoogleFormPage()

    def enter_entries_in_google_form(self, date_list, no_of_entries= 3, skip_date_list= []):
        month = '05'
        year = '2025'
        try:
            self.get_chrome_driver()
            self.open_url(urls.googleForm)

            for i in range(no_of_entries):
                for date in date_list:
                    if date in (1,2,3):
                        date = f"0{date}"
                    if date in skip_date_list:
                        continue


                    self.obj_googleForm.select_dropdown('State', 'GUJARAT')
                    self.obj_googleForm.enter_value_in_textbox('Area Office', "Ahmedabad")
                    self.obj_googleForm.enter_value_in_textbox('Name of Employee', 'Jatin Trivedi')
                    self.obj_googleForm.enter_value_in_textbox('Emp Code', '13003621')
                    self.obj_googleForm.enter_value_in_textbox('Where demo done', 'Ahmedabad')
                    self.obj_googleForm.enter_value_in_textbox('Date of Test', f"{date}{month}{year}")

                    self.obj_googleForm.select_dropdown('Ball Test Done', 'Super Strong')

                    winner = ['JK Super', 'Competition']
                    self.obj_googleForm.select_dropdown('Winner in Ball Test', random.choice(winner))

                    self.cf.type_element(By.XPATH, "(//span[contains(text(), 'Drop Test')]//ancestor::div[@jscontroller]//input)[1]", '11')
                    self.cf.type_element(By.XPATH, "(//span[contains(text(), 'Beaker Test')]//ancestor::div[@jscontroller]//input)[1]", '300')
                    
                    competitionBrand = ['Ambuja', 'Ultratech', 'Wonder', 'JK Lakshmi']
                    self.obj_googleForm.select_dropdown('Brand Name', random.choice(competitionBrand))
                    self.obj_googleForm.select_dropdown('Product Type', 'PPC')

                    self.obj_googleForm.enter_value_in_textbox('Plant Name', 'Balasinor')
                    
                    self.cf.type_element(By.XPATH, "(//span[contains(text(), 'Drop Test')]//ancestor::div[@jscontroller]//input)[2]", '3')
                    self.cf.type_element(By.XPATH, "(//span[contains(text(), 'Beaker Test')]//ancestor::div[@jscontroller]//input)[2]", '5')

                    self.obj_googleForm.submit_form()
        
        except Exception as e:
            print(e)
        finally:
            self.quit_driver()

if __name__ == "__main__":
    GoogleFormTest.setupClass()
    GoogleFormTest().enter_entries_in_google_form()
    print("ssss")