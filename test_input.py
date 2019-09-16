import random


config = {
    "base_url": "http://localhost:5000",
    "file_name": "output.log",
    "requests_per_second": 100,
    "test_lenght_in_seconds": 600
}

urls = [
    '/admin/',
    '/auth/login',
    '/auth/logout',
    '/ping',
    '/admin/users/',
    '/admin/users/12',
    '/admin/users/12/addresses'
]

headers = [
    {'Content-Type': 'text/html' , 'charset': 'UTF-8'},
    {'Content-Type': 'application/json'},
    {'Content-Type': 'application/x-www-form-urlencoded'}
]

params = [
    {},
    {'username': 'joe', 'password': 'mypass'},
    {'username': 'joe', 'password': 'mypass', 'email': 'joe@boo.com'},
    {'message': 'hi there', 'to': 'goo@lala.hu', 'subject': 'Welcome'}
]

methods = ['POST', 'GET', 'DELETE', 'PUT', 'PATCH', 'OPTIONS']

def fake_data():
    return ({'method': methods[random.randint(0, len(methods) - 1)],
          'url': config['base_url'] + urls[random.randint(0, len(urls) - 1)],
          'header': headers[random.randint(0, len(headers) - 1)],
          'param': params[random.randint(0, len(params) - 1)]
        } for x in range(config['requests_per_second'] * config['test_lenght_in_seconds']))
