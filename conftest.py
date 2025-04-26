import pytest
import os
import zipfile
from datetime import datetime
from selenium import webdriver
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.options import Options
import subprocess

# Variable global para almacenar la carpeta de reporte
REPORT_DIR = None
ALLURE_DIR = None

# Configuración de la carpeta dinámica (se llama una sola vez)
def init_report_directory():
    global REPORT_DIR, ALLURE_DIR
    if REPORT_DIR is None or ALLURE_DIR is None:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        REPORT_DIR = f"Reports/{timestamp}_Execution"
        ALLURE_DIR = f"{REPORT_DIR}/allure-results"
        os.makedirs(ALLURE_DIR, exist_ok=True)
    return REPORT_DIR, ALLURE_DIR

# Fixture para el driver de Selenium
@pytest.fixture
def driver():
    # Configurar opciones para Chrome
    options = Options()
    if os.getenv('SELENIUM_HEADLESS', 'true').lower() == 'true':
        options.add_argument("--headless")  # Modo headless solo si SELENIUM_HEADLESS=true
    options.add_argument("--no-sandbox")  # Necesario para entornos como GitHub Actions
    options.add_argument("--disable-dev-shm-usage")  # Evita problemas en entornos CI
    options.add_argument("--window-size=1920,1080")  # Tamaño de ventana opcional

    # Inicializar el driver con las opciones configuradas
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

# Hook para capturar pantallas en caso de fallo
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        driver = item.funcargs.get('driver', None)
        if driver:
            # Obtener la carpeta allure-results (solo para referencia, no se usa para guardar manualmente)
            _, allure_dir = init_report_directory()
            # Tomar captura de pantalla
            screenshot = driver.get_screenshot_as_png()
            # Adjuntar a Allure con nombre personalizado
            allure.attach(
                body=screenshot,
                name=f"screenshot_{item.name}.png",
                attachment_type=AttachmentType.PNG
            )

# Configurar el directorio de Allure dinámicamente una sola vez
def pytest_configure(config):
    _, allure_dir = init_report_directory()
    config.option.allure_report_dir = allure_dir



"""
# Hook para generar el ZIP del reporte de Allure después de la ejecución
def pytest_sessionfinish(session, exitstatus):
    # Asegurarse de que las carpetas estén inicializadas
    report_dir, allure_dir = init_report_directory()

    # Nombre del archivo ZIP
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    zip_path = os.path.join(report_dir, f"allure-report_{timestamp}.zip")

    # Crear el archivo ZIP
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Recorrer todos los archivos en allure-results
        for root, _, files in os.walk(allure_dir):
            for file in files:
                file_path = os.path.join(root, file)
                # Agregar el archivo al ZIP, manteniendo la estructura relativa
                arcname = os.path.relpath(file_path, allure_dir)
                zipf.write(file_path, arcname)

    print(f"Reporte comprimido generado en: {zip_path}")
"""