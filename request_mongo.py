import requests
import json

url = "https://store.papajohnshanghai.com/api/v1/store?code=all&include_state=true&include_total=true&relation=all&search_fields=extend_code.ex_code%2Cextend_code.us_id%2Cextend_code.ex_id%2Ccode%2Cname%2Caddress%2Crelation.geo_region.name%2Crelation.branch.name%2Crelation.distribution_region.name%2Crelation.attribute_region.name%2Crelation.formula_region.name%2Crelation.market_region.name%2Crelation.order_region.name&stringified=true&is_task=true&sort=extend_code.ex_code&order=asc&offset=0&limit=10&state=draft%2Cenabled&status=&include_request=true&is_new=true&include_state=true&_=1669601595295"

payload={}
headers = {
  'authority': 'store.papajohnshanghai.com',
  'accept': 'application/json, text/javascript, */*; q=0.01',
  'accept-language': 'zh-CN,zh;q=0.9',
  'authorization': 'Bearer NDJTLozhOrmGQtclhPO66A',
  'cache-control': 'no-cache',
  'content-type': 'application/json',
  'cookie': 'hex_server_session=d291f916-3f60-448d-9a3e-c07d86ba1829',
  'pragma': 'no-cache',
  'referer': 'https://store.papajohnshanghai.com/',
  'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
  'x-requested-with': 'XMLHttpRequest'
}

a = 1
while a < 100:

    response = requests.request("GET", url, headers=headers, data=payload)
    print(a)
    a += 1

    # print(response.text)

