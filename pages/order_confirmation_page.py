from selenium.webdriver.common.by import By

class OrderConfirmationPage:

    def __init__(self, browser):
        self.browser = browser

    def verify_order_summary(self):
        return "Billing Address" in self.browser.page_source

    def place_order(self):
        self.browser(By.CSS_SELECTOR, "button.confirm-order-next-step-button")

    def verify_final_confirmation(self):
        return "Your order has been successfully processed!" in self.driver.page_source
