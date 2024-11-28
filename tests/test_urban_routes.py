import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.urban_routes_page import UrbanPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_order_taxi(driver):
    driver.get("https://cnt-6857fc3a-3d40-4a37-bb00-1d487a1d60ae.containerhub.tripleten-services.com?lng=es")
    page = UrbanPage()

    # Configurar dirección
    page.set_address(driver, "123 Main Street")
    assert "123 Main Street" in driver.page_source

    # Seleccionar tarifa Comfort
    page.select_comfort_tariff(driver)
    assert "Comfort" in driver.page_source

    # Ingresar número de teléfono
    page.enter_phone_number(driver, "555-123-4567")
    assert "555-123-4567" in driver.page_source

    # Agregar tarjeta de crédito
    page.add_credit_card(driver, "123")
    assert "Tarjeta añadida" in driver.page_source

    # Validar modal de búsqueda de conductor
    page.wait_for_driver_modal(driver)
    assert "Información del conductor" in driver.page_source
    import pytest
from selenium import webdriver
from pages.urban_page import UrbanPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://cnt-6857fc3a-3d40-4a37-bb00-1d487a1d60ae.containerhub.tripleten-services.com")
    yield driver
    driver.quit()

def test_taxi_booking(driver):
    # Configurar la dirección
    address_field = driver.find_element(*UrbanPage.ADDRESS_FIELD)
    address_field.send_keys("123 Test Street")
    
    # Seleccionar tarifa Comfort
    comfort_button = driver.find_element(*UrbanPage.COMFORT_TARIFF_BUTTON)
    comfort_button.click()

    # Ingresar el número de teléfono
    phone_field = driver.find_element(*UrbanPage.PHONE_FIELD)
    phone_field.send_keys("+1234567890")

    # Agregar tarjeta de crédito
    add_card_button = driver.find_element(*UrbanPage.ADD_CARD_BUTTON)
    add_card_button.click()
    cvv_field = driver.find_element(*UrbanPage.CVV_FIELD)
    cvv_field.send_keys("123")
    driver.find_element_by_tag_name("body").click()  # Simular TAB o pérdida de foco

    # Enviar mensaje al conductor
    message_field = driver.find_element(*UrbanPage.MESSAGE_FIELD)
    message_field.send_keys("Por favor, no tocar la bocina.")

    # Confirmar el pedido
    submit_button = driver.find_element(*UrbanPage.SUBMIT_BUTTON)
    submit_button.click()

    # Validar la reserva
    assert "Reserva exitosa" in driver.page_source

