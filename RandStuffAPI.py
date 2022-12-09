from .util import headers, objects
from requests import Session

class randStuffAPI:
    def __init__(self, proxies : dict = None):
        self.api = 'https://randstuff.ru/{}/generate/'.format
        self.session = Session()
        self.headers = headers.Headers().headers
        self.proxies = proxies

    def number(self, start: int, end: int, count: int):
        data = {'start': start, 'end': end, 'count': count}
        req = self.session.post(url = self.api('number'), headers = self.headers, data = data, proxies = self.proxies)
        return objects.Number(req.json()).Number

    #numbers: 1 - on, 2 - off
    #Symbols: 1 - on, 2 - off
    def password(self, length: int, numbers: int, symbols: int):
        data = {'length': length, 'numbers': numbers, 'symbols': symbols}
        req = self.session.post(url = self.api('password'), headers = self.headers, data = data, proxies = self.proxies)
        return objects.Password(req.json()).Password

    def ask(self, question : str):
        data = {'question': question}
        req = self.session.post(url = self.api('ask'), headers = self.headers, data = data, proxies = self.proxies)
        return objects.Ask(req.json()).Ask

    def ticket(self):
        req = self.session.post(url = self.api('ticket'), headers = self.headers, proxies = self.proxies)
        return objects.Ticket(req.json()).Ticket

    def fact(self):
        req = self.session.post(url = self.api('fact'), headers = self.headers, proxies = self.proxies)
        return objects.Fact(req.json()).Fact

    def saying(self):
        req = self.session.post(url = self.api('saying'), headers = self.headers, proxies = self.proxies)
        return objects.Saying(req.json()).Saying
