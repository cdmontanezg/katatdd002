from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FunctionalTest (TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()
    def test_title (self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Busco Ayuda',self.browser.title)
    def test_login(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_login')
        link.click()

        modal = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, "login_modal")))

        user = modal.find_element(By.NAME, "username")
        user.send_keys('admin')

        pswd = modal.find_element(By.NAME, "password")
        pswd.send_keys('admin1234')

        botonLogin = self.browser.find_element_by_id('id_button_login')
        botonLogin.click()
        self.browser.implicitly_wait(5)
        a = self.browser.find_element_by_id('id_editar')
        self.assertNotEqual(a, None)

    def test_edit(self):
        self.test_login()

        link = self.browser.find_element_by_id('id_editar')
        link.click()
        self.browser.implicitly_wait(4000)

        modal = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, "register_modal")))

        name = modal.find_element(By.NAME, "nombre")
        name.send_keys('Juan')

        lastName = modal.find_element(By.NAME, "apellidos")
        lastName.send_keys('Pérez Páez')

        botonSubmit = self.browser.find_element_by_id('id_grabar')
        botonSubmit.click()

        self.browser.implicitly_wait(1000)
        div = self.browser.find_element_by_id('id_welcome')
        self.assertIn("Bienvenido Juan", div.text)

