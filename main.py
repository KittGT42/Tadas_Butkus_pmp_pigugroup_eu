import time
from bs4 import BeautifulSoup
import csv
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By

headers_csv = ['EAN', 'Supplier_code']

today_day_data = f'_{datetime.now().day}_{datetime.now().month}_{datetime.now().year}'
with open(f'detailed_info_product{today_day_data}.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers_csv)

login_from_site = 'td.butkus'

password_from_site = 'ObigM$pI24Snrd939'

with webdriver.Chrome() as driver:
    driver.get("https://pmp.pigugroup.eu/")
    driver.find_element(By.ID, 'login-username').send_keys(login_from_site)
    time.sleep(2)
    driver.find_element(By.ID, 'login-password').send_keys(password_from_site)
    time.sleep(2)
    for i in range(1, 165):
        driver.get(f"https://pmp.pigugroup.eu/products?status=active&page={i}")
        time.sleep(2)
        parsing_site_page = BeautifulSoup(driver.page_source, 'lxml')
        all_products = parsing_site_page.find_all('tbody', class_='rowgroup')

        for product in all_products:
            try:
                main_info_product = product.find('ul', class_='menu specification').find_all('li')
                ean = main_info_product[0].text.strip().split(' ')[-1]
                supplier_code = main_info_product[1].text.strip().split(' ')[-1]
                print(ean, supplier_code)
                with open(f'detailed_info_product{today_day_data}.csv', 'a', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow([ean, supplier_code])
            except:
                print('Error')
