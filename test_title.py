# coding: utf-8
# param = "{\n" + \
#             "\"columnNames\": [\n" + \
#             "\"location_id\",\n" + \
#             "\"store_id\",\n" + \
#             "\"store_name\",\n" + \
#             "\"b_date\",\n" + \
#             "\"serial\",\n" + \
#             "\"start_time\",\n" + \
#             "\"end_time\",\n" + \
#             "\"receivable\",\n" + \
#             "\"real_income\",\n" + \
#             "\"discount_amount\",\n" + \
#             "\"is_chargeback\",\n" + \
#             "\"chargeback\",\n" + \
#             "\"time\",\n" + \
#             "\"refresh_time\",\n" + \
#             "],\n" + \
#             "\"keyCol\":\"store_id,serial\",\n" + \
#             "\"records\": [\n" + \
#             "[\n" +\
#             "\"%(location_id)s\",\n" + \
#             "\"%(store_id)s\",\n" + \
#             "\"%(store_name)s\",\n" + \
#             "\"%(b_date)s\",\n" + \
#             "\"%(serial)s\",\n" + \
#             "\"%(start_time)s\",\n" + \
#             "\"%(end_time)s\",\n" + \
#             "\"%(receivable)s\",\n" + \
#             "\"%(real_income)s\",\n" + \
#             "\"%(discount_amount)s\",\n" + \
#             "\"%(is_chargeback)s\",\n" + \
#             "\"%(chargeback)s\",\n" + \
#             "\"%(time)s\",\n" + \
#             "\"%(refresh_time)s\",\n" + \
#             "],\n" + \
#             "],\n" + \
#             "\"tableName\": \"Business\"\n" + \
#             "}"
# param = param % {
#         'location_id': "200851",
#         'store_id': "110010082",
#         'store_name': "DQ",
#         'b_date': "2022-10-21",
#         'serial': 46809992755463782411111,
#         'start_time': "2022-10-21 10:18:34",
#         'end_time': "2022-10-21 10:18:34",
#         'receivable': 53.0,
#         'real_income': 53.0,
#         'discount_amount': 0,
#         'is_chargeback': "否",
#         'chargeback': 0,
#         'time': "2022-10-21 11:42:22",
#         'refresh_time': "2022-10-21 11:42:22"
#     }
# # print(param)

# # import base64
# # from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher
# # from Crypto.PublicKey import RSA

# # def encryption(text, public_key):
# #     # 字符串指定编码（转为bytes）
# #     text = text.encode('utf-8')
# #     # 构建公钥对象
# #     cipher_public = PKCS1_cipher.new(RSA.importKey(public_key))
# #     text_encrypted = cipher_public.encrypt(text) 
# #     # base64编码，并转为字符串
# #     # print(text_encrypted)
# #     text_encrypted_base64 = base64.b64encode(text_encrypted)
# #     return text_encrypted_base64 

# # public_key = """-----BEGIN RSA PUBLIC KEY-----
# # MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCIsGBo7H2RwlwS0p01THCCA8vX6keZ143G+pP1MMtDve9lPPgRt2IAUAmGc/79a9O69C1u5j+ebdK9a5BfjXwQcyEgV2nRlJjr83O0zwoTp6Mc4WuT5ACNGrHUdijxBW9O+pZRmql5nZES8HrkKb0EtsF6PRguqmFsxg1t3eeqSQIDAQAB
# # -----END RSA PUBLIC  KEY-----
# # """


# # qiye_code = '000062'
# # qiye_ser = '38ab46f762e63b64'

# # a = encryption(qiye_code, public_key)
# # b = encryption(qiye_ser, public_key)

# # print('corporationCode: %s' % a)
# # print('ser: %s' % b)

# # from pyDes import des, CBC, PAD_PKCS5, ECB


# # def des_encrypt(s):
# #     # secret_key = KEY[:8]
# #     # iv = secret_key
# #     # k = des(secret_key, CBC, b'00000000', pad=None, padmode=PAD_PKCS5)
# #     # # print(k.__dict__)
# #     # k.setKey(base64.b64decode(qiye_ser))
# #     # # print(k.__dict__)
# #     # en = k.encrypt(s, padmode=PAD_PKCS5)


# #     secret_key1 = b'%s' % base64.b64decode(qiye_ser)
# #     secret_key = secret_key1[:8]
# #     iv = secret_key
# #     k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
# #     # k.setKey(base64.b64decode(qiye_ser))
# #     en = k.encrypt(s, padmode=PAD_PKCS5)

# #     return base64.b64encode(en)

# # data = des_encrypt(param)
# # print('*' * 10)
# # print('data: %s' % data)







# # from Crypto.Cipher import DES

# # def new_des(s_data):
# #     pad = 8 - len(s_data) % 8
# #     pad_str = ""
# #     for i in range(pad):
# #         pad_str = pad_str + chr(pad)

# #     generator = DES.new(base64.b64decode(qiye_ser)[:8], DES.MODE_ECB)

# #     encrypted = generator.encrypt(s_data + pad_str)

# #     new_data = base64.b64encode(encrypted)
# #     return new_data

# # new_data = new_des(param)
# # print('new_data: %s' % new_data)

# # import requests
# # data = {
# #     'corporationCode': a,
# #     'data': new_data
# # }
# # res = requests.post('https://bi.tcsl.com.cn:8055/lb/api/data/str', json=data, headers={'Content-Type': 'application/json; charset=utf-8'})
# # print(res.json())


# # generator = DES.new(base64.b64decode(qiye_ser)[:8], DES.MODE_ECB)
# # origin_str = generator.decrypt(base64.b64decode(new_data))

# # print(len(origin_str))
# # print(type(origin_str))

# # print(eval(origin_str))




# a = {'247': '12321', '136': "23123", '123': '23454231', '112': '2341'}
# print(a)

from xlsxwriter.workbook import Workbook
path = '/Users/hws/Downloads/test.xlsx'
workbook = Workbook(path)
worksheet = workbook.add_worksheet('lalall')
worksheet.write_number(0, 0, 1)
print('sssss')







