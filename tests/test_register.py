import pytest
from pages.register_page import RegisterPage
from pages.home_page import HomePage

@pytest.mark.order(1)
def test_valid_register(browser):
    home = HomePage(browser)
    home.click_register()
    register = RegisterPage(browser)
    register.register(
        "mariataskin63@gmail.com",
        "maria24",
        "1219",
        "Dhaka",
        "Dhaka",
        "01708427778",
        "01708427778",
        "noori2011",
        "19",
        "70",
        "FALSE",
        "FALSE"
    )