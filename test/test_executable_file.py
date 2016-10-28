from pages.registration_pages import Registration_pages

#Registration

def test_registration_valid(base_url):
    x = Registration_pages(base_url)
    x.accessing_login_pages()
    print("Registration successfull")
