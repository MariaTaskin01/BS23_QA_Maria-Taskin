from selenium.webdriver.common.by import By
import time

class LandingPage:

    def __init__(self, browser):
        self.browser = browser

    def landing_page(self, keyword):
        self.browser.find_element(By.ID, "small-searchterms").send_keys(keyword)
        time.sleep(1)

        self.browser.find_element(By.XPATH, "//button[@class='button-1 search-box-button']").click()
        time.sleep(1)

        assert "Search" in self.browser.find_element(By.XPATH, "//div[@class = 'page-title']").text
