from selenium.webdriver.common.by import By
import time

class ProductPage:

    def __init__(self, browser):
        self.browser = browser

    def product_1(self,product_name):
        print(f"[ACTION] Searching for product: {product_name}")
        product = self.browser.find_element(By.XPATH, f"//a[contains(text(),'{product_name}')]/parent::h2")
        add_to_cart_btn = product.find_element(By.XPATH, ".//following-sibling::div//button[contains(text(),'Add to cart')]")
        add_to_cart_btn.click()
        time.sleep(1)

    def product_2(self,product_name):
        print(f"[ACTION] Searching for product: {product_name}")
        product = self.browser.find_element(By.XPATH, f"//a[contains(text(),'{product_name}')]/parent::h2")
        add_to_cart_btn = product.find_element(By.XPATH, ".//following-sibling::div//button[contains(text(),'Add to cart')]")
        add_to_cart_btn.click()
        time.sleep(1)

