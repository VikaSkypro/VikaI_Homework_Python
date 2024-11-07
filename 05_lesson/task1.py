from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.maximize_window()

# Зайти на сайт
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
# 5 раз кликнуть на кн. Add Element
# и вывести на экран кол-во кнопок Delete
click = "[onclick='addElement()']"
for i in range(0, 5):
    click5 = driver.find_element(By.CSS_SELECTOR, click).click()
    del_button = driver.find_elements(
        By.CSS_SELECTOR, "[onclick='deleteElement()']")
print("Количество кнопок Delete: ", len(del_button))

sleep(5)
