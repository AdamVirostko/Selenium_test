import main
from selenium.webdriver.common.by import By


class VirtualPatient(main.Driver):
    def __init__(self, browser, url, password, username) -> None:
        super().__init__(browser, url, password, username)

    def get_scenarios(self):
        return self.driver.find_elements(By.XPATH, "//a[@title='Spustit hru']")

    def get_links(self):
        return [element.get_attribute('href') for element in self.get_scenarios()]

    def get_current_page_heading(self):
        return self.driver.find_element(By.CLASS_NAME, "scenarioH2title").text

    def get_article_headings(self):
        return [element.find_element(By.TAG_NAME, 'h4').text for element in self.get_scenarios()]

    def bind_link_with_heading(self):
        # compare len(links) == len(article_headings) in tests
        links = self.get_links()
        article_headings = self.get_article_headings()
        return {links[i]: article_headings[i] for i in range(len(links))}
        


if __name__ == '__main__':

    browser = 'firefox'
    url = 'https://cs.laurie-project.com/vp'


    test = VirtualPatient(browser, url)
    test.set_up_driver()
    test.get_on_page_driver(url)
    test.pass_notification_element()
    test.get_scenarios()
    test.get_links()
    print(test.bind_link_with_heading())
    test.quit_driver()
