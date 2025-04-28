from selenium.webdriver.common.by import By
from config.settings import BASE_URL_Stable,TIMEOUT,BROWSER

class CheckboxesPage:
    URL = f"{BASE_URL_Stable.rstrip('/')}/checkboxes"
    timeout = TIMEOUT

    CHECKBOXES = (By.CSS_SELECTOR, "#checkboxes input")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def get_checkboxes(self):
        return self.driver.find_elements(*self.CHECKBOXES)

    def check_checkbox(self, index):
        checkboxes = self.get_checkboxes()
        if not checkboxes[index].is_selected():
            checkboxes[index].click()

    def uncheck_checkbox(self, index):
        checkboxes = self.get_checkboxes()
        if checkboxes[index].is_selected():
            checkboxes[index].click()

    def is_checked(self, index):
        return self.get_checkboxes()[index].is_selected()
