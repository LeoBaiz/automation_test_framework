import time
import unittest
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from utils.funciones import Funciones_Globales



class Funciones_Expand():

    def __init__(self, driver):
        self.driver = driver
        self.funciones = Funciones_Globales(driver)  # Instancia de Funciones_Globales

    def Tiempo(self, tie):
        t = time.sleep(tie)
        return t

    def Login(self,URL,User,Pass, Tiempo):  # Funcion para Logear un Usuario
        self.funciones.Navegar(URL, Tiempo)
        # Usar el objeto funciones para realizar las acciones

        user = self.driver.find_element(By.ID, "mat-input-0")
        user.click()
        self.funciones.Texto_Mixto_Valida("id", "mat-input-0", User, Tiempo)
        password = self.driver.find_element(By.ID, "mat-input-1")
        password.click()
        self.funciones.Texto_Mixto_Valida("id", "mat-input-1", Pass, Tiempo)
        self.funciones.Click_Mixto_Valida("xpath", "//expand-core-login[1]/form[1]/button[1]", Tiempo)
        # Verifica si la página de inicio se carga correctamente
        try:
            WebDriverWait(self.driver, Tiempo).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/expand-core-root/expand-core-main/div/mat-sidenav-container/mat-sidenav-content/div/expand-core-home/div/div[1]/div/label"))
            )
            print("Login successful, home page loaded")
        except TimeoutException:
            print("Login failed, home page not loaded")

    def extraer_texto(self,log, inicio, fin=None, delimitador=" "):
        """
        Extrae texto de un log dado entre las posiciones marcadas por `inicio` y `fin`.
        Si `fin` no se proporciona, utiliza el delimitador como referencia para el final.

        :param log: Texto completo del log.
        :param inicio: Marcador donde comienza la extracción (puede ser un texto exacto o un índice numérico).
        :param fin: Marcador donde termina la extracción (puede ser un texto exacto o un índice numérico). Opcional.
        :param delimitador: Caracter o palabra que delimita el final si no se proporciona `fin`. Por defecto: espacio.
        :return: Texto extraído o None si no se encuentran los marcadores.
        """
        try:
            # Si 'inicio' es texto, calcula su posición en el log
            if isinstance(inicio, str):
                start_pos = log.index(inicio) + len(inicio)
            else:  # Si es numérico, úsalo directamente
                start_pos = inicio

            # Determina el punto final según 'fin'
            if fin:
                if isinstance(fin, str):
                    end_pos = log.index(fin, start_pos)
                else:  # Si es numérico, úsalo directamente
                    end_pos = fin
            else:  # Si no hay fin, usa el delimitador o el resto del texto
                end_pos = log.find(delimitador, start_pos) if delimitador else len(log)

            # Extrae y retorna el texto
            return log[start_pos:end_pos].strip()
        except ValueError:
            # Maneja casos donde no se encuentran los marcadores
            return None

    def seleccionar_permisos(self, permisos, t=2):
        """
        Busca cada permiso en el campo de búsqueda y selecciona el checkbox correspondiente.

        :param permisos: Lista de nombres de permisos a seleccionar
        :param t: Tiempo de espera entre acciones (segundos)
        """
        for permiso in permisos:
            try:
                # Localizar campo de búsqueda
                campo_busqueda = self.driver.find_element(By.XPATH,
                                                          "/html/body/div[2]/div[2]/div/mat-dialog-container/div/div/expand-core-resource-attach-dialog/div[1]/div/expand-core-resource-tree/div[1]/expand-shared-search/mat-form-field/div[1]/div/div[2]/input")

                # Limpiar el campo y escribir el permiso
                campo_busqueda.clear()
                campo_busqueda.send_keys(permiso)
                time.sleep(t)  # Esperar a que la lista se actualice

                # Localizar el checkbox y hacer click
                checkbox = self.driver.find_element(By.XPATH,
                                                    f"//mat-checkbox[@title='{permiso}']//input[@type='checkbox']")
                checkbox.click()
                print(f"✔ Permiso '{permiso}' seleccionado correctamente.")

            except Exception as e:
                print(f"❌ No se pudo seleccionar el permiso '{permiso}': {e}")


