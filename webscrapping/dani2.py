'''
import bs4
from bs4 import BeautifulSoup
import requests

url = 'http://programmersclub.co.in/'
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data , 'lxml')
print(soup.prettify())
'''
# import requests
# import bs4
# from bs4 import BeautifulSoup


# r = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')
# data = r.text
# soup = BeautifulSoup(data,'lxml')
# #print(soup.prettify())
# title = soup.find_all('.titleColumn')
# for i in title:
#     print(i.get_text())
# print(title)
# for i in range(1,51):
#     r = 'http://books.toscrape.com/catalogue/page-'+str(i)+'.html'
#     print(r)

# import bs4
# from bs4 import BeautifulSoup
# import requests

# for i in range(1,52):
#     a =  'http://books.toscrape.com/catalogue/page-'+str(i)+'.html'
#     response = requests.get(a)
#     data = response.text
#     soup = BeautifulSoup(data , 'lxml')
#     print(soup.prettify())
#     print('.................................................................................')

# m = int(input('enter the starting page:'))
# n = int(input('enter the end page:'))
# for i in range(m,n+1):
#     a = 'https://www.freepik.com/search?dates=any&format=search&page='+str(i)+'&query=wallpaper&sort=popular'
#     response = requests.get(a)
#     data = response.text
#     soup = BeautifulSoup(data,'lxml' )
#     print(soup.prettify())
#     print('.....................end of'+str(i)+'..................................')

'''
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import csv
session = HTMLSession()
urls =[]
for i in range(1,51):
    urls.append(f'http://books.toscrape.com/catalogue/page-{i}.html')

csv_file = open('book.csv','w')
csv_writer = csv.writer(csv_file, lineterminator='\n')
csv_writer.writerow(['TITLE','PRICE','IMAGEURL'])
count = 1
for url in urls:
    source = session.get(url).html.html
    soup = BeautifulSoup(source, 'lxml')
    box = soup.find('ol')
    elements = box.find_all('li')
    title = []
    picture = []
    cost = []
    for element in elements:
        name = element.select('h3 a')[0]['title']
        title.append(name)
        image = element.select('img')[0]['src']
        image_url = r'https://books.toscrape.com/'+image
        picture.append(image_url)
        price = element.find('p',class_='price_color').text
        cost.append(price)
        csv_writer.writerow([name,price,image_url])
        print(count,'')
        count += 1

csv_file.close()
'''

from bs4 import BeautifulSoup
from requests_html import HTMLSession
import csv
session = HTMLSession()
urls =[]
for i in range(1,30):
    urls.append(f'https://www.zomato.com/mumbai/order-food-online?utm_source=google&utm_medium=cpc&utm_term=zomato&utm_campaign=Gsearch_P-MWeb_O-NA_C-Brand_A-NewUser_SC-Generic_L-Mumbai&gclid=CjwKCAiA-P7xBRAvEiwAow-Vaalr2jTOvSn87XxEJ7sXRQZWLXhBKcGU7mNGKnfs2kSbjNxdjpseHhoC3XwQAvD_BwE&page={i}')

csv_file = open('dish.csv','w')
csv_writer = csv.writer(csv_file, lineterminator='\n')
csv_writer.writerow(['NAME','CUISINE','RATING','IMAGEURL'])
count = 1
for url in urls:
    source = session.get(url).html.html
    soup = BeautifulSoup(source, 'lxml')
    box = soup.find('div', class_='col-s-16 search_results mbot')
    elements = box.find_all('div' , class_='content-search-result')
    name = []
    # cuisine = []
    # rating = []
    # picture = []
    for element in elements:
        print('...................................')
        name1 = element.find('div', class_='result-order-flow-title hover_feedback zred bold   fontsize0 ln20 ').text.str
        name.append(name1)
        # image = element.select('feat-img')[0]['data-original']
        # picture.append(image)
        # rating1 = element.find('rating-popup rating-for-44023 res-rating-nf right level-7 bold').text
        # rating.append(rating1)
        # cuisine1 = element.select('grey-text nowrap ln24')[0]
        # cuisine.append(cuisine1)
        csv_writer.writerow([name1])
        print(count,'')
        count += 1

csv_file.close()

