# Страница выбора продуктов
import allure
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class PageInventory:

    def __init__(self, driver):
        """
        Конструктор класса, который инициализирует объект с веб-драйвером.
        Он принимает параметр driver, который является экземпляром
        веб-драйвера и предоставляет интерфейс для взаимодействия с браузером.
        :param driver:
        """
        self.driver = driver

    @allure.step("Api. Выбор и добавление продуктов в корзину")
    def add_product(self, product_name: str) -> None:
        """
        Метод отвечает за добавление продукта в корзину.
        1. Выполняется поиск всех продуктов;
        2. Перебирает каждый продукт по названию;
        3. Находит - добавляет в корзину;
        4. Не находит - ищет дальше.
        :param product_name:
        :return:
        """
        divs = self.driver.find_elements(
            By.CSS_SELECTOR, "div.inventory_item_description"
        )  # Получаем все контейнеры
        with allure.step("1. Поиск продукта в контейнере div"):
            for div in divs:  # Перебираем контейнеры
                # Проверяем, есть ли продукт в текущем контейнере
                try:
                    div.find_element(
                        By.XPATH, f".//div[normalize-space()='{product_name}']"
                    )
                    add_button = div.find_element(By.TAG_NAME, "button")

                    with allure.step("1.1 Добавление продукта в корзину"):
                        add_button.click()  # Кликаем на кнопку добавления
                    return  # закрываем функцию после успешного добавления

                except NoSuchElementException:
                    with allure.step("1.2 Поиск продукта в следующем контейнере"):
                        continue  # Переходим к следующему контейнеру

    @allure.step("Api. Переход в корзину")
    def go_to_cart(self) -> None:
        """
        Метод выполняет переход в корзину.
        :return:
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "a.shopping_cart_link"
        ).click()
