from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException
import requests


class VirtualPatient:
    def __init__(self, browser, url) -> None:
        self.url = url
        self.browser = browser

    def set_up(self) -> None:
        self.set_up_driver()
        self.driver.get(url)

    def set_up_driver(self):
        if self.browser == 'firefox':
            s = Service('./geckodriver.exe')
            self.driver = webdriver.Firefox(service=s)
        else:
            s = Service('./chromedriver.exe')
            self.driver = webdriver.Chrome(service=s)

    def quit_driver(self):
        self.driver.close()

    def pass_through_notification_element(self):
        self.driver.implicitly_wait(3)
        try:
            self.driver.find_element(By.CLASS_NAME, 'success-button').click()
        except ElementNotInteractableException: 
            ...
        
    def get_scenarios(self):
        return self.driver.find_elements(By.XPATH, '//a[@title="Spustit hru"]')

    def get_links(self):
        scenarios = self.get_scenarios()
        return [element.get_attribute('href') for element in scenarios]

    def article_headings(self):
        scenarios = self.get_scenarios()
        return [element.find_element(By.TAG_NAME, 'h4').text for element in scenarios]
        

    def test_scenarios(self):
        headings = self.article_headings()
        scenarios = self.get_links()
        
        for index, scenario in enumerate(scenarios):
            self.test_server_response(f'{scenario}')
            self.driver.get(scenario)
            current_heading = self.driver.find_element(By.CLASS_NAME, 'scenarioH2title').text
            desirable_heading = headings[index]
            assert current_heading == desirable_heading

    def test_server_response(self, link):
        assert requests.get(link).status_code != 500


if __name__ == '__main__':

    browser = 'firefox'
    url = 'https://cs.laurie-project.com/vp'
    
    test = VirtualPatient(browser, url)
    test.set_up()
    test.pass_through_notification_element()
    headings = test.article_headings()
    test.test_scenarios()
    test.quit_driver()

