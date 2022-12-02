from requests import Session
from fake_useragent import UserAgent
from random import choice

class randStuff:
    def __init__(self):
        self.api = 'https://randstuff.ru/{}/generate/'.format
        self.session = Session()
        self.headers = {
            'user-agent': UserAgent().random,
            'x-requested-with': 'XMLHttpRequest'
        }

    def number(self, start: int, end: int, count: int):
        data = {'start': start, 'end': end, 'count': count}
        req = self.session.post(url=self.api('number'), headers = self.headers, data = data)
        return req.json()['number']

print(randStuff().number(start=0, end=100, count=1))