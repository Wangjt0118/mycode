import requests
import json
import time
import xlrd
from openpyxl import Workbook, load_workbook

#请求头部
authorization = 'Bearer iIxVvkEtNberWOPcUhjbqQ'
hex_server_session = '10dc48db-916e-4009-b524-011de6111cf1'
test_url = 'http://test.dairyqueen.com.cn'
store_url = 'http://store.dairyqueen.com.cn'
store_ppj_url = 'http://store.papajohnshanghai.com'
test_be_url = 'http://hwstest.brutcakecafe.com'
store_be_url = 'http://store.brutcakecafe.com'


headers = {
    'Connection': 'keep-alive',
    'Host': 'test.dairyqueen.com.cn',
    'Cache-Control': 'max-age=0',
    'authorization': '{}'.format(authorization),
    'content-type': 'application/json',
    'Accept': '*/*',
    'Origin': 'http://store.papajohnshanghai.com/',
    'Referer': 'http://store.papajohnshanghai.com/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'hex_server_session={}'.format(hex_server_session),
}

headers1 = {
    'authorization': '{}'.format(authorization),
    'Cookie': 'hex_server_session={}'.format(hex_server_session),
}

headers2 = {
        'authorization': '{}'.format(authorization),
        'Content-Type': 'application/json',
        'Cookie': 'hex_server_session={}'.format(hex_server_session),
    }

no_id = []
no_id_name = []
have_id = []
have_id_name = []
promotion_id_dic = {}


def get_Promotion(id):
    """
    取得促销 discount_meta 的id
    """
    url = test_url + '/api/v1/promotion/rule?search={}&is_task=true&state=draft%2Cenabled&status=&include_request=true' \
    '&is_new=true&include_state=true'.format(id)
    # print(url)
    response = requests.get(url, headers=headers1)
    # print(response.status_code)
    data = response.json()
    # print(type(data), data)
    try:
        dic = data['payload']
    except IndexError as e:
        print('促销编码{}不存在'.format(id))
        return
    if len(dic) > 1:
        print('编码不唯一，请检查')
        return
    # dic = data['payload']['context']['discount_meta']
    promotion_id = dic[0]['id']
    lis = dic[0]['context']['discount_meta']
    dis_id = lis['id']
    name = lis['name']
    if not dis_id:
        no_id.append(id)
        no_id_name.append(name)
        promotion_id_dic[id] = promotion_id
    else:
        have_id.append(id)
        have_id_name.append(name)
    return promotion_id


def get_Promotion_id(id):
    """
    取得促销 discount_meta 的id
    """
    url = test_url + '/api/v1/promotion/rule?search={}&is_task=true&state=draft%2Cenabled&status=&include_request=true' \
    '&is_new=true&include_state=true'.format(id)
    # print(url)
    response = requests.get(url, headers=headers1)
    # print(response.status_code)
    data = response.json()
    # print(type(data), data)
    try:
        dic = data['payload']
    except IndexError as e:
        print('促销编码{}不存在'.format(id))
        return
    if len(dic) > 1:
        print('编码不唯一，请检查')
        return
    # dic = data['payload']['context']['discount_meta']
    lis = dic[0]['context']['discount_meta']
    dis_id = lis['id']
    name = lis['name']
    if not dis_id:
        no_id.append(id)
        no_id_name.append(name)
    else:
        have_id.append(id)
        have_id_name.append(name)
    return


def get_discount_id(code):
    """
    取得 discount 的id
    """
    url = test_url + '/api/v1/discount?search={}&is_task=true&state=draft%2Cenabled&status=&include_request=true' \
    '&is_new=true&include_state=true'.format(code)
    # print(url)
    response = requests.get(url, headers=headers1)
    # print(response.status_code)
    data = response.json()
    # print(type(data), data)
    try:
        dic = data['payload']
    except IndexError as e:
        print('促销编码{}不存在'.format(id))
        return
    if len(dic['rows']) > 1:
        print('编码不唯一，请检查')
        return
    # dic = data['payload']['context']['discount_meta']
    promotion = dic['rows'][0]
    promotion_id = promotion['id']
    # print(promotion_id)
    return promotion_id


