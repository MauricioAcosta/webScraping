from bs4 import BeautifulSoup
import requests
import re

notices=[]
for i in range(1,4):
        page_link = 'https://www.proadmintierra.info/category/blog/noticias/page/'+str(i)+'/'
        page_response = requests.get(page_link, timeout=5)
        page_content = BeautifulSoup(page_response.content, "html.parser")
        #print(page_content.prettify())
        div = page_content.find_all('div', {"class" : 'meta-info-container'})
        #aux=''.join(div)
        notices.append(div)
allnotices=[]
for pageNotices in notices:
    for onenotice in pageNotices:
        allnotices.append(str(onenotice))
#print(allnotices)
textTitle=[]
#urlNotice=[]
urlsImage= []
for i in range(len(allnotices)):
    aux=allnotices[i].split()
    for item in aux:
        if re.match('src*', item) != None:
            urlsImage.append(item)

# =============================================================================
# for i in range(len(allnotices)):
#     aux=allnotices[i].split()
#     for item in aux:
#         if re.match('href="https://www.proadmintierra.info/*', item) != None:
#             urlNotice.append(item)
# =============================================================================
            
for i in range(len(allnotices)):
    aux=allnotices[0]
    result=re.match('title="\*\"', '<h3><a title="GeoPython 2019_Suiza">GeoPython 2019_Suiza"</a></h3>')
    print(result)
