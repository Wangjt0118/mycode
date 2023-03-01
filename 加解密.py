# coding:utf-8
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import json
 
class prpcrypt():
    def __init__(self,key):
        self.key = key
        self.mode = AES.MODE_CBC
     
    #加密函数，如果text不足16位就用空格补足为16位，
    #如果大于16当时不是16的倍数，那就补足为16的倍数。
    def encrypt(self,text):
        cryptor = AES.new(self.key,self.mode,b'0000000000000000')
        #这里密钥key 长度必须为16（AES-128）,
        #24（AES-192）,或者32 （AES-256）Bytes 长度
        #目前AES-128 足够目前使用
        length = 16
        count = len(text)
        if count < length:
            add = (length-count)
            #\0 backspace
            text = text + ('\0' * add)
        elif count > length:
            add = (length-(count % length))
            text = text + ('\0' * add)
        self.ciphertext = cryptor.encrypt(text)
        #因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        #所以这里统一把加密后的字符串转化为16进制字符串
        return b2a_hex(self.ciphertext)
     
    #解密后，去掉补足的空格用strip() 去掉
    def decrypt(self,text):
        cryptor = AES.new(self.key,self.mode,b'0000000000000000')
        plain_text  = cryptor.decrypt(a2b_hex(text)).decode()
        return plain_text.rstrip('\0')
 
if __name__ == '__main__':
    pc = prpcrypt('keyskeyskeyskeys') #初始化密钥
    # dic = {"pos_id": "4403080771152150528", "store_id": 3850146400234897409, "payments_raw": [], "real_pay_amount": 113.5, "reason_code": None, "qty": 4, "channels": ["710", "mt"], "table": {}, "id": None, "end_time": "2021-03-14 14:42:39", "version": "2.0", "ticket_id": "0f103022603f45c2ae272f431a02defc", "payments": [{"code": "89910712", "name": "\u7f8e\u56e2\u652f\u4ed8", "pay_amount": 91.8, "seq_id": 1, "amount": 91.8, "pay_time": "2021-03-14 14:42:39", "overflow": 0.0, "id": 4100840715882713089, "change": 0.0}, {"code": "820180519", "name": "\u5916\u5356\u4f63\u91d1\u652f\u4ed8", "pay_amount": 16.2, "seq_id": 2, "amount": 16.2, "pay_time": "2021-03-14 14:42:39", "overflow": 0.0, "id": 4100841738355728385, "change": 0.0}], "status": "CONFIRMED", "operator_id": None, "extend": {"takeaway_info": {"day_seq": "8", "refund_status": None, "consignee": "\u8d75\u8fdc\u7a0b(\u5148\u751f)", "delivery_name": "\u5b9e\u65f6\u5355", "sub_state": None, "id": None, "logs": [], "order_time": "2021-03-14 14:42:39", "complete_time": None, "package_fee": 8.0, "tp": "CANDAO", "source": "mt", "state": None, "table_number": None, "order_status": 10, "source_order_id": "20832820580006711", "cancel_time": None, "delivery_type": 1, "take_meal_sn": "", "description": "\u6536\u9910\u4eba\u9690\u79c1\u53f7 13032914378_8602\uff0c\u624b\u673a\u53f7 195****5610 ,\u5907\u4efd\u9690\u79c1\u53f7:[\"15596421649_1603\"]", "fetch_time": None, "tableware_num": 0, "order_method": "TAKEAWAY", "tp_pri_order_id": 405008867, "send_fee": 5.5, "drive_distance_desc": "4.2\u516c\u91cc(\u8fdc\u8ddd\u79bb\u4fdd\u51b7)", "pos_status": "", "tp_order_id": "210314144239524867", "invoice_no": None, "delivery_poi_address": "\u5982\u5bb6\u5feb\u6377\u9152\u5e97(\u4e34\u6f7c\u6587\u5316\u8def\u5e97) (4\u5c42416)", "delivery_time": "2021-03-14 15:17:39", "is_paid": True, "confirm_time": None, "takeout": False, "last_command": None, "refund_time": None, "invoice_title": "", "refund_message": None, "phone_list": ["13032914378_8602"], "waiting_time": ""}}, "pay_amount": 108.0, "start_time": "2021-03-14 14:42:39", "ticket_no": None, "is_void": 0, "members": {}, "reason_description": None, "coupons": [], "discount_amount": 2.0, "promotions": [{"name": "\u5916\u9001\u5546\u5bb6\u6298\u6263", "discount": 2.0, "discount_type": "discount", "promotion_id": 4102107625425686529, "promotion_code": "w0001", "type": "", "id": None}], "ref_ticket": None, "shop_amount": None, "gross_amount": 110.0, "products": [{"code": "TC0465", "name": "\u8461\u5f0f\u86cb\u631e(4\u53ea)", "seq_id": 1, "price": 30.0, "accessories": [], "qty": 1, "amount": 30.0, "combo_items": [{"code": "DP00512", "name": "\u8461\u5f0f\u86cb\u631e(1\u53ea)", "seq_id": 1, "price": 7.5, "accessories": [], "qty": 3, "amount": 22.5, "combo_items": [], "printCategory": "4390845057916272640", "type": "PRODUCT", "id": 4297661493633155072, "discount_amount": 0.0}, {"code": "DP00512", "name": "\u8461\u5f0f\u86cb\u631e(1\u53ea)", "seq_id": 1, "price": 7.5, "accessories": [], "qty": 1, "amount": 7.5, "combo_items": [], "printCategory": "4390845057916272640", "type": "PRODUCT", "id": 4297661493633155072, "discount_amount": 0.0}], "printCategory": "4390845057916272640", "type": "MEAL_BUNDLE", "id": 4299790763855773696, "discount_amount": 0.0}, {"code": "DP00675", "name": "\u6251\u6251\u6ee1\u676f-\u5de7\u514b\u529b\u914d\u86cb\u7cd5\u534e\u592b\u8106", "seq_id": 1, "price": 36.0, "accessories": [], "qty": 1, "amount": 36.0, "combo_items": [], "printCategory": "4390845057916272640", "type": "PRODUCT", "id": 4360038215317520384, "discount_amount": 0.0}, {"code": "9900793", "name": "\u5927\u676f\u731b\u6599-\u5965\u5229\u5965", "seq_id": 1, "price": 33.0, "accessories": [{"name": "+\u5965\u5229\u5965\uff08\u66f2\u5947\u997c\u5e72\uff09", "pid": 0, "price": 3.0, "editType": 0, "qty": 1, "amount": 3, "nameEn": "", "extId": "50004", "id": "3850201442438610945"}], "qty": 1, "amount": 33.0, "combo_items": [], "printCategory": "4390845057916272640", "type": "PRODUCT", "id": 3850202678592274433, "discount_amount": 0.0}, {"code": "9902025", "name": "\u6253\u5305\u8d39", "seq_id": 0, "price": 8.0, "accessories": [], "qty": 1, "amount": 8.0, "combo_items": [], "printCategory": None, "type": "PRODUCT", "id": 3911753334888857601, "discount_amount": 0.0}], "bus_date": "2021-03-14", "net_amount": 108.0, "sales_no": "210314144239524867"}
    dic = 'https://v.douyin.com/eHHc1ft/?a=123&b=abc'
    e = pc.encrypt(json.dumps(dic)) #加密
    print(u"加密前：",json.dumps(dic))
    print(u"加密后：",e)
   
    d = pc.decrypt(e) #解密
    print(u"密文：", e)
    print(u"解密后：",d)

        