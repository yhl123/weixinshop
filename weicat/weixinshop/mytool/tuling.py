import json
import requests

url = 'http://www.tuling123.com/openapi/api'


def get_text(text):
    data = {
        'key': '',
        'info': text,
        'userid': 2
    }
    res = requests.post(url, data)
    return json.loads(res.content.decode('utf8')).get('text')
