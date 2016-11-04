__author__ = 'admin'

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from pages.Locators import login_locators
import csv


class login_pages(object):
    def __init__(self, base_url):
        self.driver = webdriver.Firefox()
        #self.driver.maximize_window()
        self.driver.get(base_url)

    def accessing_signin_pages_valid(self):
        driver1 = self.driver
        time.sleep(10)
        driver1.find_element(*login_locators._a).click()
        time.sleep(5)
        driver1.find_element(*login_locators._b).send_keys("Enter registered email:", Keys.ENTER)
        time.sleep(15)
        driver1.find_element(*login_locators._c).send_keys("Enter associated password:", Keys.ENTER)
        driver1.find_element(*login_locators._d).click()
        driver1.quit()

    def accessing_signin_pages_invalid(self):
        driver1 = self.driver
        time.sleep(10)
        driver1.find_element(*login_locators._a).click()
        time.sleep(10)
        driver1.find_element(*login_locators._b).send_keys("roy@sj.com")
        time.sleep(5)
        driver1.find_element(*login_locators._c).send_keys("rash0207")
        driver1.find_element(*login_locators._d).click()
        time.sleep(5)
        self.invalid_login_message = driver1.find_element(*login_locators._e).text
        driver1.quit()
        return self.invalid_login_message


    def accessing_signin_pages_multiple(self):
        with open('login-import-data.csv') as csv_file:
            readCSV = csv.reader(csv_file, delimiter=',')
            u = []
            p = []
            for row in readCSV:
                username = row[0]
                password = row[1]
                u.append(username)
                print(u)
                p.append(password)
                print(p)

            for i in range(0, len(u)):
                driver1 = self.driver
                time.sleep(10)
                driver1.find_element(*login_locators._a).click()
                time.sleep(10)
                #WebDriverWait(driver1, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "login")))
                driver1.find_element(*login_locators._b).send_keys(u[i])
                time.sleep(5)
                driver1.find_element(*login_locators._c).send_keys(p[i])
                driver1.find_element(*login_locators._d).click()
                time.sleep(20)
                driver1.find_element(*login_locators._f).click()
                time.sleep(20)
                i=i+1













