import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def driver():
    """Фикстура для настройки драйвера Chrome для тестов."""
    drivers = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install())
    )
    yield drivers
    drivers.quit()


def test_calc(driver):
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    # Ожидание, пока элемент #delay станет доступен
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#delay"))
    )
    element.clear()
    element.send_keys("45")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.keys"))
    )

    # 7
    span_element_7 = driver.find_element(
        By.CSS_SELECTOR, "div[class='keys'] span:nth-child(1)"
    )
    # Получение текста (необязательно, т.к. мы его уже ищем)
    # оставлено для проверки в print
    span_text_7 = span_element_7.text
    # print(span_text_7)
    # Клик по элементу
    span_element_7.click()

    # +
    span_element_plus = driver.find_element(
        By.CSS_SELECTOR, "div[class='keys'] span:nth-child(4)"
    )
    span_text_plus = span_element_plus.text
    # print(span_text_plus)
    span_element_plus.click()

    # 8
    span_element_8 = driver.find_element(
        By.XPATH, "//span[normalize-space()='8']"
    )
    span_text_8 = span_element_8.text
    # print(span_text_8)
    span_element_8.click()

    # =
    span_element_equal = driver.find_element(
        By.CSS_SELECTOR, ".btn.btn-outline-warning"
    )
    span_text_equal = span_element_equal.text
    # print(span_text_equal)
    span_element_equal.click()

    WebDriverWait(driver, 46).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "span#spinner[style='display: none;']")
        )
    )

    res = driver.find_element(By.CSS_SELECTOR, "div.screen").text
    assert "15" in res, "результат неверный"
    print("Вычисления: ", span_text_7 + span_text_plus +
          span_text_8 + span_text_equal + res
          )
