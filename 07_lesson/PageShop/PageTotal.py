# Страница проверки стоимости товаров
from selenium.webdriver.common.by import By


class PageTotal:

    def __init__(self, driver):
        self.driver = driver

    def get_total(self):
        return self.driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label"
        ).text

    def finish(self):
        self.driver.find_element(By.CSS_SELECTOR, "#finish")
