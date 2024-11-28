# **Urban Routes - Proyecto de Pruebas Automatizadas**

## **Descripción del Proyecto**

Urban Routes es un proyecto diseñado para automatizar y validar el flujo de reserva de taxis en una aplicación web. Este proyecto utiliza herramientas como `pytest` y `Selenium` para garantizar la calidad del sistema mediante pruebas automatizadas eficientes y completas.  

El objetivo principal es probar la funcionalidad clave de la aplicación, incluyendo el registro de usuarios, la selección de tarifas, y el proceso completo de solicitud de taxis.

---

## **Requisitos Previos**

### **Librerías y Herramientas Necesarias**
Antes de ejecutar el proyecto, asegúrate de tener instaladas las siguientes herramientas y librerías:

1. **Python 3.9 o superior**
2. **pip (administrador de paquetes de Python)**
3. **Google Chrome** y el **ChromeDriver** correspondiente (debe coincidir con la versión de Chrome instalada).
4. **Librerías de Python necesarias**:
   - `selenium`
   - `pytest`
   - `pytest-html`

---

## **Instalación**

### **Clonar el Proyecto**
Primero, clona este repositorio en tu computadora local:

```bash
git clone git@github.com:tu-usuario/qa-project-Urban-Routes-es.git
cd qa-project-Urban-Routes-es

##instalar dependecias
pip install -r requirements.txt

## configuracion
BASE_URL = "https://cnt-6857fc3a-3d40-4a37-bb00-1d487a1d60ae.containerhub.tripleten-services.com"
USER_DATA = {
    "firstName": "Test",
    "phone": "+1234567890",
    "address": "123 Test Street",
}

## ejecutar pruebas
pytest tests/ --html=report.html --self-contained-html




