from selenium.webdriver.common.by import By


class PageAuth:

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(
            By.CSS_SELECTOR, "#user-name"
        ).send_keys(username)
        self.driver.find_element(
            By.CSS_SELECTOR, "#password"
        ).send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()
