from selenium.webdriver.common.by import By
import time

class CartPage:
    def __init__(self, browser):
        self.browser = browser

    def go_to_cart(self):
        self.browser.find_element(By.CSS_SELECTOR, "a.ico-cart").click()
        time.sleep(2)

    def get_total_price(self):
        total = self.browser.find_element(By.CSS_SELECTOR, "span.value-summary").text
        return total


