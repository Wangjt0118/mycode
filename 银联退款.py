import requests


data = {'merchantOrderId': '45993622031273861142', 'terminalCode': u'2202009082233194872', 'merchantCode': u'811010210101001'}

headers = dict(
        Authorization='OPEN-ACCESS-TOKEN AccessToken=358d68062a16c07e628680fb55db5f7b'
    )

url = 'https://qpay.qmai.cn/poslink/transaction/voidpayment'
res = requests.post(url, json=data, headers=headers)
print(res.content)

