import requests
from bs4 import BeautifulSoup

#获取url下的页面内容，返回soup对象
def get_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'lxml')
    return soup

#封装成函数，作用是获取列表页下面的所有相关链接 返回一个链接列表
def get_links(url):
    soup = get_page(url)
    links_div = soup.find_all('div', class_="bd")
    #links = [div.a.get('href') for div in links_div]
    links = [div.a.get('href') for div in links_div]
    return links

#url = 'http://news.baidu.com/guonei'
#url = get_links(url)
#print(url)
def get_page_info(url):
    url='https://bj.lianjia.com/zufang/101101798181.html'
    soup = get_page(url)
    price = soup.find('p',class_="content__aside--title")
    print(price)
print(get_page_info(''))
