from requests import Session

from .objects import *

class Randstuff:
    _url = 'https://randstuff.ru/{}/generate/'.format

    @classmethod
    def __request_post(cls, url: str, data: dict = None):
        session = Session()

        headers = {
            "user-agent": "Mozilla/5.0 (Linux; U; Linux x86_64; en-US) AppleWebKit/600.8 (KHTML, like Gecko) Chrome/47.0.1452.400 Safari/536",
            'x-requested-with': 'XMLHttpRequest'
        }

        req = session.post(url = url,
                          data = data,
                          headers = headers)

        if req.status_code == 200: return req

        print(f'Error >>> {req.status_code} {req.text}')
        exit()

    @classmethod
    def number(cls, start: int, end: int, count: int = 1) -> Number:
        """
        This function is designed to generate a random number
        :param start: the number of the character that number begins with
        :type start: :obj: `int`

        :param end: the number of the last character number
        :type end: :obj: `int`

        :param count: number of generations
        :type count: :obj: `int`
        :return: Number
        """
        data = {
            'count': count,
            'start': start,
            'end': end
        }

        return Number(
            **cls.__request_post(url = cls._url('number'),
                                data = data).json()
        )

    @classmethod
    def password(cls, length: int, numbers: int = 0, symbols: int = 0) -> Password:
        """
        This function is for password

        :param length: password length
        :type length: :obj: `int`

        :param numbers: True - on, None - False - off. adds numbers to the password
        :type numbers: :obj: `bool`

        :param symbols: True - on, None - False - off. adds special characters
        :type symbols: :obj: `bool`

        :return: Password
        """
        data = {
            'length': length,
            'numbers': numbers,
            'symbols': symbols
        }

        return Password(
            **cls.__request_post(url = cls._url('password'),
                                data = data).json()
        )

    @classmethod
    def ask(cls, question : str) -> Ask:
        """
        This function provides answers to questions

        :param question: the question you are asking
        :type question: :obj: `str`

        :return: Ask
        """
        data = {
            'question': question
        }

        return Ask(
            **cls.__request_post(url = cls._url('ask'),
                                data = data).json()['ask']
        )

    @classmethod
    def ticket(cls) -> Ticket:
        """
        This function is designed to receive a ticket. Both lucky and unlucky ones fall out.

        :return: Ticket
        """
        req = cls.__request_post(url = cls._url('ticket'))
        Stat(**req.json()['stat'])
        return Ticket(**req.json())

    @classmethod
    def fact(cls) -> Fact:
        """
        Get an inquisitive fact.

        :return: Fact
        """
        return Fact(
            **cls.__request_post(url = cls._url('fact')
                                ).json()['fact']
        )

    @classmethod
    def saying(cls) -> Saying:
        """
        All sorts of wise phrases.

        :return: Saying
        """
        return Saying(
            **cls.__request_post(url = cls._url('saying')
                                ).json()['saying']
        )