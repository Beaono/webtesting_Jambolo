from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class DynamicXpath():
    def test(self):
        baseUrl = "https://jambolo.xyzstaging.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(60)

        #Login from the marketplace
        driver.find_element(By.LINK_TEXT, "Marketplace").click()
        email = driver.find_element(By.XPATH, "//input[contains(@class,'form-control') and contains(@placeholder,'Email Address')]")
        email.send_keys("ehitta.o@gmail.com")
        password = driver.find_element(By. ID, "password")
        password.send_keys("12345678")
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='exampleModal']/div/div/div/div/div/div[2]/div[2]/div/form/div[4]/div/button").click()
        time.sleep(5)

        #Using the search button
        search = driver.find_element(By.NAME, "search")
        search.click()
        search.send_keys("Zara")
        driver.refresh()

        search1 = driver.find_element(By.NAME, "search")
        search1.send_keys("zara")
        time.sleep(10)

jamlog = DynamicXpath()
jamlog.test()