import concurrent.futures
import time
import random
import requests
from test_input import config, fake_data

def do_work(item):

    # faking real world request distribution
    time.sleep(random.randint(0, 1000) / 1000)
    
    if item['method'] == 'GET':
        return requests.get(item['url'], headers=item['header'], params=item['param'])
    elif item['method'] == 'POST':
        return requests.post(item['url'], headers=item['header'], data=item['param'])
    elif item['method'] == 'PUT':
        return requests.put(item['url'], headers=item['header'], data=item['param'])
    elif item['method'] == 'DELETE':
        return requests.delete(item['url'], headers=item['header'], data=item['param'])
    elif item['method'] == 'PATCH':
        return requests.patch(item['url'], headers=item['header'], data=item['param'])
    elif item['method'] == 'OPTIONS':
        return requests.options(item['url'], headers=item['header'], data=item['param'])


with concurrent.futures.ThreadPoolExecutor(max_workers=config['requests_per_second']) as executor:
        executor.map(do_work, fake_data())
