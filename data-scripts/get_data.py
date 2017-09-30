import requests
import json
import pickle
from bs4 import BeautifulSoup


main_url = "http://www.careers24.com"
#src_url = "http://www.careers24.com/jobs/lc-johannesburg/?sort=dateposted&ref=sbj"

descriptions = []
try:
    descriptions = pickle.load(open("johannesburg.pkl", "rb"))
except:
    print "Something went wrong"

for i in range(int(len(descriptions)/10)+1, 484):
    src_url = "http://www.careers24.com/jobs/lc-johannesburg/?sort=dateposted&page=" + str(i)
    req = requests.get(src_url)
    html_doc = req.text
    bs = BeautifulSoup(html_doc, "lxml")

    print "Page: ", i
    id = i*10 - 9
    del descriptions[id:]
    print "Length: ", len(descriptions) 

    for link in bs.find_all("a"):
        href = link.get("href")
        if link.text == "See more.":
            detail = main_url + href
            req = requests.get(detail)
            html_doc = req.text
            bs1 = BeautifulSoup(html_doc, "lxml")

            for e in bs1.find_all(["br"]):
                e.extract()

            for desc in bs1.find_all("span", {"itemprop": "description"}):
                data = {"description": desc.text.encode('utf8', 'ignore'), 
                        "id": id}
                print(data)
                descriptions.append(data)
                id += 1

    file = open("johannesburg.pkl", "wb")
    pickle.dump(descriptions, file)

with open('johannesburg.json', 'a') as f:
    json.dump(descriptions, f)

print "done"
