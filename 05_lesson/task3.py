from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.maximize_window()

# Зайти на сайт и кликнуть на синюю кнопку
driver.get("http://uitestingplayground.com/classattr")

button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
driver.execute_script("arguments[0].click();", button)
sleep(3)

# перехват alert и подтверждение действий
try:
    WebDriverWait(driver, 3).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()  # Или alert.dismiss() для отказа
except Exception as e:
    print("No alert present or an error occurred:", e)

sleep(5)
