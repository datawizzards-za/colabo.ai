#from bs4 import BeautifulSoup
import requests
import json
import pickle
import mechanize
import urllib2 
import cookielib


cj = cookielib.CookieJar()
br = mechanize.Browser()
br.set_cookiejar(cj)
br.open("https://id.arduino.cc/auth/login/")

br.select_form(nr=2)
br.form['username'] = '209513603@stu.ukzn.ac.za'
br.form['password'] = '7UHNspiemP1P'
br.submit()

print br.response().read()


"""
for c in range(ord('a'), ord('z') + 1):
    print "On skills: ", chr(c).upper()
    src_url = "https://www.linkedin.com/directory/topics-" + chr(c) + "/"
    #print src_url
    req = requests.get(src_url)
    html_doc = req.text
    print html_doc
    bs = BeautifulSoup(html_doc, "lxml")

    for link in bs.find_all("a"):
        href = link.get("href")
        print href
"""
