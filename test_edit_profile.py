import unittest
import edit_profile as ep


class TestEditProfile(unittest.TestCase):           
    
    BROWSER = 'chrome'
    URL = 'https://cs.laurie-project.com/'
    PASSWORD = 'Provizorni_Heslo123'
    USERNAME = 'adamvirostko'
    
    FIRST_NAME_FIELD_INDEX = 0
    LAST_NAME_FIELD_INDEX = 1

    test_case = None

    # Test case initialization

    def setUp(self) -> None:
        self.test_case = ep.EditationProfile(self.BROWSER, self.URL, self.PASSWORD, self.USERNAME)
        self.test_case.set_up_driver()

    def tearDown(self):
        self.test_case.quit_driver()

    # Help methods

    def edit_input_field_procedure(self, input_field, content):
        self.test_case.edit_input_field(input_field, content)
        self.test_case.submit_changes()

    def get_input_elements(self):
        self.test_case.get_on_edit_profile_page()
        first_name = self.test_case.get_first_name_input_field_element()
        last_name = self.test_case.get_last_name_input_field_element()
        return first_name, last_name

    def get_full_name_procedure(self):
        self.test_case.get_on_profile_table_page()
        full_name = self.test_case.get_full_name_from_table()
        return full_name        
        
    def invalid_editation(self, desired_input_field, content):
        self.test_case.login()
        input_field = self.get_input_elements()[desired_input_field]
        full_name = self.get_full_name_procedure()
        self.edit_input_field_procedure(input_field, content)
        self.assertEqual(self.test_case.driver.current_url, 'https://cs.laurie-project.com/profile/edit/')
        self.test_case.get_on_profile_table_page()
        self.assertEqual(full_name, self.test_case.get_full_name_from_table())

    # Test suite

    def test_signed_out_user_redirection_to_login_page(self):
        self.test_case.get_on_profile_table_page()
        #self.test_case.driver.implicitly_wait(3)       
        self.assertEqual(self.test_case.driver.current_url, 'https://cs.laurie-project.com/login')

    def test_valid_profile_editation(self):
        self.test_case.login()
        self.test_case.get_on_edit_profile_page()
        first_name_input = self.test_case.get_first_name_input_field_element()
        last_name_input = self.test_case.get_last_name_input_field_element()
        self.test_case.edit_input_field(first_name_input, 'Jan')
        self.test_case.edit_input_field(last_name_input, 'Novák')
        self.test_case.get_on_profile_table_page()
        self.assertEqual(self.test_case.get_full_name_from_table, 'Jan Novák')

    def test_invalid_empty_input_profile_editation(self):
        self.invalid_editation(self.FIRST_NAME_FIELD_INDEX, '')

    def test_invalid_digit_input_profile_editation(self):
        # depends on client's requirements, assuming this input is invalid
        self.invalid_editation(self.FIRST_NAME_FIELD_INDEX, '5')


if __name__ == '__main__':
    unittest.main()
