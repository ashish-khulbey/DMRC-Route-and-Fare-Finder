#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import requests
from bs4 import BeautifulSoup as bs

url = "http://www.delhimetrorail.com/metro-fares.aspx"

response = requests.get(url)
webpage = response.content
soup = bs(webpage, "html.parser")
stations = soup.select("#ctl00_MainContent_ddlFrom")
print(stations[0].text.strip())

browser = webdriver.Firefox()
browser.get("http://www.delhimetrorail.com/metro-fares.aspx")

text = input("From Station : ") # Source Station
currentselection = browser.find_element_by_id("ctl00_MainContent_ddlFrom")
select = Select(currentselection)
select.select_by_visible_text(text)

text = input("To Station : ") # Destination Station
currentselection = browser.find_element_by_id("ctl00_MainContent_ddlTo")
select = Select(currentselection)
select.select_by_visible_text(text)

enter = browser.find_element_by_css_selector("#ctl00_MainContent_btnShowFare")
enter.click()
