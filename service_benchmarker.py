
import random
import requests
import time

config = {
    "base_url": "http://localhost/",
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


class ServiceBenchmarker(object):

    def __init__(self):
        self.tests = []
        self.responses = []
        self.base_url = "http://localhost:5000"
        self.request_per_second = 10
        self.test_lenght_in_seconds = 10
        self.start_time = None
        self.end_time = None

    def init_test(self):
        for x in range(self.request_per_second * self.test_lenght_in_seconds):
            self.tests.append({
                'method': methods[random.randint(0, len(methods) - 1)],
                'url': self.base_url + urls[random.randint(0, len(urls) - 1)],
                'header': headers[random.randint(0, len(headers) - 1)],
                'param': params[random.randint(0, len(params) - 1)]
                }
            )

    def run_all_tests(self):
        self.start_time = time.time()
        for t in self.tests:
            req_start_time = time.time()
            response = self.service_call(t)
            req_end_time = time.time()
            self.responses.append([response, req_end_time - req_start_time])
        self.end_time = time.time()
        
    def service_call(self, test_case):
        if test_case['method'] == 'GET':
            return requests.get(test_case['url'], headers=test_case['header'], params=test_case['param'])
        elif test_case['method'] == 'POST':
            return requests.post(test_case['url'], headers=test_case['header'], data=test_case['param'])
        elif test_case['method'] == 'PUT':
            return requests.put(test_case['url'], headers=test_case['header'], data=test_case['param'])
        elif test_case['method'] == 'DELETE':
            return requests.delete(test_case['url'], headers=test_case['header'], data=test_case['param'])
        elif test_case['method'] == 'PATCH':
            return requests.patch(test_case['url'], headers=test_case['header'], data=test_case['param'])
        elif test_case['method'] == 'OPTIONS':
            return requests.options(test_case['url'], headers=test_case['header'], data=test_case['param'])

    def report(self):
        # number of requests
        print('{} requests in {} seconds'.format(len(self.tests), self.end_time - self.start_time))
        
        # average request response time
        s = sum(t[1] for t in self.responses)
        print('average response time: {}'.format(s / len(self.tests)))

        # number of successful requests
        n = len([t[0] for t in self.responses if t[0].status_code in [200, 201, 204]])
        print('number of successful requests: {}'.format(n)) 
        
        # number failed requests
        n = len([t[0] for t in self.responses if t[0].status_code in [404, 500]])
        print('number of failed requests: {}'.format(n)) 
                
sb = ServiceBenchmarker()
sb.init_test()
sb.run_all_tests()
sb.report()
