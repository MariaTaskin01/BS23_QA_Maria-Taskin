from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class RegisterPage:
    def __init__(self,browser):
        self.browser = browser
        self.country_dropdown = (By.ID,"CountryId")
        self.state_dropdown = (By.ID,"StateProvinceId")

    def register(self, email, username, zip, region, city, phone, fax, password, country_value, state_value, click_newsletter, click_user_agreement):
        self.browser.find_element(By.ID,"Email").send_keys(email)
        time.sleep(1)
        self.browser.find_element(By.ID,"ConfirmEmail").send_keys(email)
        time.sleep(1)
        self.browser.find_element(By.ID,"Username").send_keys(username)
        time.sleep(1)
        self.browser.find_element(By.ID,"ZipPostalCode").send_keys(zip)
        time.sleep(1)
        self.browser.find_element(By.ID,"County").send_keys(region)
        time.sleep(1)
        self.browser.find_element(By.ID,"City").send_keys(city)
        time.sleep(1)

        dropdown_element = self.browser.find_element(*self.country_dropdown)
        Select(dropdown_element).select_by_value(country_value)
        time.sleep(1)

        dropdown_element = self.browser.find_element(*self.state_dropdown)
        Select(dropdown_element).select_by_value(state_value)
        time.sleep(1)

        self.browser.find_element(By.ID,"Phone").send_keys(phone)
        time.sleep(1)

        self.browser.find_element(By.ID,"Fax").send_keys(fax)
        time.sleep(1)

        newsletter_checkbox = self.browser.find_element(By.ID,"Newsletter")
        time.sleep(1)
        if click_newsletter:
            if not newsletter_checkbox.is_selected():
                newsletter_checkbox.click()
        else:
            if newsletter_checkbox.is_selected():
                newsletter_checkbox.click()

        self.browser.find_element(By.ID,"Password").send_keys(password)
        time.sleep(1)

        self.browser.find_element(By.ID,"ConfirmPassword").send_keys(password)
        time.sleep(1)

        user_agreement_checkbox = self.browser.find_element(By.ID,"accept-consent")
        time.sleep(1)
        if click_user_agreement:
            if not user_agreement_checkbox.is_selected():
                user_agreement_checkbox.click()
        else:
            if user_agreement_checkbox.is_selected():
                user_agreement_checkbox.click()

        self.browser.find_element(By.ID,"register-button").click()
        assert "completed" in self.browser.find_element(By.XPATH,"//div[@class = 'result']"), "The user already exists"

        self.browser.find_element(By.XPATH,"//div[@class = 'buttons']").click()
        time.sleep(1)





