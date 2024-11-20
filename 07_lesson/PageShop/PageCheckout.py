# Страница проверки данных покупателя
from selenium.webdriver.common.by import By


class PageCheckout:

    def __init__(self, driver):
        self.driver = driver

    def checkout_step(self, first_name, last_name, postal_code):
        self.driver.find_element(
            By.CSS_SELECTOR, "#first-name"
        ).send_keys(first_name)
        self.driver.find_element(
            By.CSS_SELECTOR, "#last-name"
        ).send_keys(last_name)
        self.driver.find_element(
            By.CSS_SELECTOR, "#postal-code"
        ).send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()
