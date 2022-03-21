import virtual_patient as vp
import unittest
import requests


class TestVirtualPatient(unittest.TestCase):

    BROWSER = 'chrome'
    URL = 'https://cs.laurie-project.com/vp'
    PASSWORD = 'Provizorni_Heslo123'
    USERNAME = 'adamvirostko'
    
    FIRST_NAME_FIELD_INDEX = 0
    LAST_NAME_FIELD_INDEX = 1

    test_case = None

    # Test case initialization

    def setUp(self) -> None:
        self.test_case = vp.VirtualPatient(self.BROWSER, self.URL, self.PASSWORD, self.USERNAME)
        self.test_case.set_up_driver()

    def tearDown(self) -> None:
        self.test_case.quit_driver()

    # Help methods

    def loop_through_scenario_pages(self):
        links_scenarios = self.test_case.bind_link_with_heading()
        for link in links_scenarios:
            self.assertNotEqual(requests.get(link).status_code, 500)
            self.test_case.get_on_page_driver(link)
            current_heading = self.test_case.get_current_page_heading()
            self.assertEqual(links_scenarios[link], current_heading)

    # Test suite

    def test_getting_all_scenarios_logged_out(self):
        self.test_case.get_on_page_driver(self.URL)
        self.test_case.pass_notification_element()
        patient_scenarios = self.test_case.get_scenarios()
        self.assertEqual(len(patient_scenarios), 10)

    def test_getting_all_scenarios_logged_in(self):
        self.test_case.login()
        self.test_case.get_on_page_driver(self.URL)
        patient_scenarios = self.test_case.get_scenarios()
        self.assertEqual(len(patient_scenarios), 10)

    def test_get_on_every_scenario_page_logged_out(self):
        self.test_case.get_on_page_driver(self.URL)
        self.test_case.pass_notification_element()
        self.loop_through_scenario_pages()

    def test_get_on_every_scenario_page_logged_in(self):
        self.test_case.login()
        self.test_case.get_on_page_driver(self.URL)
        self.loop_through_scenario_pages()


if __name__ == '__main__':
    unittest.main()
