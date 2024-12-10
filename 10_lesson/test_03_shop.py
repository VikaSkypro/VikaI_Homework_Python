import pytest
import allure
from allure_commons.types import Severity
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from PageShop.PageAuth import PageAuth
from PageShop.PageInventory import PageInventory
from PageShop.PageCart import PageCart
from PageShop.PageCheckout import PageCheckout
from PageShop.PageTotal import PageTotal


@pytest.fixture(scope="module")
def driver():
    """Фикстура для настройки драйвера Chrome для тестов."""
    drivers = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    yield drivers
    drivers.quit()


@allure.id("Shop-1")
@allure.story("Покупка товаров с получением итоговой стоимости")
@allure.epic("Интернет-магазин")
@allure.feature("READ")
@allure.title("Покупка товаров в интернет-магазине")
@allure.description(
    "Тест авторизует пользователя в интернет-магазине,"
    "помещает в корзину выбранный товар,"
    "выполняет оформление заказа по указанным данным,"
    "получает и сравнивает итоговую сумму с передаваемым значением."
)
@allure.severity(Severity.BLOCKER)
@allure.suite("Тесты на работу с интернет-магазином")
def test_shop(driver):
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    username = "standard_user"
    password = "secret_sauce"
    with allure.step('1. Авторизация на сайте "https://www.saucedemo.com/"'):
        authorization_page = PageAuth(driver)  # экземпляр класса
        with allure.step(f"1.1 ввод логина: {username} и пароля: {password}"):
            authorization_page.login(username, password)

    with allure.step("2. Добавление товаров в корзину:"):
        with allure.step('2.1 Добавление товара "Sauce Labs Backpack"'):
            inventory_page = PageInventory(driver)
            inventory_page.add_product("Sauce Labs Backpack")

        with allure.step('2.2 Добавление товара "Sauce Labs Bolt T-Shirt"'):
            inventory_page.add_product("Sauce Labs Bolt T-Shirt")

        with allure.step('2.3 Добавление товара "Sauce Labs Onesie"'):
            inventory_page.add_product("Sauce Labs Onesie")

    with allure.step("3. Переход в корзину"):
        inventory_page.go_to_cart()

    with allure.step("4. Клик по кнопке Проверить"):
        cart_page = PageCart(driver)
        cart_page.proceed_to_checkout()

    with allure.step("5. Оформление заказа"):
        checkout_page = PageCheckout(driver)
        checkout_page.checkout_step("Виктория", "Исаева", "172730")

    with allure.step("6. Проверка итоговой стоимости"):
        total_page = PageTotal(driver)
        with allure.step("6.1 Получение стоимости всех добавленных товаров"):
            total = total_page.get_total()
        with allure.step('6.2 Сравнение полученной стоимости со значением "$58.29"'):
            print(total)
            assert "$58.29" in total, "Неверная итоговая цена"
    with allure.step("7. Завершение покупок!"):
        total_page.finish()
