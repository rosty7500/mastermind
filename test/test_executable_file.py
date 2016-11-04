from pages.registration_pages import Registration_pages
from pages.login_pages import login_pages

#Registration
'''
def test_registration_valid(base_url):
    valid_registration = Registration_pages(base_url)
    thankyou_code = valid_registration.accessing_login_pages_valid()
    thankyou_message = 'THANK YOU FOR SIGNING UP'
    assert thankyou_message == thankyou_code
    if thankyou_message == thankyou_code:
        print("REGISTRATION SUCCESSFULL")


def test_registration_invalid(base_url):
    valid_registration = Registration_pages(base_url)
    thankyou_code = valid_registration.accessing_login_pages_invalid()
    thankyou_message = 'User could not be saved. Try Again'
    assert thankyou_message == thankyou_code
    if thankyou_message == thankyou_code:
        print("DUPLICATE ENTRY")


def test_registration_blank(base_url):
    valid_registration = Registration_pages(base_url)
    error_code = valid_registration.accessing_login_pages_blank()
    empty_message = 'Can not be empty'
    assert empty_message == error_code
    if empty_message == error_code:
        print("NO EMPTY FIELDS")

#Login
def test_login_valid(base_url):
    valid_login = login_pages(base_url)
    valid_login.accessing_signin_pages_valid()
    print("SUCCESSFULLY SIGNED IN")


def test_login_invalid(base_url):
    invalid_login = login_pages(base_url)
    validation_message = invalid_login.accessing_signin_pages_invalid()
    invalid_message = 'Invalid username or password'
    assert invalid_message == validation_message
    if invalid_message == validation_message:
        print("INVALID EMAIL OR PASSWORD")'''

def test_login_multiple(base_url):
    multiple_login = login_pages(base_url)
    multiple_login.accessing_signin_pages_multiple()
    print("Successfull logins")
