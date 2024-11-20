import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from MainPageCalc import CalculatorPage


@pytest.fixture(scope="module")
def driver():
    """Настройка драйвера Chrome для тестов."""
    drivers = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install())
    )
    yield drivers
    drivers.quit()


def test_calculator(driver):
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    calculator = CalculatorPage(driver)

    # Ввод значения
    calculator.enter_delay("45")

    # Выполнение действий
    calculator.click_number(7)
    calculator.click_plus()
    calculator.click_number(8)
    calculator.click_equals()

    # Проверка результата
    result = calculator.get_result()
    assert "15" in result, "Результат неверный"
    print(f"result = {result}")
