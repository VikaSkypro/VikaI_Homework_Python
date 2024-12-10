import pytest
import allure
from allure_commons.types import Severity
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from MainPageForm import MainPageForm
from MainPageForm import FIELDS


@pytest.fixture(scope="module")
def driver():
    """Фикстура для настройки драйвера Chrome для тестов."""
    drivers = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    yield drivers
    drivers.quit()


@allure.id("DataTypes-1")
@allure.story("Заполнение полей формы, кроме поля Zip")
@allure.epic("Форма для заполнения полей")
@allure.feature("READ")
@allure.title("Заполнение формы, кроме поля Zip с проверкой цветов полей")
@allure.description(
    "Тест заполняет поля значениями из словаря FIELDS. "
    "После нажатия кнопки Submit отправляет результаты на проверку."
    "Проверяет цвета полей:"
    "если красный - поле не заполнено;"
    "Если зеленый - заполнено верно."
)
@allure.severity(Severity.BLOCKER)
@allure.suite("Тесты на работу с формой заполнения полей")
def test_data_types(driver):
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

    form_page = MainPageForm(driver)
    with allure.step("1. Заполнение поля формы значениями из словаря FIELDS"):
        form_page.fill_form()

    with allure.step("2. Нажатие кнопки Submit"):
        form_page.submit_form()

    with allure.step("3. Сравнение цвета поля с ожидаемым цветом"):
        field_colors = form_page.check_field_colors()
        for field_name, bg_color in field_colors.items():
            # если проверять любое поле, тогда: if FIELDS[field_name] is None
            if field_name == "zip-code":
                assert (
                    bg_color == "rgba(248, 215, 218, 1)"
                ), f"Поле {field_name} должно быть красным, но оно {bg_color}"
            elif FIELDS[field_name] is not None:  # см только заполненные поля
                assert (
                    bg_color == "rgba(209, 231, 221, 1)"
                ), f"Поле {field_name} должно быть зеленым, но оно {bg_color}"


# fields_is_not_none = [i for i in fields.keys() if i != 'zip-code']
#
# for field_name, bg_color in field_colors.items():
#     if field_name == "zip-code":  # Пустое поле - должно быть красным
#         assert bg_color == "rgba(248, 215, 218, 1)", \
#             f"Поле {field_name} должно быть красным"
#     elif fields_is_not_none:  # Проверяем только заполненные поля
#         assert bg_color == "rgba(209, 231, 221, 1)", \
#             f"Поле {field_name} должно быть зеленым"
