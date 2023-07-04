from requests import Session
from fake_useragent import FakeUserAgent
from .objects import *

class randstuff_API:
    def __init__(self, proxies : dict = None):
        self.api = 'https://randstuff.ru/{}/generate/'.format
        self.session = Session()
        self.headers = {
            'user-agent': FakeUserAgent().random,
            'x-requested-with': 'XMLHttpRequest'
        }
        self.proxies = proxies

    def number(self, start: int, end : int, count: int = None):
        """
        This function is designed to generate a random number
        :param start: the number of the character that number begins with
        :type start: :obj: `int`

        :param end: the number of the last character number
        :type end: :obj: `int`

        :param count: number of generations
        :type count: :obj: `int`
        :return: number in json format
        """
        if count == None: count = 1
        else: count = count
        data = {'start': start, 'end': end, 'count': count}
        req = self.session.post(url = self.api('number'), headers = self.headers, data = data, proxies = self.proxies)
        if req.status_code != 200: return req.status_code
        else: return obj_number(data = req.json()).obj_number

    def password(self, length: int, numbers: bool = False, symbols: bool = False):
        """
        This function is for password

        :param length: password length
        :type length: :obj: `int`

        :param numbers: True - on, None - False - off. adds numbers to the password
        :type numbers: :obj: `bool`

        :param symbols: True - on, None - False - off. adds special characters
        :type symbols: :obj: `bool`

        :return: password in json format
        """
        if numbers == False: numbers = 2
        else: numbers = 1
        if symbols == False: symbols = 2
        else: symbols = 1
        data = {'length': length, 'numbers': numbers, 'symbols': symbols}
        req = self.session.post(url = self.api('password'), headers = self.headers, data = data, proxies = self.proxies)
        if req.status_code != 200: return  req.status_code
        else: return obj_password(data = req.json()).obj_password

    def ask(self, question : str):
        """
        This function provides answers to questions

        :param question: the question you are asking
        :type question: :obj: `str`

        :return: the answer to the question in json format
        """
        data = {'question': question}
        req = self.session.post(url = self.api('ask'), headers = self.headers, data = data, proxies = self.proxies)
        if req.status_code != 200: return req.status_code
        else: return obj_ask(data = req.json()).obj_ask

    def ticket(self):
        req = self.session.post(url = self.api('ticket'), headers = self.headers, proxies = self.proxies)
        if req.status_code != 200: return req.status_code
        else: return obj_ticket(data = req.json()).obj_ticket

    def fact(self):
        req = self.session.post(url = self.api('fact'), headers = self.headers, proxies = self.proxies)
        if req.status_code != 200: return req.status_code
        else: return obj_fact(data = req.json()).obj_fact

    def saying(self):
        req = self.session.post(url = self.api('saying'), headers = self.headers, proxies = self.proxies)
        if req.status_code != 200: return req.status_code
        else: return obj_saying(data = req.json()).obj_saying