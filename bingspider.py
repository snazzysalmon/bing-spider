import re
import requests
from bs4 import BeautifulSoup
import random

score=0
lastscore=0
dork=False
ip=True
randomip=True

input="192.124.249.59"

def ipgen():
    global r_ip
    r_ip = ".".join(map(str, (random.randint(0, 255)
                            for _ in range(4))))
scraped=[]
out=[]
urls=[]
def scraper(lastquery):
    global lastscore
    for x in range(int(lastscore), int(score)):
        query = re.sub("first=[0-9]*", "first=" + str(x), lastquery)
        r=requests.get(query)
        print(query)
        soup = BeautifulSoup(r.text, 'html.parser')
        for link in soup.find_all('a'):
            bs4e = (link.get('href'))
            scraped.append(bs4e)
            for z in scraped:
                try:
                    url_extract = re.findall("^http*.*.$", z)
                    for i in url_extract:
                        if "bing" not in i:
                            if "microsoft" not in i:
                                if i not in out:
                                    out.append(i)
                                    with open("database.txt", "a+") as f:
                                        for i in out:
                                            if i not in open('database.txt').read():
                                                f.write(i + "\n")
                except:
                    pass
    lastscore=score
def startup():
    global score
    global lastquery
    list=[]
    pagelist=[]
    if dork == False and ip == True and randomip == True:
        ipgen()
        input=r_ip
        print("[IP-Random] Module Selected")
        if score == 0:
            query="https://www.bing.com/search?q=ip%3a{}&&first=0&FORM=PERE".format(input)
            print(query)
        else:
            query=lastquery
        r=requests.get(query)
        soup = BeautifulSoup(r.text, 'html.parser')
        for link in soup.find_all('a'):
            links = (link.get('href'))
            list.append(links)
    for links in list:
        try:
            pages = re.findall('^/search*.*[A-Z][0-9]+$', links)
            for i in pages:
                if i not in pagelist:
                    pagelist.append(i)
        except:
            pass
    if len(pagelist)>0:
        digits=[]
        for pages in pagelist:
            thicc = re.findall("=[0-9]*", pages)
            for thic in thicc:
                digi = re.sub("=", "", thic)
                digits.append(digi)
                digits = [i for i in digits if i != '']
        lastquery=len(pagelist)-1
        if int(digits[lastquery]) > int(score):
            score=(digits[lastquery])
        else:
            print("queried")
            startup()
        lastquery=("https://www.bing.com"+pagelist[lastquery])
        print(lastquery)
        scraper(lastquery)
        print(score)
        startup()
    if len(pagelist) <= 0:
        print("Saving Urls And Restarting")
        startup()

            
startup()
#
