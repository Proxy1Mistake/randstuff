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
    def number(cls, start: int, end: int, count: int = 1) -> int | Number:
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
        return _req.status_code if _req.status_code != 200 else Number(**_req.json())

    @classmethod
    def password(cls, length: int, numbers: int = 0, symbols: int = 0) -> int | Password:
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
        _data = {'length': length, 'numbers': numbers, 'symbols': symbols}
        _req = cls._session.post(url = cls._api('password'), headers = cls._headers, data = _data)
        return _req.status_code if _req.status_code != 200 else Password(**_req.json())

    @classmethod
    def ask(cls, question : str) -> int | Ask:
        """
        This function provides answers to questions

        :param question: the question you are asking
        :type question: :obj: `str`

        :return: the answer to the question in json format
        """
        _data = {'question': question}
        _req = cls._session.post(url = cls._api('ask'), headers = cls._headers, data = _data)
        return _req.status_code if _req.status_code != 200 else Ask(**_req.json()['ask'])

    @classmethod
    def ticket(cls) -> int | Ticket:
        _req = cls._session.post(url = cls._api('ticket'), headers = cls._headers)
        if _req.status_code != 200: return _req.status_code
        else:
            Stat(**_req.json()['stat'])
            return Ticket(**_req.json())

    @classmethod
    def fact(cls) -> int | Fact:
        _req = cls._session.post(url = cls._api('fact'), headers = cls._headers)
        return _req.status_code if _req.status_code != 200 else Fact(**_req.json()['fact'])

    @classmethod
    def saying(cls) -> int | Saying:
        _req = cls._session.post(url = cls._api('saying'), headers = cls._headers)
        return _req.status_code if _req.status_code != 200 else Saying(**_req.json())