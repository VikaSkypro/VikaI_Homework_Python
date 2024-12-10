import pytest
import allure
from allure_commons.types import Severity
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from MainPageCalc import CalculatorPage


@pytest.fixture(scope="module")
def driver():
    """Настройка драйвера Chrome для тестов."""
    drivers = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    yield drivers
    drivers.quit()


@allure.id("SlowCalculator-1")
@allure.story("Сложение двух чисел на медленном калькуляторе")
@allure.epic("Медленный калькулятор")
@allure.feature("READ")
@allure.title("Калькулятор с таймером для получения результата")
@allure.description(
    "Тест устанавливает таймер,"
    "выполняет сложение двух чисел,"
    "возвращает результат по истечении таймера"
    "и сравнивает его с ожидаемым"
)
@allure.severity(Severity.BLOCKER)
@allure.suite("Тесты на работу с калькулятором")
def test_calculator(driver):
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    calculator = CalculatorPage(driver)

    with allure.step("1. Ввод значения счетчика(сек) до выдачи результата"):
        calculator.enter_delay(float("5"))

    with allure.step("2. Выполнение арифметической операции:"):
        with allure.step('2.1 Нажатие кнопки "7"'):
            calculator.click_number(7)

        with allure.step('2.2 Нажатие кнопки "+"'):
            calculator.click_plus()

        with allure.step('2.3 Нажатие кнопки "8"'):
            calculator.click_number(8)

        with allure.step('2.4 Нажатие кнопки "="'):
            calculator.click_equals()

    with allure.step("3. Проверка результата с указанным значением"):
        with allure.step("3.1 Получение результата"):
            result = calculator.get_result()
        with allure.step('3.2 Сравнение результата со значением "15"'):
            assert "15" in result, "Результат неверный"
            print(f"result = {result}")
