from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class PageInventory:

    def __init__(self, driver):
        self.driver = driver

    def add_product(self, product_name):
        divs = self.driver.find_elements(By.CSS_SELECTOR,
                                         "div.inventory_item_description"
                                         )  # Получаем все контейнеры
        for div in divs:  # Перебираем контейнеры
            # Проверяем, есть ли продукт в текущем контейнере
            try:
                div.find_element(
                    By.XPATH, f".//div[normalize-space()='{product_name}']"
                )
                add_button = div.find_element(By.TAG_NAME, "button")
                add_button.click()  # Кликаем на кнопку добавления
                return  # закрываем функцию после успешного добавления
            except NoSuchElementException:
                continue  # Переходим к следующему контейнеру

    def go_to_cart(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "a.shopping_cart_link"
        ).click()
