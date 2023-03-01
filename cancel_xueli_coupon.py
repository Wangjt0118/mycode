import requests
import hashlib
import copy


secret_key = 'c20fea3042037c37e19a30d148cfc8b3'
member_code = 'M00016001736'
ticket_id = '34f725b787ff40db9d1e876313802de6'

def generate_sign(request_body):
    # type: (dict) -> str
    # 雪沥的签名方法, 从 request_body 中生成签名
    sorted_keys = sorted(copy.copy(list(request_body.keys())))
  
    l = []
    for k in sorted_keys:
        if request_body.get(k) is None:
            # 如果值是空不参与排序
            continue

        v = request_body[k]
        if type(v) is list or type(v) is dict:
            continue
        s = '{}={}'.format(k, v)
        l.append(s)

    l.append('key={}'.format(secret_key))
    s = '&'.join(l).encode()
    
   
    r = hashlib.md5(s).hexdigest()
   
    return r


data = dict(
	memberCode=member_code,
    externalId=ticket_id,
)

url = 'https://openapi.dairyqueen.com.cn/openapi/order/cancelSubmitOrder'

headers = {
	'sign': generate_sign(data),
	'Content-Type': 'application/json'
}

headers.update(dict(
                tenantId='1',
                channelId='105'
            ))
print(headers)
res = requests.post(url, data=data, headers=headers)
print(res.content)