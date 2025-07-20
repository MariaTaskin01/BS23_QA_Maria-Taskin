import pytest
from pages.landing_page import LandingPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage

@pytest.mark.order(1)
def test_valid_login(browser):
    home = HomePage(browser)
    home.click_login()
    login = LoginPage(browser)
    login.login("maria24","noori2011")

@pytest.mark.order(2)
def test_search(browser):
    landing = LandingPage(browser)
    landing.landing_page()

@pytest.mark.order(3)
def test_add_multiple_products(browser):
    product_page = ProductPage(browser)

    products = [
        "Awesome Gadgets",
        "Awesome Clothing"
    ]
    for product_name in products:
        product_page.add_product_by_name(product_name)


