'''
import requests
for i in range (0,4):
    #print(a.text)
    
    a= requests.get(input('enter the url:'))
    print(a.encoding)
    print(a.status_code)
    print(a.elapsed)
    print(a.url)

a = requests.get('https://www.imdb.com/title/tt1187043/')
print(a.text[0:1001])
'''


'''
import requests
from requests_html import HTMLSession
session = HTMLSession()

r = session.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')

listerList= r.html.find('.lister-list',first=True)
print(listerList)

title = listerList.find('.titleColumn')
#print(title)
rating = listerList.find('.ratingColumn strong')

for i in range (0,len(title)):
    print(title[i].text ,"\t", rating[i].text)
    
    #print(rating[i].text)
    #print()
img = listerList.find('.posterColumn a img')
for i in img:
    print(i.attrs['src'])
    '''


'''
import requests
from requests_html import HTMLSession
session = HTMLSession()

r = session.get('https://www.imdb.com/movies-coming-soon/?ref_=nv_mv_cs')

listDetail= r.html.find('.list.detail',first=True)
#print(listDetail)
title = listDetail.find('.overview-top h4')
for i in range(0,len(title)):
    print(title[i].text)
'''



'''
import requests
from requests_html import HTMLSession
session = HTMLSession()
r = session.get('https://www.imdb.com/title/tt1187043/?ref_=nv_sr_srsg_0')

titleBar= r.html.find('.titleBar', first=True)
#print(titleBar.text)
title = titleBar.find('.title_wrapper h1')
ratingvalue= r.html.find('.ratingValue strong')
listdetail = r.html.find('.cast_list' , first=True)
cast = listdetail.find('.cast_list td a ')

for i in range(0,len(title)):
    print(title[i].text)
    print(ratingvalue[i].text)
for i in range(0,len(cast)):   
    print(cast[i].text)
'''



import requests
from requests_html import HTMLSession
session = HTMLSession()
r = session.get('https://www.imdb.com/movies-coming-soon/?ref_=nv_mv_cs')

listDetail = r.html.find('.list.detail', first=True)
movies = listDetail.find('.overview-top')
for i in range(0,len(movies)):
    print(movies[i].text)
    print('no ratings')
    print()

