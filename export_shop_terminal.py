import requests
import json

url = "https://store.dairyqueen.com.cn/api/v1/store?code=all&include_state=true&include_total=true&relation=all&search_fields=extend_code.ex_code%2Cextend_code.us_id%2Cextend_code.ex_id%2Ccode%2Cname%2Caddress%2Crelation.geo_region.name%2Crelation.branch.name%2Crelation.distribution_region.name%2Crelation.attribute_region.name%2Crelation.formula_region.name%2Crelation.market_region.name%2Crelation.order_region.name&stringified=true&is_task=true&sort=extend_code.ex_code&order=asc&state=draft%2Cenabled&status=&include_request=true&is_new=true&include_state=true&_=1676357126738"

payload={}
headers = {
  'authority': 'store.dairyqueen.com.cn',
  'accept': 'application/json, text/javascript, */*; q=0.01',
  'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
  'authorization': 'Bearer hoO4rqOcOgCQzvqH619OKQ',
  'content-type': 'application/json',
  'cookie': 'hex_server_session=0f39e346-35b3-49f4-8ffa-c691ea1bd21e; hex_server_session=0f39e346-35b3-49f4-8ffa-c691ea1bd21e',
  'referer': 'https://store.dairyqueen.com.cn/',
  'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
  'x-requested-with': 'XMLHttpRequest'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.json())
