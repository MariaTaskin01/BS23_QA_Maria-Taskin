from selenium.webdriver.common.by import By
import time

class LoginPage:

    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        self.browser.find_element(By.ID, "Username").send_keys(username)
        time.sleep(1)

        self.browser.find_element(By.ID, "Password").send_keys(password)
        time.sleep(1)

        self.browser.find_element(By.XPATH, "//button[@class='button-1 login-button']").click()
        time.sleep(1)

        assert "Welcome" in self.browser.find_element(By.XPATH, "//div[@class = 'topic-block-title']").text
