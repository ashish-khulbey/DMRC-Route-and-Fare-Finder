#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import requests
from bs4 import BeautifulSoup as bs

# browser = webdriver.Chrome(executable_path='/path/to/driver/chromedriver')

url = "http://www.delhimetrorail.com/metro-fares.aspx"

response = requests.get(url)
webpage = response.content
soup = bs(webpage, "html.parser")
stations = soup.select("#ctl00_MainContent_ddlFrom")
print(stations[0].text.strip())

browser = webdriver.Firefox()
browser.get("http://www.delhimetrorail.com/metro-fares.aspx")

# elem = browser.find_element_by_css_selector("#ctl00_MainContent_ddlFrom")
# Select dropdown = new Select(driver.findElement(By.id("ctl00_MainContent_ddlFrom")))
# dropdown.selectByVisibleText("TODO From Station")



text = input("From Station : ") # what ever you want to select in dropdown
currentselection = browser.find_element_by_id("ctl00_MainContent_ddlFrom")
select = Select(currentselection)
select.select_by_visible_text(text)

text = input("To Station : ") # what ever you want to select in dropdown
currentselection = browser.find_element_by_id("ctl00_MainContent_ddlTo")
select = Select(currentselection)
select.select_by_visible_text(text)

enter = browser.find_element_by_css_selector("#ctl00_MainContent_btnShowFare")
enter.click()

# select.deselect_by_visible_text("All")

# print("Selected Calgary by visible text")

# browser.find_element_by_id('ctl00_MainContent_submit1').click()