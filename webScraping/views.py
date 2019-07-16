import json
import requests
import os
import subprocess
import re
from django.http import HttpResponse
from bs4 import BeautifulSoup

def noticias(request):        
    notices=[]
    titlenotices=[]
    hrefnotices=[]
    for i in range(1,4):
            page_link = 'https://www.proadmintierra.info/category/blog/noticias/page/'+str(i)+'/'
            page_response = requests.get(page_link, timeout=10)
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
        if i!=19:
            jsonreturn = {'title'+str(i):titlenotices[i], 'image'+str(i):urlsImage[i][5:-1], 'urlNotice'+str(i):hreftitle[i][6:-1]}
            listjson.append(jsonreturn)
        if i == 19:
            jsonreturn = {'title'+str(i):titlenotices[i], 'image'+str(i):urlsImage[i][8:], 'urlNotice'+str(i):hreftitle[i][6:-1]}
            listjson.append(jsonreturn)
    return HttpResponse(json.dumps(listjson), content_type='application/json')