def get_promotion_content(id, promotion_id):
    """
    取得促销 promotion 的content
    """
    url = test_url + '/api/v1/promotion/rule/{}?stringified=true&is_new=true'.format(id)
    # print(url)
    response = requests.get(url, headers=headers1)
    # print(response.status_code)
    data = response.json()
    # print(type(data), data)
    try:
        dic = data['payload']
    except IndexError as e:
        print('促销编码{}不存在'.format(id))
        return
    dic['context']['discount_meta']['id'] = str(promotion_id)
    # print(dic)
    return dic

def update_promotion(id, dic):
    url = test_url + '/api/v1/promotion/rule/{}'.format(id)
    data = json.dumps(dic)
    response = requests.request("PUT", url, headers=headers1, data=data)
    return

def get_request_id(id):
    """
    取得促销 request 的 id
    """
    url = test_url + '/api/v1/promotion/rule?search={}&is_task=true&state=draft%2Cenabled&status=&include_request=true' \
    '&is_new=true&include_state=true'.format(id)
    # print(url)
    response = requests.get(url, headers=headers1)
    # print(response.status_code)
    data = response.json()
    # print(type(data), data)
    try:
        dic = data['payload']
    except IndexError as e:
        print('促销编码{}不存在'.format(id))
        return
    # dic = data['payload']['context']['discount_meta']
    request_id = dic[0]['request_id']
    return request_id

def apply_change(request_id):
    url = test_url + '/api/v1/promotion/rule/change/{}/apply'.format(request_id)
    # print(url)
    response = requests.request("PUT", url, headers=headers1)
    data = response.json()
    return



if __name__ == '__main__':
#     lis = [
# '202103161',
# '202103162',
# '202103163',
# '202103251',
# '202103253',
# '202103252',
# '202103291',
# '202103292',
# '202103293',
# '202103294',
# '202103295',
# '202103296',
# '202103298',
# '202103301',
# '202103311',
# '202103312',
# '202104021',
# '202104025',
# '202104052',
# '202104026',
# '202104121',
# '202104131']
    # dic = {'202103162': 4469349136514220032, '202103163': 4469358546829475840, '202103251': 4472649870634680320, '202103253': 4472661515834556416, '202103252': 4472658839805689856, '202103291': 4474046767131852800, '202103292': 4474052790672490496, '202103293': 4474053672269021184, '202103294': 4474093960840642560, '202103295': 4474095313021337600, '202103296': 4474112075267866624, '202103298': 4474133581045760000, '202103301': 4474503715035873280, '202103311': 4474782259838222336, '202103312': 4474899470061961216, '202104021': 4475545674307371008, '202104025': 4475713582522204160, '202104052': 4477676312334467072, '202104026': 4475713885422256128, '202104121': 4479121399539073024, '202104131': 4479517429409546240}
    # lis = ['202103162']
    lis = ["202104191"]
    for i in lis:
        get_Promotion(i)
    print("have_id_name", have_id_name, len(have_id_name))
    print("no_id_name", no_id_name, len(no_id_name))

    for i in lis:
        promotion_long_id = get_Promotion(i)
        print('折扣{}的长id为{}'.format(i, promotion_long_id))
        promotion = get_discount_id(i)
        print('折扣{}的折扣id为{}'.format(i, promotion))
        dic = get_promotion_content(promotion_long_id, promotion)
        update_promotion(promotion_long_id, dic)
        print('更新折扣{}的payload的id'.format(i))
        request_id = get_request_id(i)
        print('折扣{}的request_id为{}'.format(i, request_id))
        apply_change(request_id)
        print('折扣{}更新完成'.format(i))
        time.sleep(5)



