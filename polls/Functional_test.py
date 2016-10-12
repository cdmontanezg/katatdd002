from unittest import TestCase
from selenium import webdriver

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
        usuario = self.browser.find_element_by_id('id_username')
        usuario.send_keys('admin')
        pswd = self.browser.find_element_by_id('id_password')
        pswd.send_keys('admin1234')
        botonLogin = self.browser.find_element_by_id('id_button_login')
        botonLogin.click()
        self.browser.implicity_wait(5)
        h3 = self.browser.find_element(By.XPATH, '//h3[text()="Administrar"]')
        self.assertIn('Administrar', h3.text)


