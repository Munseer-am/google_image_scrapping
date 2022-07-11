#! /usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

dst = "Enter path to save images"

query = str(input("Search: "))

browser = webdriver.Chrome()
browser.get("https://images.google.com")
f = browser.find_element("name", "q")
f.send_keys(query,  u'\ue007')
html = browser.find_element("xpath", '/html')

for i in range(1,11):
    try:
        image = browser.find_element("xpath", f'//*[@id="islrg"]/div[1]/div[{i}]/a[1]/div[1]/img')
        image.screenshot(f"{dst}/{query.replace(' ', '-')}{i}.png")
        time.sleep(1)
    except Exception as e:
        print(e)
        html.send_keys(Keys.PAGE_DOWN)
        continue
 
browser.close()
