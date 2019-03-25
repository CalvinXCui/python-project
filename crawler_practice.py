import requests
from  bs4 import BeautifulSoup

url = "https://www.baidu.com"
response = requests.get(url)
soup = BeautifulSoup(response.text,'lxml')
links_div = soup.find_all('div',class_="head_wrapper")
links = [div.a for div in links_div]
print(links)
lable = [div.img for div in links_div]
print(lable)