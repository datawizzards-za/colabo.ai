import requests
import json
import pickle
from bs4 import BeautifulSoup


# The selenium module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


#driver = webdriver.Chrome('/home/asive/Documents/projects/toka/chromedriver') 
driver = webdriver.PhantomJS('../../../../toka/phantomjs-2.1.1-linux-x86_64/bin/phantomjs',
                             service_args=['--ignore-ssl-errors=true'])

driver.get("https://www.linkedin.com/uas/login?goback=&trk=hb_signin") # load the web page

username = driver.find_element_by_id("session_key-login")
username.send_keys("209513603@stu.ukzn.ac.za");
password = driver.find_element_by_id("session_password-login")
password.send_keys("7UHNspiemP1P");

button = driver.find_element_by_id("btn-primary")
button.submit()

for c in range(ord('a'), ord('z') + 1):
    print "On skills: ", chr(c).upper()
    driver.get("https://www.linkedin.com/directory/topics-" + chr(c) + "/")
    html_doc = driver.page_source
    bs = BeautifulSoup(html_doc, "lxml")

    for div in bs.find_all('div', {'class': ['section', 'last']}):
        for a in div.find_all('a'):
            print a.text
