from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException


class Driver:
    
    def __init__(self, browser, url, password, username) -> None:
        self.url = url
        self.browser = browser
        self.password = password
        self.username = username

    def get_on_page_driver(self, page) -> None:
        self.driver.get(page)

    def set_up_driver(self):
        if self.browser == 'firefox':
            s = Service('./geckodriver.exe')
            self.driver = webdriver.Firefox(service=s)
        else:
            s = Service('./chromedriver.exe')
            self.driver = webdriver.Chrome(service=s)

    def login(self):
        self.get_on_page_driver('https://cs.laurie-project.com/login')
        self.pass_notification_element()
        username_input_field = self.driver.find_element(By.NAME, '_username')
        password_input_field = self.driver.find_element(By.NAME, '_password')

        self.clear_input_field(username_input_field)
        self.clear_input_field(password_input_field)

        self.fill_in_input_field(username_input_field, self.username)
        self.fill_in_input_field(password_input_field, self.password)

        self.driver.find_element(By.CLASS_NAME, 'login-button').click()

    def clear_input_field(self, input_field_element):
        input_field_element.clear()

    def fill_in_input_field(self, input_field, content):
        input_field.send_keys(content)

    def logout(self):
        self.get_on_page_driver('https://cs.laurie-project.com/logout')

    def pass_notification_element(self):
        self.driver.implicitly_wait(3)
        try:
            self.driver.find_element(By.CLASS_NAME, 'success-button').click()
        except ElementNotInteractableException: 
            ...

    def return_current_url(self):
        return self.driver.current_url

    def quit_driver(self):
        self.driver.close()
