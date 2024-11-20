import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from MainPageForm import MainPageForm
from MainPageForm import FIELDS


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

    form_page = MainPageForm(driver)
    form_page.fill_form()
    form_page.submit_form()

    field_colors = form_page.check_field_colors()
    # fields_is_not_none = [i for i in fields.keys() if i != 'zip-code']
    #
    # for field_name, bg_color in field_colors.items():
    #     if field_name == "zip-code":  # Пустое поле - должно быть красным
    #         assert bg_color == "rgba(248, 215, 218, 1)", \
    #             f"Поле {field_name} должно быть красным"
    #     elif fields_is_not_none:  # Проверяем только заполненные поля
    #         assert bg_color == "rgba(209, 231, 221, 1)", \
    #             f"Поле {field_name} должно быть зеленым"

    for field_name, bg_color in field_colors.items():
        # если проверять любое поле, тогда: FIELDS[field_name] is None
        if field_name == "zip-code":
            assert bg_color == "rgba(248, 215, 218, 1)", \
                f"Поле {field_name} должно быть красным, но оно {bg_color}"
        elif FIELDS[field_name] is not None:  # см только заполненные поля
            assert bg_color == "rgba(209, 231, 221, 1)", \
                f"Поле {field_name} должно быть зеленым, но оно {bg_color}"
