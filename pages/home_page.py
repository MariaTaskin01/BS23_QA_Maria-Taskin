from selenium.webdriver.common.by import By
import time

class HomePage:
    def __init__(self,browser):
        self.browser = browser

    def click_register(self):
        self.browser.find_element(By.XPATH,"//a[@class = 'ico-register']").click()
        time.sleep(1)

    def click_login(self):
        self.browser.find_element(By.XPATH,"//a[@class = 'ico-login']").click()
        time.sleep(1)