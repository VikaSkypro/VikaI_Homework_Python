# Страница проверки данных покупателя
import allure
from selenium.webdriver.common.by import By
import typing as t


class PageCheckout:

    def __init__(self, driver):
        """
        Конструктор класса, который инициализирует объект с веб-драйвером.
        Он принимает параметр driver, который является экземпляром
        веб-драйвера и предоставляет интерфейс для взаимодействия с браузером.
        :param driver:
        """
        self.driver = driver

    @allure.step("Api. Оформление заказа")
    def checkout_step(
            self, first_name: str, last_name: str, postal_code: t.Any
    ):
        """
        Метод отвечает за ввод данных покупателя
        на странице оформления заказа.
        Заполняются все поля и выполняется нажатие кнопки Continue.
        :param first_name:
        :param last_name:
        :param postal_code:
        :return:
        """
        with allure.step("Ввод Имени в поле first_name"):
            self.driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(
                first_name
            )
        with allure.step("Ввод Фамилии в поле last_name"):
            self.driver.find_element(
                By.CSS_SELECTOR, "#last-name"
            ).send_keys(last_name)
        with allure.step("Ввод Индекса в поле postal_code"):
            self.driver.find_element(
                By.CSS_SELECTOR, "#postal-code"
            ).send_keys(
                postal_code
            )
        with allure.step("Клик по кнопке Continue"):
            self.driver.find_element(By.ID, "continue").click()
