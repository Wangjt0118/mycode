import pymongo
from dateutil.parser import parse
from datetime import datetime

mongo_client = pymongo.MongoClient(host='127.0.0.1', port=27071,)
db_name = mongo_client.saas_dq
# db_name = mongo_client.saas_dq_uat


start_date = '2021-08-01T00:00:00.000Z'
end_date = '2021-08-03T00:00:00.000Z'

query = {
	"store_us_id": 46269,
    "created": {
        "$gte": parse(start_date),
        "$lt": parse(end_date)
    	}
    }

# query = {
# 	'payload.body.order_unique_no': 'af17f761772047948e9ba760ff436a30'
# }

result = db_name.pos.find(query, {'_id': 1, 'created': 1, 'payload.body.order_unique_no': 1})

for i in result:
	print(i['_id'], i['created'], i['payload']['body']['order_unique_no'])
	created_time = str(i['created']).split(' ')[1].split(':')

	now_time = datetime(2021, 8, 11, int(created_time[0]), int(created_time[1]), int(created_time[2]))
	print(now_time)
	db_name.pos.update_one({
			'payload.body.order_unique_no': i['payload']['body']['order_unique_no']
		},
		{
			'$set': {'created': now_time}
		}
		)
