# Страница корзины
from selenium.webdriver.common.by import By


class PageCart:

    def __init__(self, driver):
        self.driver = driver

    # кнопка Проверить в корзине
    def proceed_to_checkout(self):
        self.driver.find_element(By.ID, "checkout").click()
