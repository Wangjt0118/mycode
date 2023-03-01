import requests
import json

corip_id = 'wwd3c8a2e69de3864a'
s_id = 'l9bORWigG1hdNdbdImMj9KL6tmf3qK7QRgknUUDkAgE'
a_id = '1000003'

# token = '2wsMvETBtUDg6miwtCumoRjEG0GqERDKzfaHrtOdTC9AqUl8gsnwQu6a38AHeFcW_BmwazE1GdnMgTIiYnQArm0xS28STLy3d8Go1v-JVvjEBsbLraKQJguRhvPRVAQh3eFw7624R8GLdHe7he8TS8tUwxRoNb9BlMwY64k6FpUX2esOgONiz5HEEePN-NmR8m7BNzLW5LEKhf7EGijJqQ'

def get_token(c_id, s_id):
	url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={}&corpsecret={}'.format(c_id, s_id)

	response = requests.get(url)
	print(response.json())
	token = response.json().get('access_token')

	return token
	

def get_agent_scope(token):
	url = 'https://qyapi.weixin.qq.com/cgi-bin/agent/get?access_token={}&agentid={}'.format(token, a_id)
	resp = requests.get(url)
	print(resp.json())

def get_user_info(token, u_id):
	url = 'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={}&userid={}'.format(token, u_id)
	resp = requests.get(url)
	print(resp.json())

def send_message(token, u_id):
	url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}'.format(token)
	data = {
		"touser" : u_id,
		"msgtype": "text",
		"agentid": a_id,
		"text": {
			"content": "<a href=\"https://open.weixin.qq.com/connect/oauth2/authorize?appid=wwd3c8a2e69de3864a&redirect_uri=http%3A%2F%2Fh5.store.meet-xiaomian.com%2Flogin&response_type=code&scope=snsapi_userinfo&agentid=1000002&state=YMHexLogin&connect_redirect=1#wechat_redirect\">有物料即将过期，请查看</a>"
		}
	}
	requests.post(url, json.dumps(data))


def get_department(toekn):
	url = 'https://qyapi.weixin.qq.com/cgi-bin/department/get?access_token={}&id=2'.format(token)
	resp = requests.get(url)
	print(resp.json())

token = get_token(corip_id, s_id)
get_user_info(token, 'peng.zhen')
# print(get_token(corip_id, s_id))

# get_agent_scope(token)

# send_message(token, 'CeShiGongSi')

# get_department(token)