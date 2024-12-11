import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def driver():
    """Фикстура для настройки драйвера Chrome для тестов."""
    drivers = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install())
    )
    yield drivers
    drivers.quit()


def test_shop(driver):
    driver.maximize_window()
    driver.get(
        "https://www.saucedemo.com/"
    )
    # авторизация
    username = driver.find_element(By.CSS_SELECTOR, "#user-name")
    username.clear()
    username.send_keys("standard_user")
    aut_password = driver.find_element(By.CSS_SELECTOR, "#password")
    aut_password.clear()
    aut_password.send_keys("secret_sauce")
    # ищем кн Login и кликаем
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    # ищем контейнер со всеми продуктами
    inventory_list = driver.find_element(By.CSS_SELECTOR, "div.inventory_list")
    # ищем продукт 1
    prod1 = inventory_list.find_element(
        By.XPATH, "//div[normalize-space()='Sauce Labs Backpack']"
    )
    # Ищем кнопку добавить и кликаем
    produ1 = prod1.find_element(
        By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']"
    )
    produ1.click()

    prod2 = inventory_list.find_element(
        By.XPATH, "//div[normalize-space()='Sauce Labs Bolt T-Shirt']"
    )
    produ2 = prod2.find_element(
        By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    )
    produ2.click()

    prod3 = inventory_list.find_element(
        By.XPATH, "//div[normalize-space()='Sauce Labs Onesie']"
    )
    produ3 = prod3.find_element(
        By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']"
    )
    produ3.click()

    # Переход в корзину
    driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()

    # Заполните форму своими данными: имя, фамилия, почтовый индекс
    name = driver.find_element(By.CSS_SELECTOR, "#first-name")
    name.clear()
    name.send_keys("Виктория")

    last_name = driver.find_element(By.CSS_SELECTOR, "#last-name")
    last_name.clear()
    last_name.send_keys("Исаева")

    zip = driver.find_element(By.CSS_SELECTOR, "#postal-code")
    zip.clear()
    zip.send_keys("172730")

    driver.find_element(By.ID, "continue").click()
    # total
    total = driver.find_element(
        By.CSS_SELECTOR, "div.summary_total_label"
    ).text
    print(total)
    assert "$58.29" in total, "неверная итоговая цена"
