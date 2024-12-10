# Страница авторизации
import allure
from selenium.webdriver.common.by import By


class PageAuth:

    def __init__(self, driver):
        """
        Конструктор класса, который инициализирует объект с веб-драйвером.
        Он принимает параметр driver, который является экземпляром
        веб-драйвера и предоставляет интерфейс для взаимодействия с браузером.
        :param driver:
        """
        self.driver = driver

    @allure.step("Api. Авторизация на сайте")
    def login(self, username: str, password: str):
        """
        Метод, который отвечает за вход в систему.
        Заполняются поля Username и Password,
        выполняется клик по кнопке Login.
        :param username:
        :param password:
        :return:
        """
        with allure.step("Ввод имени"):
            self.driver.find_element(
                By.CSS_SELECTOR, "#user-name"
            ).send_keys(username)
        with allure.step("Ввод пароля"):
            self.driver.find_element(
                By.CSS_SELECTOR, "#password"
            ).send_keys(password)
        with allure.step("Клик на кнопку Login"):
            self.driver.find_element(
                By.CSS_SELECTOR, "#login-button"
            ).click()
