# coding=utf8
import zeep
from zeep import Client
from zeep.cache import SqliteCache
from zeep.transports import Transport
# 定义WebService的访问地址和参数
wsdl = 'http://58.33.130.242:10001/frdif/n_frdif.asmx?WSDL'
username = 'test'
password = '00B54E5ADD61AC9C'
cmdid = '2000'
# inputpara = "'01','W-B119','0012','123213123','2023-04-07 16:00:00','1','000228',20.00,1,20.00,0001,,,20,0,0,0,0"   # 根据具体需求自定义
inputpara = "01,W-B119,0012,12321312312,2023-04-07 16:00:00,1,000228,20.00,1,20.00,0001,,,20,0,0,0,0"   # 根据具体需求自定义
outputpara = ''
return_val = 0
errormsg = ''


class DQConfig(object):
    WEBSERVICE = 'http://58.33.130.242:10001/frdif/n_frdif.asmx?WSDL'
    GATEWAY_TIME_OUT = 60


class WebServiceApi(object):
    def __init__(self, config):
        self.config = config
        self.__transport = None
        self.__client = None
        self.__port_name = None
    def client(self):
        if self.__client is None:
            self.__transport = Transport(cache=SqliteCache())
            self.__client = Client(self.config.WEBSERVICE, transport=self.__transport)
        return self.__client

    def sync_processdata(self, url, **kwargs):
        service = self.client().create_service('{http://tempurl.org}n_frdifSoap', url)
        res = service.processdata(**kwargs)
        return res

api = WebServiceApi(DQConfig)
data = {}
# data['transStr'] = inputpara
data['userid'] = 'test'
data['password'] = '00B54E5ADD61AC9C'
data['cmdid'] = '2000'
data['inputpara'] = inputpara
data['outputpara'] = ''
data['rtn'] = 1
data['errormsg'] = ''
resp = api.sync_processdata(wsdl, **data)
print(resp)
print(resp.errormsg)
print(resp['errormsg'])
print(resp['rtn']==-1)
