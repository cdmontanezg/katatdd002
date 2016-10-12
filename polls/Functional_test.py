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
        wait = WebDriverWait(self.browser, 10)

        user = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
        user.clear()
        user.send_keys('admin')

        pswd = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
        pswd.clear()
        pswd.send_keys('admin1234')

        botonLogin = self.browser.find_element_by_id('id_button_login')
        botonLogin.click()
        self.browser.implicitly_wait(5)
        h3 = self.browser.find_element(By.XPATH, '//h3[text()="Administrar"]')
        self.assertIn('Administrar', h3.text)


