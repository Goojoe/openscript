import requests
from bs4 import BeautifulSoup
#soup = BeautifulSoup(open("index.html"))
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
# params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
#羊毛网站->'https://www.huilv.cc/USD_CNY/'
response = requests.get('https://www.huilv.cc/USD_CNY/', headers = headers)
# 查看响应内容，response.text 返回的是Unicode格式的数据
data=response.text
#print(data)
soup = BeautifulSoup(data,"lxml")
text=str(soup)
pos=text.find(r'<span class="back">')
#这个是汇率
got_mes=eval(text[pos+19:pos+25])
print("汇率是：%f"%got_mes)



