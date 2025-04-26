import allure
from pages.login_page import LoginPage  # Asegúrate de que la importación sea correcta

@allure.title("Login Test - Valid Credentials")
@allure.description("Este test verifica que un usuario con credenciales válidas pueda iniciar sesión correctamente.")
def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.load()  # Llama al método 'load' para abrir la página de login
    login_page.enter_username("usuario_valido")
    login_page.enter_password("contraseña_valida")
    login_page.click_login()
    # Aquí añadirías las aserciones para verificar que el login fue exitoso

@allure.title("Login Test - Invalid Credentials")
@allure.description("Este test verifica que un usuario con credenciales inválidas no pueda iniciar sesión.")
def test_unsuccessful_login(driver):
    login_page = LoginPage(driver)
    login_page.load()  # Llama al método 'load' para abrir la página
    login_page.enter_username("usuario_invalido")
    login_page.enter_password("contraseña_invalida")
    login_page.click_login()
    # Aquí añadirías las aserciones para verificar que el login falló

"""@allure.title("Login Test - Missing Username")
@allure.description("Este test verifica que un usuario sin nombre de usuario no pueda iniciar sesión.")
def test_missing_username(driver):
    login_page = LoginPage(driver)
    login_page.load()  # Llama al método 'load' para abrir la página de login
    login_page.enter_password("contraseña_valida")
    login_page.click_login()
    # Aquí debes verificar que el mensaje de error para 'usuario faltante' se muestra
    assert login_page.get_flash_message() == "Your username is invalid!", "El mensaje de error no es el esperado"""

