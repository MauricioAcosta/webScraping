from bs4 import BeautifulSoup
import requests
import re
import json

notices=[]
titlenotices=[]
hrefnotices=[]
for i in range(1,4):
        page_link = 'https://www.proadmintierra.info/category/blog/noticias/page/'+str(i)+'/'
        page_response = requests.get(page_link, timeout=5)
        page_content = BeautifulSoup(page_response.content, "html.parser")
        #print(page_content.prettify())
        div = page_content.find_all('div', {"class" : 'meta-info-container'})
        #aux=''.join(div)
        notices.append(div)
        for title in page_content.find_all('h3', {"class" : 'entry-title td-module-title'}):
            if title.text not in titlenotices:
                hrefnotices.append(str(title.find('a')))
                titlenotices.append(title.text)
                
                 
allnotices=[]
for pageNotices in notices:
    for onenotice in pageNotices:
        allnotices.append(str(onenotice))

urlsImage= []
for i in range(len(allnotices)):
    aux=allnotices[i].split()
    for item in aux:
        if re.match('src*', item) != None:
            urlsImage.append(item)

hreftitle=[]
for i in hrefnotices:
    aux=i.split()
    for item in aux:
        if re.match('href*', item) != None:
            hreftitle.append(item)
listjson=[]
for i in range(len(hrefnotices)):
    jsonreturn = {'title'+str(i):titlenotices[i], 'image'+str(i):urlsImage[i], 'urlNotice'+str(i):hreftitle[i]}
    listjson.append(jsonreturn)

# =============================================================================
# for i in listjson:
#     print(i)
# =============================================================================
