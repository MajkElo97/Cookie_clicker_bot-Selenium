from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = 'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(service=Service(chrome_driver_path))

url = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(url=url)

cookie = driver.find_element(by=By.ID, value="cookie")
timeout = time.time() + 60 * 5  # 5 minutes from now
time_buy = time.time() + 5
index = 0
while time.time() < timeout:
    cookie.click()
    money = int(driver.find_element(by=By.ID, value="money").text.replace(",", ""))
    items = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
    items.pop()
    items_cost = [int(item.text.split("-")[1].strip().replace(",", "")) for item in items]
    if time.time() > time_buy:
        for item in items_cost:
            if money > item:
                index = items_cost.index(item)
        items[index].click()
        time_buy = time.time() + 5
cps = driver.find_element(by=By.ID, value="cps").text.split(":")[1].strip()
print(cps)
driver.quit()
