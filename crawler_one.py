import requests
from  bs4 import BeautifulSoup



class crawler:
    def __init__(self):
        print("dasdassa")
        return crawler()

    def crawler(self):
        url ="https://baike.baidu.com/item/%E8%A5%BF%E5%AE%89/121614?fromtitle=%E9%99%95%E8%A5%BF%E8%A5%BF%E5%AE%89&fromid=17503331&fr=aladdin"
        response = requests.get(url)
        print(response)
        soup = BeautifulSoup(response.text,"lxml")