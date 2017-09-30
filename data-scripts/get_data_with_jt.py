import requests
import json
import pickle
from bs4 import BeautifulSoup


main_url = "http://www.careers24.com"

descriptions = pickle.load(open("johannesburg.pkl", "rb"))

job_titles = []

for i in range(len(descriptions)):

    src_url = "http://www.careers24.com/jobs/lc-johannesburg/?sort=dateposted&page=" + str(i+1)
    req = requests.get(src_url)
    html_doc = req.text
    bs = BeautifulSoup(html_doc, "lxml")

    print "Page: ", i+1
    id = (i+1)*10 - 10

    for title in bs.find_all("span", {"itemprop": "title"}):
        descriptions[id]['job_title'] = str(title.text.encode('utf8', 'ignore'))
        print descriptions[id]
        id += 1

    file = open("johannesburg.pkl", "wb")
    pickle.dump(descriptions, file)

#with open('johannesburg.json', 'a') as f:
#    json.dump(descriptions, f)

print "done"
