from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.maximize_window()
wait = WebDriverWait(driver, 20, 0.1)

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
src1 = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "img#landscape"))
)
src = driver.find_element(By.CSS_SELECTOR, "img#award").get_attribute("src")
print(src)

driver.quit()
