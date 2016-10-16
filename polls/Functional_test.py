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

        name = self.browser.find_element(By.NAME, "nombre")
        name.clear()
        name.send_keys('Juan')

        lastName = self.browser.find_element(By.NAME, "apellidos")
        lastName.clear()
        lastName.send_keys('Pérez Páez')

        botonSubmit = self.browser.find_element_by_id('id_grabar')
        botonSubmit.click()

        self.browser.implicitly_wait(1000)
        a = self.browser.find_element_by_id('id_welcome')
        self.assertIn("Bienvenido Juan", a.text)

    def test_comment(self):
        self.browser.get('http://localhost:8000')

        link = self.browser.find_element_by_id('id_trabajador_Juan')
        link.click()
        self.browser.implicitly_wait(500)

        correo = self.browser.find_element(By.ID, "correo")
        correo.clear()
        correo.send_keys('correo@correo.com')

        comentario = self.browser.find_element(By.ID, "comentario")
        comentario.clear()
        comentario.send_keys('comentario test')

        botonSubmit = self.browser.find_element_by_id('id_comentar')
        botonSubmit.click()

        self.browser.implicitly_wait(1000)
        p = self.browser.find_element(By.XPATH, '//p[text()="comentario test"]')
        self.assertIn("comentario test", p.text)

