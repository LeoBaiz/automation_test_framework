import pytest
import os
from selenium import webdriver
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.options import Options

# Directorio fijo para los resultados de Allure
ALLURE_DIR = "allure-results"

# Configuración de la carpeta de resultados
def init_report_directory():
    os.makedirs(ALLURE_DIR, exist_ok=True)
    return ALLURE_DIR

# Fixture para el driver de Selenium
@pytest.fixture
def driver():
    options = Options()
    if os.getenv('SELENIUM_HEADLESS', 'true').lower() == 'true':
        options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
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
            screenshot = driver.get_screenshot_as_png()
            allure.attach(
                body=screenshot,
                name=f"screenshot_{item.name}.png",
                attachment_type=AttachmentType.PNG
            )

# Configurar el directorio de Allure
def pytest_configure(config):
    allure_dir = init_report_directory()
    config.option.allure_report_dir = allure_dir