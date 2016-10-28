from selenium import webdriver
import time
from pages.Locators import sign_locators

class Registration_pages(object):

    def __init__(self, base_url):
        self.driver = webdriver.Firefox()
        #self.driver.maximize_window()
        self.driver.get(base_url)

    def accessing_login_pages(self):
        driver1 = self.driver
        time.sleep(10)
        driver1.find_element(*sign_locators._a).click()
        time.sleep(10)
        driver1.find_element(*sign_locators._b).click()
        driver1.find_element(*sign_locators._c).send_keys("royston")
        driver1.find_element(*sign_locators._d).send_keys("fernandes")
        driver1.find_element(*sign_locators._e).send_keys("roystontestuser1@gmail.com")
        driver1.find_element(*sign_locators._f).send_keys("rash0207")
        driver1.find_element(*sign_locators._g).send_keys("rash0207")
        driver1.find_element(*sign_locators._h).click()
        driver1.quit()
        return
