import pytest
from selenium import webdriver
from urban_routes_page import UrbanRoutesPage

class TestUrbanRoutes:
    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()  # Usa WebDriverManager si es necesario
        driver.get("https://cnt-6857fc3a-3d40-4a37-bb00-1d487a1d60ae.containerhub.tripleten-services.com")
        yield driver
        driver.quit()

    def test_complete_taxi_request(self, driver):
        page = UrbanRoutesPage(driver)

        # Configurar dirección
        page.set_address("123 Main St, Cityville")

        # Seleccionar tarifa Comfort
        page.select_comfort_tariff()

        # Rellenar número de teléfono
        page.fill_phone_number("+1234567890")

        # Agregar tarjeta de crédito
        page.add_credit_card("4111111111111111", "12/25", "123")

        # Solicitar artículos adicionales
        page.request_items("blanket")
        page.request_items("tissue")
        page.request_items("ice-cream", 2)

        # Confirmar solicitud
        page.confirm_request()

        # (Opcional) Esperar información del conductor
        page.wait_for_driver_info()
