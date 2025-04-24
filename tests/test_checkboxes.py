
import pytest
import allure
from pages.checkboxes_page import CheckboxesPage

@pytest.mark.usefixtures("driver")
class TestCheckboxes:

    @allure.title("Verificar que el checkbox 0 se puede marcar y desmarcar")
    @allure.description("Este test verifica que el checkbox 0 se puede marcar y desmarcar correctamente.")
    def test_checkbox_0_can_be_checked_and_unchecked(self, driver):
        page = CheckboxesPage(driver)
        page.open()

        # Asegurarse de que esté desmarcado
        page.uncheck_checkbox(0)
        assert not page.is_checked(0)

        # Marcarlo
        page.check_checkbox(0)
        assert page.is_checked(0)

        # Desmarcarlo otra vez
        page.uncheck_checkbox(0)
        assert not page.is_checked(0)

    @allure.title("Verificar que el checkbox 1 está marcado por defecto")
    @allure.description("Este test verifica que el checkbox 1 debería estar marcado por defecto al abrir la página.")
    def test_checkbox_1_is_checked_by_default(self, driver):
        page = CheckboxesPage(driver)
        page.open()

        assert page.is_checked(1), "El checkbox 1 debería estar marcado por defecto"

    @allure.title("Verificar que ambos checkboxes pueden ser marcados")
    @allure.description("Este test verifica que ambos checkboxes (0 y 1) pueden ser marcados correctamente.")
    def test_both_checkboxes_can_be_checked(self, driver):
        page = CheckboxesPage(driver)
        page.open()

        page.check_checkbox(0)
        page.check_checkbox(1)

        assert page.is_checked(0)
        assert page.is_checked(1)

    @allure.title("Verificar que ambos checkboxes pueden ser desmarcados")
    @allure.description("Este test verifica que ambos checkboxes (0 y 1) pueden ser desmarcados correctamente.")
    def test_both_checkboxes_can_be_unchecked(self, driver):
        page = CheckboxesPage(driver)
        page.open()

        page.uncheck_checkbox(0)
        page.uncheck_checkbox(1)

        assert not page.is_checked(0)
        assert not page.is_checked(1)
