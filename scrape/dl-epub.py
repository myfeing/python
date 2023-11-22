from bs4 import BeautifulSoup
import requests
import random
import time

dir = r'C:\Users\myfei\Downloads\\'
with open(dir+r"Books Alphabetical - Austin-Sparks.Net.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
all = soup.find_all('h2', class_="u-text u-text-1")
#print(all)
h2 = None
for item in all:
    if item.contents[0].string == 'T':
        h2 = item
print(h2)
if h2 != None:
    tags = h2.find_next_siblings('p')
'''    i = 0
    for tag in tags:
        if tag.contents[0].string != 'Spiritual Maturity':
            i = i + 1
        else:
            break
    tags = tags[i:]'''
print(len(tags))
for tag in tags:
    if tag.name == 'p': 
        #print(tag['class'])
        url = tag.contents[0].get('href')
        #print(url)
        req = requests.get(url)
        n = random.randrange(10, 22)
        time.sleep(n)
        page = BeautifulSoup(req.text, 'html.parser')
        ele = page.find('img', class_='u-image u-image-default u-image-2')
        if ele != None:
            fn = ele['data-href'][11:]
            lnk = r'https://www.austin-sparks.net/ePub/' + fn
            print(lnk)
            req2 = requests.get(lnk)
            with open(dir+fn, 'wb') as f:
                f.write(req2.content)

