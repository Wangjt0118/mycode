import redis
import time

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0

ERROR_THRESHOLD = 3
ERROR_WINDOW = 5 * 60  # 5 minutes

def log_error(redis_client, error_timestamp):
    redis_client.zadd('error_log', {error_timestamp: time.time()})

def get_error_log(redis_client):
    error_log = redis_client.zrange('error_log', 0, -1, withscores=True)
    return error_log

def remove_old_errors(redis_client):
    old_timestamp = time.time() - ERROR_WINDOW
    redis_client.zremrangebyscore('error_log', 0, old_timestamp)

def check_errors(redis_client):
    remove_old_errors(redis_client)
    error_log = get_error_log(redis_client)

    if len(error_log) < ERROR_THRESHOLD:
        return False

    error_count = 0
    first_error_timestamp = None
    for timestamp, score in error_log:
        if first_error_timestamp is None:
            first_error_timestamp = timestamp

        error_count += 1
        if error_count >= ERROR_THRESHOLD:
            time_range = (first_error_timestamp, timestamp)
            return time_range

        if time.time() - timestamp > ERROR_WINDOW:
            error_count = 0
            first_error_timestamp = None

    return False


if __name__ == '__main__':
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
    log_error(r, 'error1')
    log_error(r, 'error2')
    log_error(r, 'error3')
    log_error(r, 'error4')
    log_error(r, 'error5')

    time_range = check_errors(r)
    if time_range:
        print(f'Continuous errors found: {time_range}')
        # do something to handle continuous errors
    else:
        print('No continuous errors found')
