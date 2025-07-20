from selenium.webdriver.common.by import By
import time

class CheckoutPage:
    def __init__(self, browser):
        self.browser = browser

    def fill_billing_address(self, address):
        self.browser.find_element(By.ID, "BillingNewAddress_FirstName").clear()
        self.browser.find_element(By.ID, "BillingNewAddress_FirstName").send_keys(address["first_name"])
        self.browser.find_element(By.ID, "BillingNewAddress_LastName").clear()
        self.browser.find_element(By.ID, "BillingNewAddress_LastName").send_keys(address["last_name"])
        self.browser.find_element(By.ID, "BillingNewAddress_Email").clear()
        # Email might be prefilled, so skip or fill if needed
        self.browser.find_element(By.ID, "BillingNewAddress_CountryId").send_keys(address["country"])
        self.browser.find_element(By.ID, "BillingNewAddress_City").clear()
        self.browser.find_element(By.ID, "BillingNewAddress_City").send_keys(address["city"])
        self.browser.find_element(By.ID, "BillingNewAddress_Address1").clear()
        self.browser.find_element(By.ID, "BillingNewAddress_Address1").send_keys(address["address"])
        self.browser.find_element(By.ID, "BillingNewAddress_ZipPostalCode").clear()
        self.browser.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys(address["zip"])
        self.browser.find_element(By.ID, "BillingNewAddress_PhoneNumber").clear()
        self.browser.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys(address["phone"])
        self.browser.find_element(By.CSS_SELECTOR, "button.new-address-next-step-button").click()
        time.sleep(2)

    def continue_shipping(self):
        self.browser.find_element(By.CSS_SELECTOR, "button.shipping-method-next-step-button").click()
        time.sleep(2)

    def continue_payment(self):
        self.browser.find_element(By.CSS_SELECTOR, "button.payment-method-next-step-button").click()
        time.sleep(2)

    def fill_payment_info(self, payment):
        # Select Card Type dropdown
        card_type_select = self.browser.find_element(By.ID, "CreditCardType")
        for option in card_type_select.find_elements(By.TAG_NAME, 'option'):
            if option.text == payment["card_type"]:
                option.click()
                break

        self.browser.find_element(By.ID, "CardholderName").send_keys(payment["cardholder_name"])
        self.browser.find_element(By.ID, "CardNumber").send_keys(payment["card_number"])
        self.browser.find_element(By.ID, "ExpireMonth").send_keys(payment["expiry_month"])
        self.browser.find_element(By.ID, "ExpireYear").send_keys(payment["expiry_year"])
        self.browser.find_element(By.ID, "CardCode").send_keys(payment["cvv"])
        self.browser.find_element(By.CSS_SELECTOR, "button.payment-info-next-step-button").click()
        time.sleep(2)

    def confirm_order(self):
        self.browser.find_element(By.CSS_SELECTOR, "button.confirm-order-next-step-button").click()
        time.sleep(3)

    def get_order_success_message(self):
        return self.browser.find_element(By.CSS_SELECTOR, "div.title").text
