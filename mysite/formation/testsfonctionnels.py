from django.test import TestCase
from http import HTTPStatus
import re
import random
import string
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class FonctionalTestCase(StaticLiveServerTestCase):
    @classmethod
    def setUp(cls):
        super().setUpClass()
        cls.options = Options()
        cls.options.add_argument("--headless")
        cls.browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver',
        options=cls.options)
        cls.browser.implicitly_wait(3) 

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def test_can_show_app(self):
        # Je me rend sur le site localhost:8000
        # et compte y trouver une app de R&D
        # Choose your url to visit
        self.browser.get('http://127.0.0.1:8000')

        # Je remarque que "Django : Projet de Sylvie Ye"
        # figure dans le titre de la page
        self.assertIn('Django : Projet de Sylvie Ye', self.browser.title)

    def test_add_contact(self):
        '''Test d'ajout d'un contact '''

        # Je me rend sur la route de création
        # d'une nouvelle tâche
        # Choose your url to visit
        self.browser.get('http://127.0.0.1:8000/contact')

        # Je crée un nouveau message de  "Pierre" "Paul"
        # Ayant pour mail "pierre@gmail.org"
        # Avec le message "Petit message."
        lastname = self.browser.find_element_by_id("lastname")
        firstname = self.browser.find_element_by_id("firstname")
        message = self.browser.find_element_by_id("message")
        email = self.browser.find_element_by_id("email")
        # J'envoie son nom, prénom
        lastname.send_keys("Pierre")
        firstname.send_keys("Paul")
        
        # puis son email
        email.send_keys("pierre@gmail.org")
        
        # Je crée un message
        randstring = 'Test fonctionnel '.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        message.send_keys(randstring)
        
        # Je valide le formulaire et vérifie qu'il est bien ajouté
        self.browser.find_element_by_id("submit").click()
        assert randstring in self.browser.page_source

        # Je vais sur la page d'accueil
        link = self.browser.find_element_by_id("accueil")
        self.browser.execute_script("arguments[0].click();", link)
        self.assertEquals(self.browser.current_url, "http://127.0.0.1:8000/")

    def test_add_contact_2(self):
        # J'accède à la page de candidature
        self.browser.get('http://127.0.0.1:8000')
    
        link = self.browser.find_element_by_id("contact")
        self.browser.execute_script("arguments[0].click();", link)
        self.assertEquals(self.browser.current_url, "http://127.0.0.1:8000/contact")
    
        # Je crée un nouveau message de "Marie" "Antoinette"
        # Ayant pour mail "marie@gmail.org"
        lastname = self.browser.find_element_by_id("lastname")
        firstname = self.browser.find_element_by_id("firstname")
        message = self.browser.find_element_by_id("message")
        email = self.browser.find_element_by_id("email")
        # J'envoie son nom, prénom
        lastname.send_keys("Marie")
        firstname.send_keys("Antoinette")
        
        # J'oublie son email
    
        # Je crée un message
        randstring = 'Test fonctionnel 2'.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        message.send_keys(randstring)
        
        # Je valide le formulaire et vérifie qu'il n'est pas enregistré
        self.browser.find_element_by_id("submit").click()
        self.assertNotIn(randstring, self.browser.page_source)  
    
        # Je rajoute l'email oublié
        email.send_keys("marie@gmail.org")

        # Je valide le formulaire et vérifie qu'il est bien ajouté
        self.browser.find_element_by_id("submit").click()
        self.assertIn(randstring, self.browser.page_source) 

        # Je retourne sur la page du dashboard
        link = self.browser.find_element_by_id("dashboard")
        self.browser.execute_script("arguments[0].click();", link)
        self.assertEquals(self.browser.current_url, "http://127.0.0.1:8000/dashboard")