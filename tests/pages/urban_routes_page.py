from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UrbanPage:
    # Selectores
    ADDRESS_INPUT = (By.ID, "address")
    COMFORT_TARIFF = (By.CSS_SELECTOR, "button[data-tariff='comfort']")
    PHONE_INPUT = (By.ID, "phone")
    CREDIT_CARD_BUTTON = (By.ID, "add-card")
    CVV_FIELD = (By.CLASS_NAME, "card-input")
    CONFIRM_BUTTON = (By.XPATH, "//button[contains(text(), 'Confirmar')]")
    DRIVER_MODAL = (By.ID, "driver-modal")
    
    # Métodos de interacción
    def set_address(self, driver, address):
        driver.find_element(*self.ADDRESS_INPUT).send_keys(address)

    def select_comfort_tariff(self, driver):
        driver.find_element(*self.COMFORT_TARIFF).click()

    def enter_phone_number(self, driver, phone_number):
        driver.find_element(*self.PHONE_INPUT).send_keys(phone_number)

    def add_credit_card(self, driver, cvv):
        driver.find_element(*self.CREDIT_CARD_BUTTON).click()
        cvv_input = driver.find_element(*self.CVV_FIELD)
        cvv_input.send_keys(cvv)
        cvv_input.send_keys(Keys.TAB)  # Cambiar el foco
        driver.find_element(*self.CONFIRM_BUTTON).click()

    def wait_for_driver_modal(self, driver, timeout=10):
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(self.DRIVER_MODAL)
        )

from selenium.webdriver.common.by import By

class UrbanPage:
    ADDRESS_FIELD = (By.ID, "address")
    COMFORT_TARIFF_BUTTON = (By.CSS_SELECTOR, ".tariff-comfort")
    PHONE_FIELD = (By.ID, "phone")
    ADD_CARD_BUTTON = (By.ID, "add-card")
    CVV_FIELD = (By.ID, "code")
    MESSAGE_FIELD = (By.ID, "message")
    SUBMIT_BUTTON = (By.ID, "submit")
