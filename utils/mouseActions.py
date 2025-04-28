import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

import utils.funciones
from utils.funciones import Funciones_Globales
from selenium.webdriver import ActionChains

t = 2

class base_test (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test1(self):
        driver = self.driver
        f=Funciones_Globales(driver)
        f.Navegar("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",t)
        f.Texto_Mixto_Valida("xpath", "//input[contains(@name,'username')]","Admin",t)
        f.Texto_Mixto_Valida("xpath","//input[contains(@type,'password')]","admin123", t)
        f.Click_Mixto_Valida("xpath","//button[contains(@type,'submit')]",t)

        time.sleep(t)
    def testMoveMouse(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://thotcomputacion.com.uy/",t)

        categorias = driver.find_element(By.XPATH,"//div[@class='menu-title closed'][contains(.,'CATEGORÍAS')]")
        equipoArm = driver.find_element(By.XPATH, "//li[contains(@id,'nav-menu-item-69374')]")
        playstation = driver.find_element(By.XPATH,"(//a[@href='/categoria-producto/accesorios-playstation'])[1]")
        act = ActionChains(driver)
        act.move_to_element(categorias).move_to_element(equipoArm).move_to_element(playstation).click().perform()
        time.sleep(t)

    def testDoubleClick(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://demoqa.com/buttons", t)
        f.DoubleClick("id","doubleClickBtn",t)
        msjDobuleClick = driver.find_element(By.XPATH,"//p[contains(.,'You have done a double click')]")
        if msjDobuleClick.is_displayed():
            print("Se dio doble click ")
        else:
            print("No se dio doble click")

    def testRigthClick(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://demoqa.com/buttons", t)
        f.RightClick("xpath","//button[@type='button'][contains(.,'Right Click Me')]",t)
        msjRigthClick = driver.find_element(By.XPATH,"//p[contains(.,'You have done a right click')]")
        if msjRigthClick.is_displayed():
            print("Se dio click derecho ")
        else:
            print("No se dio click derecho")

    def testDragnAndDrop(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://demo.seleniumeasy.com/drag-and-drop-demo.html", t)
        f.DragAndDrop("xpath","//span[@draggable='true'][contains(.,'Draggable 1')]","//div[contains(@dropzone,'move')]",t)

    def testDragnAndDropCualquerLugar(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://jqueryui.com/draggable/", t)
        f.DragAndDropCoordenadas("id","draggable",150,200)

    def testClickAlElementoEnCoordenadasXY(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://jqueryui.com/draggable/", t)
        f.ClickXY("xpath", "(//a[contains(.,'Draggable')])[2]", 200, 0, 4)

    def testClickAlElementoEnCoordenadasXYEnGoogle(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://www.google.com/?hl=es", t)
        f.Texto_Mixto_Valida("xpath","//textarea[contains(@id,'APjFqb')]" ,"f",2)
        f.ClickXY("xpath", "//textarea[contains(@id,'APjFqb')]", 0, 200, 4)

    def tearDown(self):
        driver = self.driver

        driver.close()


if __name__ == "__main__":
    unittest.main()
