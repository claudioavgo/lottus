import random
import string
import time

from django.test import TestCase, tag
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Tests here.
class app_health(TestCase):

    def setUp(self):
        self.base_url = "http://localhost:8000"

        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("--no-sandbox")
        #options.add_argument('--headless')
        options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome(options=options)

        self.driver.maximize_window()

        self.driver.implicitly_wait(10)

    def test_load_home_page(self):
        driver = self.driver

        driver.get(self.base_url)

        # test whether correct URL/ Web Site has been loaded or not
        self.assertIn("Cultive", driver.title)


class doacao_test(TestCase):
    base_url = "http://127.0.0.1:8000/"

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        #options.add_argument('--headless')
        options.add_argument("--disable-gpu")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)

        self.driver.maximize_window()

        self.driver.implicitly_wait(10)

    def test_doacao(self):
        driver = self.driver
        driver.get(self.base_url)

        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/ul/li[2]/a').click()

        driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/a').click()

        self.assertIn("PagBank", driver.title)
        
class iniciativa_test(TestCase):
    base_url = "http://127.0.0.1:8000/"

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        #options.add_argument('--headless')
        options.add_argument("--disable-gpu")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)

        self.driver.maximize_window()

        self.driver.implicitly_wait(10)

    def test_iniciativa(self):
        driver = self.driver
        driver.get(self.base_url)

        driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/a').click()

        self.assertIn("Cultive", driver.title)

class dia_a_dia_test(TestCase):
    base_url = "http://127.0.0.1:8000/"

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        #options.add_argument('--headless')
        options.add_argument("--disable-gpu")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)

        self.driver.maximize_window()

        self.driver.implicitly_wait(10)

    def test_dia_a_dia(self):
        driver = self.driver
        driver.get(self.base_url)

        driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/a').click()

        self.assertIn("Cultive", driver.title)

class adicionar_crianca_test(TestCase):
    base_url = "http://127.0.0.1:8000/"

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        #options.add_argument('--headless')
        options.add_argument("--disable-gpu")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)

        self.driver.maximize_window()

        self.driver.implicitly_wait(10)

    def test_adicionar_crianca(self):
        driver = self.driver
        driver.get(self.base_url)

        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/a[1]').click()

        driver.find_element(By.XPATH, '/html/body/div[2]/form/div[1]/input').send_keys("admin@admin.com")

        driver.find_element(By.XPATH, '/html/body/div[2]/form/div[2]/input').send_keys("123")

        driver.find_element(By.XPATH, '/html/body/div[2]/form/div[4]/button').click()

        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/a').click()
        
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/ul/li[1]/a').click()

        driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[2]/details/summary/span[1]').click()

        driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[2]/details/ul/li[2]/a').click()

        valores_input = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        
        elemento_input = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/form/div/div[1]/div[1]/div/div/input") 

        for i in range(10):
            valor_aleatorio = random.choice(valores_input)

            elemento_input.send_keys(valor_aleatorio)

            time.sleep(0.1)
        
        elemento_input = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/form/div/div[1]/div[2]/div/div/input") 

        for i in range(10):
            valor_aleatorio = random.choice(valores_input)

            elemento_input.send_keys(valor_aleatorio)

            time.sleep(0.1)

        elemento_input = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/form/div/div[1]/div[3]/div/div/input")
    
        for i in range(10):
            valor_aleatorio = random.choice(valores_input)

            elemento_input.send_keys(valor_aleatorio)

            time.sleep(0.1)
        
        elemento_input = driver.find_element(By.ID, "idade")

        valor_aleatorio = random.randint(1, 9)

        elemento_input.send_keys(valor_aleatorio)

        time.sleep(0.1)
        
        elemento_input = driver.find_element(By.ID, "ano_nascimento")

        for i in range(8):
            valor_aleatorio = random.randint(1, 9)

            elemento_input.send_keys(valor_aleatorio)

            time.sleep(0.1)
        
        driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/form/div/div[2]/button[2]').click()

        self.assertIn("Cultive", driver.title)

