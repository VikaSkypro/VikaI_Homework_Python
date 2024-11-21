from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = "#delay"
        self.keys_container = "div.keys"
        self.equals_button = ".btn.btn-outline-warning"
        self.result_display = "div.screen"

    def enter_delay(self, delay):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.delay_input))
        )
        element.clear()
        element.send_keys(delay)

    def click_number(self, number):
        number_button = f"//span[normalize-space()='{number}']"
        self.driver.find_element(By.XPATH, number_button).click()

    def click_plus(self):
        plus_button = self.driver.find_element(
            By.CSS_SELECTOR, "div[class='keys'] span:nth-child(4)"
        )
        plus_button.click()

    def click_equals(self):
        self.driver.find_element(By.CSS_SELECTOR, self.equals_button).click()

    def get_result(self):
        WebDriverWait(self.driver, 46).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "span#spinner[style='display: none;']")
            )
        )
        return self.driver.find_element(
            By.CSS_SELECTOR, self.result_display
        ).text
