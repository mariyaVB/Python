from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time


chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.nseindia.com/market-data/pre-open-market-cm-and-emerge-market')
time.sleep(5)
wait = WebDriverWait(driver, 10)
table = wait.until(EC.presence_of_element_located((By.ID, 'table-preOpen')))
tbody = table.find_elements(By.TAG_NAME, 'tbody')

names: list = []
prices: list = []

for row in tbody:
    tr_final_price = row.find_elements(By.CSS_SELECTOR, '.bold.text-right')
    tr_name = row.find_elements(By.CLASS_NAME, 'symbol-word-break')
    for name, price in zip(tr_name, tr_final_price):
        names.append(name.text)
        prices.append(price.text)

data = {'Имя': names, 'цена': prices}
df = pd.DataFrame(data)

df.to_csv('name_final_price.csv', index=False)
driver.quit()


driver.get('https://www.nseindia.com')
time.sleep(5)

tab_niftybank = driver.find_element(By.ID, 'tabList_NIFTYBANK').click()
time.sleep(3)

wait = WebDriverWait(driver, 5)

a_viewall = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#tab4_gainers_loosers > div.link-wrap a')))
scroll_origin = ScrollOrigin.from_element(a_viewall)
ActionChains(driver).scroll_from_origin(scroll_origin, 0, 100).perform()
time.sleep(5)

a_viewall.click()
time.sleep(10)

select_stock = (driver.find_element(By.ID, 'equitieStockSelect')).click()
time.sleep(5)

option = driver.find_element(By.XPATH, '//*[@id="equitieStockSelect"]/optgroup[4]/option[7]')
driver.execute_script("arguments[0].scrollIntoView();", option)
option.click()
time.sleep(15)

scroll_origin = ScrollOrigin.from_element(driver.find_element(By.ID, 'equitieStockTable'))
ActionChains(driver).scroll_from_origin(scroll_origin, 0, 100).perform()
time.sleep(5)

driver.quit()



