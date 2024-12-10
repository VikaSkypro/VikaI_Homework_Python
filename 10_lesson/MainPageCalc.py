from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """
    Методы класса CalculatorPage описывают
    взаимодействие с калькулятором в веб-приложении.
    """

    def __init__(self, driver):
        """
        Конструктор класса, инициализирующий объект с веб-драйвером
        и определяющий селекторы для элементов интерфейса калькулятора.
        :param driver:
        """
        self.driver = driver
        self.delay_input = "#delay"
        self.keys_container = "div.keys"
        self.equals_button = ".btn.btn-outline-warning"
        self.result_display = "div.screen"

    def enter_delay(self, delay: float) -> None:
        """
        Метод позволяет вводить задержку.
        Он ожидает, пока элемент поля для ввода задержки станет доступным,
        очищает его и вводит заданное значение delay.
        :param delay:
        :return:
        """
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.delay_input))
        )
        element.clear()
        element.send_keys(str(delay))

    def click_number(self, number: int) -> None:
        """Метод выполняет нажатие на кнопку с числом."""
        number_button = f"//span[normalize-space()='{number}']"
        self.driver.find_element(By.XPATH, number_button).click()

    def click_plus(self) -> None:
        """Метод выполняет нажатие на кнопку \"плюс\"."""
        plus_button = self.driver.find_element(
            By.CSS_SELECTOR, "div[class='keys'] span:nth-child(4)"
        )
        plus_button.click()

    def click_equals(self) -> None:
        """
        Метод выполняет нажатие на кнопку \"равно\",
        чтобы выполнить вычисление.
        """
        self.driver.find_element(By.CSS_SELECTOR, self.equals_button).click()

    def get_result(self) -> float:
        """
        Метод для получения результата вычисления.
        Он ждет, пока исчезнет спиннер, указывающий на загрузку,
        а затем возвращает текст из поля результата.
        :return:
        """
        WebDriverWait(self.driver, 46).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "span#spinner[style='display: none;']")
            )
        )
        return self.driver.find_element(
            By.CSS_SELECTOR, self.result_display
        ).text
