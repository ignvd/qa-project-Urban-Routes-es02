from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver

    def set_address(self, address):
        address_input = self.driver.find_element(By.ID, "address")
        address_input.clear()
        address_input.send_keys(address)
        address_input.send_keys(Keys.RETURN)

    def select_comfort_tariff(self):
        self.driver.find_element(By.ID, "comfort-tariff").click()

    def fill_phone_number(self, phone):
        phone_input = self.driver.find_element(By.ID, "phone")
        phone_input.send_keys(phone)

    def add_credit_card(self, card_number, expiration, cvv):
        self.driver.find_element(By.ID, "add-card").click()
        self.driver.find_element(By.ID, "card-number").send_keys(card_number)
        self.driver.find_element(By.ID, "card-expiration").send_keys(expiration)
        cvv_input = self.driver.find_element(By.ID, "code")
        cvv_input.send_keys(cvv)
        cvv_input.send_keys(Keys.TAB)

    def request_items(self, item, quantity=1):
        for _ in range(quantity):
            self.driver.find_element(By.ID, f"add-{item}").click()

    def confirm_request(self):
        self.driver.find_element(By.ID, "confirm-request").click()

    def wait_for_driver_info(self, timeout=60):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.ID, "driver-info"))
        )
