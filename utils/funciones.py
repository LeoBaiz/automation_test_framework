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


class Funciones_Globales():

    def __init__(self, driver):
        self.driver = driver

    def Tiempo(self, tie):
        t = time.sleep(tie)
        return t

    def Navegar(self, URL, Tiempo):  # Funcion para navegar a un link
        self.driver.get(URL)
        print("\nIngresando la la URL -> {}".format(str(URL)))
        t = time.sleep(Tiempo)
        return t

    def SelxPath(self, selector):
        val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))
        val = self.driver.execute_script("arguments[0].scrollIntoView;", val)
        val = self.driver.find_element(By.XPATH, selector)
        return val

    def SelID(self, selector):
        val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))
        val = self.driver.execute_script("arguments[0].scrollIntoView;", val)
        val = self.driver.find_element(By.ID, selector)
        return val

    def Texto_Mixto_Valida(self, tipo, selector, texto, tiempo):  # Funcion para ingresar datos en un campo
        if (tipo == "xpath"):
            try:
                val = self.SelxPath(selector)
                val.clear()
                val.send_keys(texto)
                print("Ingresando en el campo -> {} el texto -> {}".format(selector, texto))
                t = time.sleep(tiempo)
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)
        elif (tipo == "id"):
            try:
                val = self.SelID(selector)
                val.clear()
                val.send_keys(texto)
                print("Ingresando en el campo -> {} el texto -> {}".format(selector, texto))
                t = time.sleep(tiempo)
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)
        else:
            print("El tipo de selector es incorrecto")

    def Click_Mixto_Valida(self, tipo, selector, tiempo):  # Funcion para dar click en un elemento
        if (tipo == "xpath"):
            try:
                val = self.SelxPath(selector)
                val.click()
                print("Damos Click en el campo {} ".format(selector))
                t = time.sleep(tiempo)
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)
        elif (tipo == "id"):
            try:
                val = self.SelID(selector)
                val.click()
                print("Damos Click en el campo {} ".format(selector))
                t = time.sleep(tiempo)
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)
        else:
            print("El tipo de selector es incorrecto")

    def DoubleClick(self, tipo, selector, tiempo=.2):  # Funcion para Dar doble click
        if (tipo == "xpath"):
            try:
                val = self.SelxPath(selector)
                act = ActionChains(self.driver)
                act.double_click(val).perform()
                print("Doble click en  -> {}".format(selector))
                t = time.sleep(tiempo)
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)
        elif (tipo == "id"):
            try:
                val = self.SelID(selector)
                act = ActionChains(self.driver)
                act.double_click(val).perform()
                print("Doble click en  -> {}".format(selector))
                t = time.sleep(tiempo)
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)
        else:
            print("El tipo de selector es incorrecto")

    def RightClick(self, tipo, selector, tiempo=.2):  # Funcion para dar click derecho
        if (tipo == "xpath"):
            try:
                val = self.SelxPath(selector)
                act = ActionChains(self.driver)
                act.context_click(val).perform()
                print("Click derecho en  -> {}".format(selector))
                t = time.sleep(tiempo)
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)
        elif (tipo == "id"):
            try:
                val = self.SelID(selector)
                act = ActionChains(self.driver)
                act.context_click(val).perform()
                print("Click derecho en  -> {}".format(selector))
                t = time.sleep(tiempo)
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)
        else:
            print("El tipo de selector es incorrecto")

    def DragAndDrop(self, tipo, selector, destino, tiempo=.2):  # Funcion para un elemento a otro elemento
        if (tipo == "xpath"):
            try:
                val = self.SelxPath(selector)
                val2 = self.SelxPath(destino)
                act = ActionChains(self.driver)
                act.drag_and_drop(val, val2).perform()
                print("Se movio el elemento -> {} hasta el elemento  -> {}".format(selector, destino))
                t = time.sleep(tiempo)
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)
        elif (tipo == "id"):
            try:
                val = self.SelID(selector)
                val2 = self.SelID(destino)
                act = ActionChains(self.driver)
                act.drag_and_drop(val, val2).perform()
                print("Se movio el elemento -> {} hasta el elemento  -> {}".format(selector, destino))
                t = time.sleep(tiempo)
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)
        else:
            print("El tipo de selector es incorrecto")

    def DragAndDropCoordenadas(self, tipo, selector, x, y,
                               tiempo=.2):  # Funcion para mover un elemento a unas coordenadas
        if (tipo == "xpath"):
            try:
                self.driver.switch_to.frame(0)  # el valor entre () es el numero de iframe correspondiente
                val = self.SelxPath(selector)
                act = ActionChains(self.driver)
                act.drag_and_drop_by_offset(val, x, y).perform()
                print("Se movio el elemento -> {} hasta las coordenadas  -> x: {} y:{} ".format(selector, x, y))
                t = time.sleep(tiempo)
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)
        elif (tipo == "id"):
            try:
                self.driver.switch_to.frame(0)  # el valor entre () es el numero de iframe correspondiente
                val = self.SelID(selector)
                act = ActionChains(self.driver)
                act.drag_and_drop_by_offset(val, x, y).perform()
                print("Se movio el elemento -> {} hasta las coordenadas  -> x: {} y:{} ".format(selector, x, y))
                t = time.sleep(tiempo)
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)
        else:
            print("El tipo de selector es incorrecto")

    def ClickXY(self, tipo, selector, x, y, tiempo=.2):  # Funcion para mover un elemento a unas coordenadas
        if (tipo == "xpath"):
            try:
                self.driver.switch_to.frame(0)  # el valor entre () es el numero de iframe correspondiente
                val = self.SelxPath(selector)
                act = ActionChains(self.driver)
                act.move_to_element_with_offset(val, x, y).click().perform()
                print("Click en el elemento -> {} en las coordenadas  -> x: {} y:{} ".format(selector, x, y))
                t = time.sleep(tiempo)
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)
        elif (tipo == "id"):
            try:
                self.driver.switch_to.frame(0)  # el valor entre () es el numero de iframe correspondiente
                val = self.SelID(selector)
                act = ActionChains(self.driver)
                act.move_to_element_with_offset(val, x, y).click().perform()
                print("Click en el elemento -> {} en las coordenadas  -> x: {} y:{} ".format(selector, x, y))
                t = time.sleep(tiempo)
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)
        else:
            print("El tipo de selector es incorrecto")

    def Select_Xpath_Text(self, Xpath, text, tiempo):  # Funcion para Manejar Select solo por Text
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, Xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView;", val)
            val = self.driver.find_element(By.XPATH, Xpath)
            val = Select(val)
            val.select_by_visible_text(text)

            print("El campo selecionado es -> {} ".format(text))
            t = time.sleep(tiempo)
            return t

        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento: " + Xpath)

    def Select_Mixto_Type(self, tipo, selector, typeSelect, dato,
                          tiempo):  # Funcion para Manejar Select en topdos los tipos
        if (tipo == "xpath"):
            try:
                val = self.SelxPath(selector)
                val = Select(val)
                if (typeSelect == "text"):
                    val.select_by_visible_text(dato)
                elif (typeSelect == "index"):
                    val.select_by_index(dato)
                elif (typeSelect == "value"):
                    val.select_by_value(dato)

                print("El campo selecionado es -> ´{}´  con el tipo ´{}´".format(dato, typeSelect))
                t = time.sleep(tiempo)
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)
        elif (tipo == "id"):
            try:
                val = self.SelID(selector)
                val = Select(val)
                if (typeSelect == "text"):
                    val.select_by_visible_text(dato)
                elif (typeSelect == "index"):
                    val.select_by_index(dato)
                elif (typeSelect == "value"):
                    val.select_by_value(dato)
                print("El campo selecionado es -> ´{}´  con el tipo ´{}´".format(dato, typeSelect))
                t = time.sleep(tiempo)
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)
        else:
            print("El tipo de selector es incorrecto")

    def UpLoad_Mixto(self, tipo, selector, ruta, tiempo):  # Funcion para Subir un archivo
        if (tipo == "xpath"):
            try:
                val = self.SelxPath(selector)
                val.send_keys(ruta)
                nombre_archivo = os.path.basename(ruta)

                print("Se subio el archivo {} en el campo {} ".format(nombre_archivo, selector))
                t = time.sleep(tiempo)
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)
        elif (tipo == "id"):
            try:
                val = self.SelxPath(selector)
                val.send_keys(ruta)
                nombre_archivo = os.path.basename(ruta)

                print("Se subio el archivo {} en el campo {} ".format(nombre_archivo, selector))
                t = time.sleep(tiempo)
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)

        else:
            print("El tipo de selector es incorrecto")

    def Check_Mixto(self, tipo, selector, tiempo):  # Funcion Radio y Check
        if (tipo == "xpath"):
            try:
                val = self.SelxPath(selector)
                val.click()
                print("Se hace click en el elemento {} ".format(selector))
                t = time.sleep(tiempo)
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)
        elif (tipo == "id"):
            try:
                val = self.SelxPath(selector)
                val.click()
                print("Se hace click en el elemento {} ".format(selector))
                t = time.sleep(tiempo)
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)
        else:
            print("El tipo de selector es incorrecto")

    def Existe(self, tipo, selector, tiempo):
        if (tipo == "xpath"):
            try:
                val = self.SelxPath(selector)
                print("El elemento {} -> Existe".format(selector))
                t = time.sleep(tiempo)
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)
                return "No existe"

        elif (tipo == "id"):
            try:
                val = self.SelID(selector)
                print("El elemento {} -> Existe".format(selector))
                t = time.sleep(tiempo)
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)
                return "No existe"
        else:
            print("El tipo de selector es incorrecto")

    def validar_elemento(self, tipo, selector, t):
        """Verifica si un elemento existe en la página."""
        try:
            if tipo == "id":
                WebDriverWait(self.driver, t).until(EC.presence_of_element_located((By.ID, selector)))
            elif tipo == "xpath":
                WebDriverWait(self.driver, t).until(EC.presence_of_element_located((By.XPATH, selector)))
            else:
                raise ValueError("El tipo de selector debe ser 'id' o 'xpath'.")

            print(f"El elemento con {tipo} '{selector}' existe.")
            return True
        except TimeoutException:
            print(f"No se encontró el elemento con {tipo} '{selector}'.")
            return False

        except ValueError as ve:
            print(ve)
            return False

    def Salida(self):
        print("Se termino la ejecucion correctamente")
