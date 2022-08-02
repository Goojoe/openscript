import requests
import json
heads = {}
heads['User-Agent'] = 'Mozilla/5.0 ' \
                          '(Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 ' \
                          '(KHTML, like Gecko) Version/5.1 Safari/534.50'
response = requests.get('https://www.chinamoney.com.cn/r/cms/www/chinamoney/data/fx/sdds-exch-rate.json',headers=heads)

response.encoding="utf-8" 
js = response.text
# 将 JSON 对象转换为 Python 字典
data2 = json.loads(js)
print(data2['records'][0]['price'])
'''
print ("data2['name']: ", data2['name'])
print ("data2['url']: ", data2['url'])


with open('test.txt','w') as f:
   f.write(lines)
f.close()
'''