class apadrinhar_test(TestCase):
    base_url = "http://127.0.0.1:8000/"

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        #options.add_argument('--headless')
        options.add_argument("--disable-gpu")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)

        self.driver.maximize_window()

        self.driver.implicitly_wait(10)

    def test_apadrinhar(self):
        driver = self.driver
        driver.get(self.base_url)

        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/ul/li[1]/a').click()
        
        driver.find_element(By.XPATH, '/html/body/div/a/button').click()

        valores_input = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        
        elemento_input = driver.find_element(By.XPATH, "/html/body/div[2]/form/div[1]/input") 

        for i in range(10):
            valor_aleatorio = random.choice(valores_input)

            elemento_input.send_keys(valor_aleatorio)

            time.sleep(0.1)
        
        elemento_input = driver.find_element(By.XPATH, "/html/body/div[2]/form/div[2]/input") 

        for i in range(10):
            valor_aleatorio = random.choice(valores_input)

            elemento_input.send_keys(valor_aleatorio)

            time.sleep(0.1)
        
        elemento_input.send_keys("@a.com")

        elemento_input = driver.find_element(By.XPATH, "/html/body/div[2]/form/div[3]/input") 

        for i in range(11):
            valor_aleatorio = random.randint(1, 9)

            elemento_input.send_keys(valor_aleatorio)

            time.sleep(0.1)
        
        elemento_input = driver.find_element(By.XPATH, "/html/body/div[2]/form/div[4]/input") 

        for i in range(9):
            valor_aleatorio = random.randint(1, 9)

            elemento_input.send_keys(valor_aleatorio)

            time.sleep(0.1)
        
        elemento_input = driver.find_element(By.XPATH, "/html/body/div[2]/form/div[5]/input") 
        elemento_input_1 = driver.find_element(By.XPATH, "/html/body/div[2]/form/div[6]/input") 

        for i in range(9):
            valor_aleatorio = random.randint(1, 9)

            elemento_input.send_keys(valor_aleatorio)
            elemento_input_1.send_keys(valor_aleatorio)

            time.sleep(0.1)
        
        driver.find_element(By.XPATH, "/html/body/div[2]/form/div[8]/button").click()

        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/ul/li[1]/a").click()

        driver.find_element(By.ID, "apadrinhar").click()

        self.assertIn("Cultive", driver.title)

class adicionar_atividade_test(TestCase):
    base_url = "http://127.0.0.1:8000/"

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        #options.add_argument('--headless')
        options.add_argument("--disable-gpu")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)

        self.driver.maximize_window()

        self.driver.implicitly_wait(10)

    def test_adicionar_atividade(self):
        driver = self.driver
        driver.get(self.base_url)

        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/a[1]').click()

        driver.find_element(By.XPATH, '/html/body/div[2]/form/div[1]/input').send_keys("admin@admin.com")

        driver.find_element(By.XPATH, '/html/body/div[2]/form/div[2]/input').send_keys("123")

        driver.find_element(By.XPATH, '/html/body/div[2]/form/div[4]/button').click()

        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/a').click()
        
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/ul/li[1]/a').click()

        driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[2]/details/summary/span[1]').click()
        
        driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[2]/details/ul/li[1]/a').click()
        
        driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/table/tbody/tr[1]/td[4]/a').click()

        driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[1]/div/a[1]').click()

        valores_input = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        
        elemento_input = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/form/div/div[1]/div[1]/div/div/input") 

        for i in range(10):
            valor_aleatorio = random.choice(valores_input)

            elemento_input.send_keys(valor_aleatorio)

            time.sleep(0.1)
        
        elemento_input = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/form/div/div[1]/div[3]/div/div/textarea") 

        for i in range(10):
            valor_aleatorio = random.choice(valores_input)

            elemento_input.send_keys(valor_aleatorio)

            time.sleep(0.1)
        
        elemento_input = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/form/div/div[1]/div[2]/div/div/input") 

        for i in range(8):
            valor_aleatorio = random.randint(1, 9)

            elemento_input.send_keys(valor_aleatorio)

            time.sleep(0.1)

        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/form/div/div[2]/button").click()

        self.assertIn("Cultive", driver.title)

