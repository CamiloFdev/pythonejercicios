from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service('C:\chromeDriver\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://www.macal.cl/auth/?redirect_uri=https://www.macal.cl/")
driver.maximize_window()
time.sleep(7)
usr = driver.find_element(By.XPATH, "//input[@id='email-input']").send_keys("user")

pw = driver.find_element(By.XPATH, "//input[@id='password-input']").send_keys("pass")
time.sleep(3)
btn =  driver.find_element(By.XPATH, "//button[@type='button'][contains(.,'CONTINUAR')]")
btn.click()

time.sleep(10)
driver.close()