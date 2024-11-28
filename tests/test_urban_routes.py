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
