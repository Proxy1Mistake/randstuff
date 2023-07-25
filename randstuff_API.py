from requests import Session
from fake_useragent import FakeUserAgent
from .objects import *

class Data:
    _api = 'https://randstuff.ru/{}/generate/'.format
    _session = Session()
    _headers = {
        'user-agent': FakeUserAgent().random,
        'x-requested-with': 'XMLHttpRequest'
    }

class RandstuffApi(Data):
    @classmethod
    def number(cls, start: int, end: int, count: int = 1) -> int | ObjectNumber:
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
        _data = {'start': start, 'end': end, 'count': count}
        _req = cls._session.post(url = cls._api('number'), headers = cls._headers, data = _data)
        if _req.status_code != 200: return _req.status_code
        else: return ObjectNumber(data = _req.json()).object_number

    @classmethod
    def password(cls, length: int, numbers: int = 1, symbols: int = 1) -> int | ObjectPassword:
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
        if numbers: numbers = 2
        if symbols: symbols = 2
        _data = {'length': length, 'numbers': numbers, 'symbols': symbols}
        _req = cls._session.post(url = cls._api('password'), headers = cls._headers, data = _data)
        if _req.status_code != 200: return _req.status_code
        else: return ObjectPassword(data = _req.json()).object_password

    @classmethod
    def ask(cls, question : str) -> int | ObjectAsk:
        """
        This function provides answers to questions

        :param question: the question you are asking
        :type question: :obj: `str`

        :return: the answer to the question in json format
        """
        _data = {'question': question}
        _req = cls._session.post(url = cls._api('ask'), headers = cls._headers, data = _data)
        if _req.status_code != 200: return _req.status_code
        else: return ObjectAsk(data = _req.json()).object_ask

    @classmethod
    def ticket(cls) -> int | ObjectTicket:
        _req = cls._session.post(url = cls._api('ticket'), headers = cls._headers)
        if cls._req.status_code != 200: return cls._req.status_code
        else: return ObjectTicket(data = _req.json()).object_ticket

    @classmethod
    def fact(cls) -> int | ObjectFact:
        _req = cls._session.post(url = cls._api('fact'), headers = cls._headers)
        if _req.status_code != 200: return _req.status_code
        else: return ObjectFact(data = _req.json()).object_fact

    @classmethod
    def saying(cls) -> int | ObjectSaying:
        _req = cls._session.post(url = cls._api('saying'), headers = cls._headers)
        if _req.status_code != 200: return _req.status_code
        else: return ObjectSaying(data = _req.json()).object_saying