import main
from selenium.webdriver.common.by import By


class EditProfile(main.Driver):
    def __init__(self, url, browser, username, password) -> None:
        self.url = url
        self.browser = browser
        self.username = username
        self.password = password

    def get_on_profile_table_page(self):
        self.get_on_page_driver('https://cs.laurie-project.com/profile')

    def edit_input_field(self, input_field, content):
        self.clear_input_field(input_field)
        self.fill_in_input_field(input_field, content)

    def submit_changes(self):
        self.driver.find_element(By.ID, 'appbundle_users_save').click()

    def get_on_edit_profile_page(self):
        self.get_on_page_driver('https://cs.laurie-project.com/profile/edit')

    def get_full_name_from_table(self):
        table = self.driver.find_element(By.TAG_NAME, 'tablebody')
        return [self.driver.find_element(By.CLASS_NAME, 'text-left').text for table_value in table][0]




