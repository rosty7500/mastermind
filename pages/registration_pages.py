from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from pages.Locators import sign_locators
from selenium.webdriver.common.by import By


class Registration_pages(object):
    _a = (By.XPATH, "//div[@class='row']/div[2]/ul/li[2]/a")
    _b = (By.ID, "register-normal")
    _c = (By.ID, "UserFirstName")
    _d = (By.ID, "UserLastName")
    _e = (By.ID, "UserEmail")
    _f = (By.ID, "UserPassword")
    _g = (By.ID, "UserConfirmPassword")
    _h = (By.XPATH, "//form[@id='UserRegisterForm']/div[4]/div[6]/div[1]/button")
    _i = (By.ID, "SignupSecurityCode")
    _j = (By.ID, "captcha-submit")
    _k = (By.CLASS_NAME, "access-denied-title")
    _l = (By.ID, "user-save-fail")
    _m = (By.CLASS_NAME, "errormassage")


    def __init__(self, base_url):
        self.driver = webdriver.Firefox()
        #self.driver.maximize_window()
        self.driver.get(base_url)

    def accessing_login_pages_valid(self):
        driver1 = self.driver
        time.sleep(10)
        driver1.find_element(*sign_locators._a).click()
        time.sleep(10)
        driver1.find_element(sign_locators._b).click()
        driver1.find_element(*sign_locators._c).send_keys("royston")
        driver1.find_element(*sign_locators._d).send_keys("fernandes")
        driver1.find_element(*sign_locators._e).send_keys("Enter a new email:", Keys.ENTER)
        #driver1.find_element(*sign_locators._e).send_keys("roystontestuser104@gmail.com")
        driver1.find_element(*sign_locators._f).send_keys("rash0207")
        driver1.find_element(*sign_locators._g).send_keys("rash0207")
        driver1.find_element(*sign_locators._h).click()
        time.sleep(10)
        driver1.find_element(*sign_locators._i).send_keys("royston")
        driver1.find_element(*sign_locators._j).click()
        time.sleep(5)
        self.thankyou = driver1.find_element(*sign_locators._k).text
        driver1.quit()
        return self.thankyou


    def accessing_login_pages_invalid(self):
        driver1 = self.driver
        time.sleep(10)
        driver1.find_element(*sign_locators._a).click()
        time.sleep(10)
        driver1.find_element(*sign_locators._b).click()
        driver1.find_element(*sign_locators._c).send_keys("royston")
        driver1.find_element(*sign_locators._d).send_keys("fernandes")
        driver1.find_element(*sign_locators._e).send_keys("Enter already registered email:", Keys.ENTER)
        #driver1.find_element(*sign_locators._e).send_keys("roystontestuser104@gmail.com")
        driver1.find_element(*sign_locators._f).send_keys("rash0207")
        driver1.find_element(*sign_locators._g).send_keys("rash0207")
        driver1.find_element(*sign_locators._h).click()
        time.sleep(10)
        driver1.find_element(*sign_locators._i).send_keys("royston")
        driver1.find_element(*sign_locators._j).click()
        time.sleep(5)
        self.thankyou = driver1.find_element(*sign_locators._l).text
        driver1.quit()
        return self.thankyou


    def accessing_login_pages_blank(self):
        driver1 = self.driver
        time.sleep(10)
        driver1.find_element(*sign_locators._a).click()
        time.sleep(10)
        driver1.find_element(*sign_locators._b).click()
        driver1.find_element(*sign_locators._h).click()
        errormessage = driver1.find_element(*sign_locators._m).text
        if errormessage:
            driver1.find_element(*sign_locators._c).send_keys("royston")
            driver1.find_element(*sign_locators._h).click()
            if errormessage:
                driver1.find_element(*sign_locators._d).send_keys("fernandes")
                driver1.find_element(*sign_locators._h).click()
                if errormessage:
                    driver1.find_element(*sign_locators._e).send_keys("Enter already registered email:", Keys.ENTER)
                    driver1.find_element(*sign_locators._h).click()
                    if errormessage:
                        driver1.find_element(*sign_locators._f).send_keys("rash0207")
                        driver1.find_element(*sign_locators._h).click()
                        if errormessage:
                            driver1.find_element(*sign_locators._g).send_keys("rash0207")
                            driver1.find_element(*sign_locators._h).click()
                            print("REGISTRATION DONE :NO EMPTY FIELDS")
                            return errormessage
                        else:
                            print("END")







