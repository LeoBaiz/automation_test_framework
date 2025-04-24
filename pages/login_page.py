from selenium.webdriver.common.by import By
from config.settings import BASE_URL, BROWSER, TIMEOUT

class LoginPage:
    URL = f"{BASE_URL.rstrip('/')}/login"
    t = TIMEOUT

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def enter_username(self, username):
        self.driver.find_element(By.ID, "username").send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_login(self):
        self.driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    def get_flash_message(self):
        return self.driver.find_element(By.ID, "flash").text
