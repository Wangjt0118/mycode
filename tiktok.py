# import openpyxl
# outwb = openpyxl.Workbook()

# outws = outwb.create_sheet(index=0)
# for i in range(1, 10):
#     outws.cell(i, 1).value = '0.3000'

# filename2 = '/Users/hws/Downloads/test.xlsx'
# outwb.save(filename2)
# print(filename2, '  down!!')


from urllib import parse
import requests
# import json

# url = "http://store.dairyqueen.com.cn/api/v1/bi/product/sales?subtotal=day&region=1&region_level=0&start_date=2021-08-11&end_date=2021-08-12&category_ids=3895644930529886111&product_is_master=false&limit=10&offset=0&stringified=true"

# payload={}
# headers = {
#   'Proxy-Connection': 'keep-alive',
#   'Cache-Control': 'max-age=0',
#   'authorization': 'Bearer pqW-1wbJPiifLN6gP0tScA',
#   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
#   'content-type': 'application/json',
#   'Accept': '*/*',
#   'Referer': 'http://store.dairyqueen.com.cn/',
#   'Accept-Language': 'zh-CN,zh;q=0.9',
#   'Cookie': 'hex_server_session=48680e9e-484c-4438-bd6d-19fd86a51fb5; hex_server_session=48680e9e-484c-4438-bd6d-19fd86a51fb5'
# }

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)
# print(response.headers)


import requests

# url = "https://v.douyin.com/eHHc1ft/"

# payload={}
# headers = {
#   'authority': 'v.douyin.com',
#   'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
#   'sec-ch-ua-mobile': '?0',
#   'upgrade-insecure-requests': '1',
#   'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
#   'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#   'sec-fetch-site': 'none',
#   'sec-fetch-mode': 'navigate',
#   'sec-fetch-user': '?1',
#   'sec-fetch-dest': 'document',
#   'accept-language': 'zh-CN,zh;q=0.9'
# }

# response = requests.request("GET", url, headers=headers, data=payload)


# 抖音基础信息
headers = {"Content-Type": "application/x-www-form-urlencoded"}
client_token = 'clt.c187ac2e49daf29ce4a9c7ff7f2199d0rbxMWjwJuaNYtd2QudRWR8DNLSiU'

# # # 核销券

# data = {
#     'verify_token': '94b5812f-cb95-46bf-9fd9-c60a7f9f305f',
#     'encrypted_codes': ['CgwIARC1HhifIyABKAESLgosnDCET1GOyJ04V4Rfvi1EhzOVxCAJtaUs+W4UOkeeBpwcUg0EoXb8VndmDIkaAA==']
# }
# response = requests.post('https://open.douyin.com/namek/fulfilment/verify/?client_token={}'.format(client_token), json=data, headers=headers)
# print(response.text, '*'* 10)
# data = {
#     'verify_token': '8366048b-1860-4be1-8d84-1677942ea604',
#     'encrypted_codes': ['CgwIARC1HhifIyABKAESLgos8OOIzb/B4brOI+V8GmOFtCPS5jg2N7U3giQBpPZoABmn9gK80a5vbjsdLPIaAA==']
# }
# response = requests.post('https://open.douyin.com/namek/fulfilment/verify/?client_token={}'.format(client_token), json=data, headers=headers)
# print(response.text, '#'* 10)


# 取消核销券
# headers = {"Content-Type": "application/json"}
# data = {
#   'verify_id': '7145745952867385356',
#   'certificate_id': '714573903614515612822'
# }

# response = requests.post('https://open.douyin.com/namek/fulfilment/cancel/?client_token={}'.format(client_token), json=data, headers=headers)

# s = response.text
# print(type(s))
# print('*' * 10)
# print(response.json())

# 券状态查询
data = {
  "encrypted_code": "CgwIARC1HhifIyABKAESLgoshAUIU48+mFFSYCy9ZirUNouquMgBPNNNEnWC92uJ9TK4Ta6d6JbdpQ9y65IaAA=="
}
# data = parse.urlencode(data)
# print(data)
response = requests.get('https://open.douyin.com/namek/fulfilment/query/certificate/?client_token={}'.format(client_token), params=data, headers=headers)
print(response.text)
print('-' * 10)
print(response.text)
print('-' * 10)
print(response.json())

# res = requests.get('https://open.douyin.com/namek/poi/query/?client_token={}&page=1&size=1000'.format(client_token))
# print(res.text)
# with open ('/Users/hws/Downloads/shop.json','w') as f:
#     f.write(res.text)

