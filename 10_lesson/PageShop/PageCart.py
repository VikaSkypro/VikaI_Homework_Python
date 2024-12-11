# Страница корзины
import allure
from selenium.webdriver.common.by import By


class PageCart:

    def __init__(self, driver):
        """
        Конструктор класса, который инициализирует объект с веб-драйвером.
        Он принимает параметр driver, который является экземпляром
        веб-драйвера и предоставляет интерфейс для взаимодействия с браузером.
        :param driver:
        """
        self.driver = driver

    @allure.step("Api. Клик по кнопке Проверить")
    def proceed_to_checkout(self) -> None:
        """
        Метод отвечает за переход к оформлению заказа.
        :return:
        """
        self.driver.find_element(By.ID, "checkout").click()
