from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PageBase:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, clickable = False):
        if clickable:
            elem = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator)
            )
        else:
            elem = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator)
            )
        return elem
    
    def input_text(self, elem, text):
        elem.clear()
        elem.send_keys(text)