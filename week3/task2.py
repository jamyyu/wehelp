import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import urllib.request as req
import bs4
def getHTML(url):
    request=req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36",
        "cookie":"_gid=GA1.2.757711060.1713267671; over18=1; _ga=GA1.1.1662076600.1707884199; _ga_DZ6Y3BY9GW=GS1.1.1713275170.12.0.1713275170.0.0.0"
    })

    with req.urlopen(request) as response:
        page=response.read().decode("utf-8")
    return page

def getData(url):
    root=bs4.BeautifulSoup(getHTML(url),"html.parser")
    blocks=root.find_all("div", class_="r-ent")
    nextLink=root.find("a",string="‹ 上頁")["href"]
    for block in blocks:
        title=block.find("div", class_="title")
        count=block.find("div", class_="nrec")
        if title.a != None:
            article_link="https://www.ptt.cc"+title.a["href"]
            article_data=getHTML(article_link)
            root=bs4.BeautifulSoup(article_data,"html.parser")
            article_info=root.find_all("span", class_="article-meta-value")
            if (article_info != []) and (count.string != None):
                with open("article.csv","a",encoding="utf-8") as file:
                    file.write(f"{title.a.string},{count.string},{article_info[3].string}\n")
            elif(article_info == []) and (count.string != None):
                with open("article.csv","a",encoding="utf-8") as file:
                    file.write(f"{title.a.string},{count.string},no data\n")
            elif(article_info != []) and (count.string == None):
                with open("article.csv","a",encoding="utf-8") as file:
                    file.write(f"{title.a.string},0,{article_info[3].string}\n")
            else:
                with open("article.csv","a",encoding="utf-8") as file:
                    file.write(f"{title.a.string},0,no data\n")   
    return  nextLink


page_url="https://www.ptt.cc/bbs/Lottery/index.html"
with open("article.csv", "w", encoding="utf-8") as file:
        pass 
count=0
while count<3:
    page_url="https://www.ptt.cc"+getData(page_url)
    count+=1



        

    





