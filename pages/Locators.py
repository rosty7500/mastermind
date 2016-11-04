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
    _i = (By.ID, "SignupSecurityCode")
    _j = (By.ID, "captcha-submit")
    _k = (By.CLASS_NAME, "access-denied-title")
    _l = (By.ID, "user-save-fail")
    _m = (By.CLASS_NAME, "errormassage")

class login_locators(object):
    _a = (By.XPATH, "//div[@class='row']/div[2]/ul/li[1]/a")
    _b = (By.ID, "username")
    _c = (By.ID, "password")
    _d = (By.ID, "button-submit")
    _e = (By.ID, "loginMessage")
    _f = (By.XPATH, "//div[@id='bs-example-navbar-collapse-1']/ul[2]/li/a")










