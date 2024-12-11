from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(
    GeckoDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/inputs")

input_elements = driver.find_element(
    By.CSS_SELECTOR, "input[type='number']")
# input_element.send_keys("1" * 1000)  # Вводим 1000 единиц
input_elements.send_keys("1000")  # Вводим текст '1000'
sleep(2)
input_elements.clear()
sleep(2)
input_elements.send_keys("999")  # Вводим текст '999'

sleep(2)
driver.close()
