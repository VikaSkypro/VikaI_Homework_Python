from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Словарь в формате Ключ:значение
FIELDS = {
    "first-name": "Иван",
    "last-name": "Петров",
    "address": "Ленина, 55-3",
    "zip-code": None,  # Поле для проверки, передаю None
    "e-mail": "test@skypro.com",
    "phone": "+7985899998787",
    "city": "Москва",
    "country": "Россия",
    "job-position": "QA",
    "company": "SkyPro",
}


class MainPageForm:
    def __init__(self, driver):
        """
        Метод инициализирует экземпляр класса MainPageForm,
        принимает объект driver Selenium и
        устанавливает поле fields,
        содержащий данные для заполнения формы.
        """
        self.driver = driver
        self.fields = FIELDS

    def fill_form(self) -> None:
        """
        Метод заполняет поля формы значениями из словаря FIELDS.
        1. Перебирает все пары "имя поля - значение" из словаря;
        2. Очищает текущее поле;
        3. При значении не None - заполняет поле;
        4. При None - оставляет поле пустым.
        """
        for field_name, value in self.fields.items():
            try:
                field = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, f"input[name='{field_name}']")
                    )
                )
                field.clear()
                if value is not None:  # проверка на None
                    field.send_keys(value)
            except Exception as e:
                print(f"Не удалось заполнить поле '{field_name}': {e}")

    def submit_form(self) -> None:
        """
        Метод отправляет результаты на проверку
        после нажатия кнопки Submit.
        :return:
        """
        submit_button = self.driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        )
        submit_button.click()

        WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "div#company.alert.py-2.alert-success")
                or (By.CSS_SELECTOR, "#company.alert.py-2.alert-danger")
            )
        )

    def check_field_colors(self) -> dict[str, str]:
        """
        Метод проверяет цвета полей.
        Если красный - поле не заполнено;
        Если зеленый - заполнено верно.
        :return:
        """
        results = {}
        for field_name in self.fields.keys():
            field = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, field_name))
            )
            bg_color = field.value_of_css_property("background-color")
            results[field_name] = bg_color
            print(f"Поле {field_name} проверено, цвет: {bg_color}")

        return results