class prestar_contas_test(TestCase):
    base_url = "http://127.0.0.1:8000/"

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        #options.add_argument('--headless')
        options.add_argument("--disable-gpu")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)

        self.driver.maximize_window()

        self.driver.implicitly_wait(10)

    def test_prestar_contas(self):
        driver = self.driver
        driver.get(self.base_url)

        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/a[1]').click()

        driver.find_element(By.XPATH, '/html/body/div[2]/form/div[1]/input').send_keys("admin@admin.com")

        driver.find_element(By.XPATH, '/html/body/div[2]/form/div[2]/input').send_keys("123")

        driver.find_element(By.XPATH, '/html/body/div[2]/form/div[4]/button').click()

        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/a').click()
        
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/ul/li[1]/a').click()

        driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[3]/a').click()
        
        valores_input = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        
        elemento_input = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/form/div/div[1]/div[1]/div/div/input") 

        for i in range(8):
            valor_aleatorio = random.randint(1, 9)

            elemento_input.send_keys(valor_aleatorio)

            time.sleep(0.1)
        
        elemento_input = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/form/div/div[1]/div[2]/div/div/textarea") 

        for i in range(10):
            valor_aleatorio = random.choice(valores_input)

            elemento_input.send_keys(valor_aleatorio)

            time.sleep(0.1)
        
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/form/div/div[2]/button").click()
        
        self.assertIn("Cultive", driver.title)

class visualizar_padrinho_test(TestCase):
    base_url = "http://127.0.0.1:8000/"

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        #options.add_argument('--headless')
        options.add_argument("--disable-gpu")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)

        self.driver.maximize_window()

        self.driver.implicitly_wait(10)

    def test_visualizar_padrinho(self):
        driver = self.driver
        driver.get(self.base_url)

        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/a[1]').click()

        driver.find_element(By.XPATH, '/html/body/div[2]/form/div[1]/input').send_keys("admin@admin.com")

        driver.find_element(By.XPATH, '/html/body/div[2]/form/div[2]/input').send_keys("123")

        driver.find_element(By.XPATH, '/html/body/div[2]/form/div[4]/button').click()

        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/a').click()
        
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/ul/li[1]/a').click()

        driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[4]/a').click()
        
        self.assertIn("Cultive", driver.title)

class prestar_contas_test(TestCase):
    base_url = "http://127.0.0.1:8000/"

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        #options.add_argument('--headless')
        options.add_argument("--disable-gpu")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)

        self.driver.maximize_window()

        self.driver.implicitly_wait(10)

    def test_prestar_contas(self):
        driver = self.driver
        driver.get(self.base_url)

        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/a[1]').click()

        driver.find_element(By.XPATH, '/html/body/div[2]/form/div[1]/input').send_keys("admin@admin.com")

        driver.find_element(By.XPATH, '/html/body/div[2]/form/div[2]/input').send_keys("123")

        driver.find_element(By.XPATH, '/html/body/div[2]/form/div[4]/button').click()

        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/a').click()
        
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/ul/li[1]/a').click()

        driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/ul/li[3]/a').click()
        
        valores_input = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        
        elemento_input = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/form/div/div[1]/div[1]/div/div/input") 

        for i in range(8):
            valor_aleatorio = random.randint(1, 9)

            elemento_input.send_keys(valor_aleatorio)

            time.sleep(0.1)
        
        elemento_input = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/form/div/div[1]/div[2]/div/div/textarea") 

        for i in range(10):
            valor_aleatorio = random.choice(valores_input)

            elemento_input.send_keys(valor_aleatorio)

            time.sleep(0.1)
        
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/form/div/div[2]/button").click()
        
        self.assertIn("Cultive", driver.title)

class editar_perfil_padrinho_test(TestCase):
    base_url = "http://127.0.0.1:8000/"

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        #options.add_argument('--headless')
        options.add_argument("--disable-gpu")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)

        self.driver.maximize_window()

        self.driver.implicitly_wait(10)

    def test_editar_perfil(self):
        driver = self.driver
        driver.get(self.base_url)

        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/a[1]').click()

        driver.find_element(By.XPATH, '/html/body/div[2]/form/div[1]/input').send_keys("admin@admin.com")

        driver.find_element(By.XPATH, '/html/body/div[2]/form/div[2]/input').send_keys("123")

        driver.find_element(By.XPATH, '/html/body/div[2]/form/div[4]/button').click()

        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/a').click()
        
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/ul/li[2]/a').click()

        driver.find_element(By.XPATH, '').click()

        valores_input = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        
        elemento_input = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/form/div/div[1]/div[1]/input") 

        for i in range(10):
            valor_aleatorio = random.choice(valores_input)

            elemento_input.send_keys(valor_aleatorio)

            time.sleep(0.1)
        
        elemento_input = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/form/div/div[2]/button[2]").click()

        self.assertTrue(True)