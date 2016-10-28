__author__ = 'admin'

from selenium.webdriver.common.by import By

class sign_locators(object):
    _a = (By.XPATH, "//div[@class='row']/div[2]/ul/li[2]/a")
    _b = (By.ID, "register-normal")
    _c = (By.ID, "UserFirstName")
    _d = (By.ID, "UserLastName")
    _e = (By.ID, "UserEmail")
    _f = (By.ID, "UserPassword")
    _g = (By.ID, "UserConfirmPassword")
    _h = (By.XPATH, "//form[@id='UserRegisterForm']/div[4]/div[6]/div[1]/button")




