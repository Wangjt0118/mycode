# coding:utf-8

import psycopg2
import datetime
import json
import requests


def conn_pg_get_info():
    error = ''
    rows = []
    result = []
    total = 0
    try:
        conn = psycopg2.connect(host='rm-uf6ad3241v0k432qb.pg.rds.aliyuncs.com', port='3433', database='hex_estate_bi',
                                user='postgres', password='Hex@1qaz2wsx')

        cursor = conn.cursor()

        cursor.execute("""

		SELECT
			store_name || '[' || store_code || ']' store_name,
			sync_type,
		CASE
				
				WHEN sync_type IN ( 'HTTP', 'TCP', 'WebSerT', 'WebService', 'Webservice' ) THEN
			CASE
					
					WHEN date_part( 'day', now() - sync_time :: TIMESTAMP ) > 1 THEN
					'error' ELSE 'success' 
				END 
					WHEN sync_type = 'FTP' THEN
				CASE
						
						WHEN date_part( 'day', now() - sync_time :: TIMESTAMP ) > 2 THEN
						'error' ELSE 'success' 
					END ELSE 'error' 
				END sync_status,
				sync_time
		FROM
			estate_store 
		WHERE
			status = '100'
		""")
        rows = cursor.fetchall()
        total = len(rows)
        for row in rows:
            if row[2] == 'error':
                result.append(row)
        return total, result

    except Exception as e:
        error = str(e)
        print('连接pg查询失败: {}'.format(error))
    finally:
        # 关闭游标
        cursor.close()
        # 关闭数据库连接
        conn.close()


def format_msg(total, result):
    if not result:
        return ''
    title = 'DQ物业'

    head = """###{} {}\n>""".format(title, 'DQ')

    error_count = len(result)
    body = """> 物业状态为100的共{}笔数据, 超过时间限制同步共{}笔数据\n >""".format(total, error_count)
    for r in result:
        body += """> 门店:{}, 同步类型[{}], 最近一次同步时间为{} \n >""".format(r[0], r[1], r[3].strftime("%Y-%m-%d %H:%M:%S"))

    tail = """> #### {}发布 \n""".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    return head + body + tail


def send_ding_talk_msg(msg):
    url = 'https://oapi.dingtalk.com/robot/send?access_token=a8ef2ef0eac8fa45dbaa3abc2e64d1de0b8716fe07fd0e08a27606324a1b0c3e'
    headers = {
        "Content-Type": "application/json ;charset=utf-8 "
    }

    msg_dic = {
        "msgtype": "text",
        "text": {"content": msg},
        # "markdown": {
        #   "title": "监控",
        #   "text": msg
        # },
        "at": {
            "atMobiles": [
                "17610351121"
            ],
            "isAtAll": False
        }
    }
    res = requests.post(url, data=json.dumps(msg_dic), headers=headers)
    print(res.text)


if __name__ == '__main__':
    total, result = conn_pg_get_info()
    msg = format_msg(total, result)
    print(msg)
# if msg:
# 	send_ding_talk_msg(msg)
