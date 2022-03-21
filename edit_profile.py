import main
from selenium.webdriver.common.by import By


class EditationProfile(main.Driver):     
    def __init__(self, browser, url, password, username) -> None:
        super().__init__(browser, url, password, username)

    def get_on_profile_table_page(self):
        self.get_on_page_driver('https://cs.laurie-project.com/profile')

    def edit_input_field(self, input_field, content):
        self.clear_input_field(input_field)
        self.fill_in_input_field(input_field, content)

    def get_first_name_input_field_element(self):
        return self.driver.find_element(By.ID, 'appbundle_users_firstName')

    def get_last_name_input_field_element(self):
        return self.driver.find_element(By.ID, 'appbundle_users_lastName')

    def submit_changes(self):
        password_input_field = self.driver.find_element(By.ID, 'appbundle_users_plainPassword_first')
        password_input_field_confirm = self.driver.find_element(By.ID, 'appbundle_users_plainPassword_second')
        self.edit_input_field(password_input_field, self.password)
        self.edit_input_field(password_input_field_confirm, self.password)
        self.driver.find_element(By.ID, 'appbundle_users_save').click()

    def get_on_edit_profile_page(self):
        self.get_on_page_driver('https://cs.laurie-project.com/profile/edit')

    def get_full_name_from_table(self):
        table = self.driver.find_element(By.TAG_NAME, 'tbody')
        return table.find_elements(By.CLASS_NAME, 'text-left')[0].text

