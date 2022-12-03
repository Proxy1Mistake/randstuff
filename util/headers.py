from fake_useragent import UserAgent

class Headers:
    def __init__(self):
        self.headers = {
            'user-agent': UserAgent().random,
            'x-requested-with': 'XMLHttpRequest'
        }