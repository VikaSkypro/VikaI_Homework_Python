import pytest
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


def test_shop(driver):
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    # Авторизация
    authorization_page = PageAuth(driver)  # экземп.класса
    authorization_page.login("standard_user", "secret_sauce")

    # Добавление товаров и Переход в корзину
    inventory_page = PageInventory(driver)
    inventory_page.add_product("Sauce Labs Backpack")
    inventory_page.add_product("Sauce Labs Bolt T-Shirt")
    inventory_page.add_product("Sauce Labs Onesie")
    inventory_page.go_to_cart()

    # кнопка Проверить в корзине
    cart_page = PageCart(driver)
    cart_page.proceed_to_checkout()

    # оформление заказа
    checkout_page = PageCheckout(driver)
    checkout_page.checkout_step("Виктория", "Исаева", "172730")

    # Проверка итоговой стоимости
    total_page = PageTotal(driver)
    total = total_page.get_total()
    total_page.finish()
    print(total)
    assert "$58.29" in total, "неверная итоговая цена"
