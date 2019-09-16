from flask import Flask
import random
import time

app = Flask(__name__)

response_codes = [200, 201, 204, 404, 500]

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def catch_all(path):
    ms = random.randint(25, 190) / 1000
    time.sleep(ms)
    return 'Hello', response_codes[random.randint(0, len(response_codes) - 1)]

app.run(debug=True)
