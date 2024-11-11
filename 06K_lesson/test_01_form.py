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


def test_form(driver):
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "zip-code": "",  # Поле для проверки, передаю null
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for field_name, value in fields.items():
        try:
            field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, f"input[name='{field_name}']")
                )
            )
            field.clear()
            field.send_keys(value)
        except Exception as e:
            print(f"Не удалось заполнить поле '{field_name}': {e}")

    submit_button = driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']"
    )
    submit_button.click()

    WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "div#company.alert.py-2.alert-success")
        )
    )

    for field_name in fields.keys():
        field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, field_name))
        )
        bg_color = field.value_of_css_property("background-color")

        # Проверяем цвет полей и добавляем assert
        if field_name == "zip-code":  # Пустое поле - должно быть красным
            assert bg_color == "rgba(248, 215, 218, 1)", \
                f"Поле {field_name} должно быть красным, но оно {bg_color}"
        else:  # Поле заполнено - должны быть зеленым
            assert bg_color == "rgba(209, 231, 221, 1)", \
                f"Поле {field_name} должно быть зеленым, но оно {bg_color}"

        # результат для проверки корретности цветов полей
        print(f"Поле {field_name} проверено, цвет: {bg_color}")
