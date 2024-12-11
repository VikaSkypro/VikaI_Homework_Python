# Страница проверки стоимости товаров
import allure
from selenium.webdriver.common.by import By


class PageTotal:

    def __init__(self, driver):
        """
        Конструктор класса, который инициализирует объект с веб-драйвером.
        Он принимает параметр driver, который является экземпляром
        веб-драйвера и предоставляет интерфейс для взаимодействия с браузером.
        :param driver:
        """
        self.driver = driver

    @allure.step("Api. Получение стоимости товаров")
    def get_total(self):
        """
        Метод отвечает за получение общей стоимости товаров на странице.
        Находит элемент отображающий общую стоимость и
        возвращает текстовое содержимое этого элемента.
        :return:
        """
        return self.driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label"
        ).text

    @allure.step("Api. Завершение покупки")
    def finish(self) -> None:
        """
        Метод отвечает за завершение процесса покупки.
        Происходит клик по кнопке Finish.
        :return:
        """
        finish_button = self.driver.find_element(
            By.CSS_SELECTOR, "button.btn_action#finish"
        )
        finish_button.click()
