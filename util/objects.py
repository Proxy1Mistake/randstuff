class Number:
    def __init__(self, data):
        self.json = data
        self.number = None

    @property
    def Number(self):
        self.number = self.json['number']
        self.save = self.json['save']
        return self

class Password:
    def __init__(self, data):
        self.json = data
        self.password = None

    @property
    def Password(self):
        self.password = self.json['password']
        return self

class Ask:
    def __init__(self, data):
        self.json = data
        self.ask = None
        self.question = None

    @property
    def Ask(self):
        self.ask = self.json['ask']['prediction']
        self.question = self.json['ask']['question']
        return self

class Ticket:
    def __init__(self, data):
        self.json = data
        self.ticket = None
        self.lucky = None
        self.stat = None
        self.count = None
        self.countLucky = None

    @property
    def Ticket(self):
        self.ticket = self.json['ticket']
        self.lucky = self.json['lucky']
        self.stat = self.json['stat']
        self.count = self.json['stat']['count']
        self.countLucky = self.json['stat']['lucky']
        return self

class Fact:
    def __init__(self, data):
        self.json = data
        self.fact = None
        self.id = None
        self.text = None

    @property
    def Fact(self):
        self.fact = self.json['fact']
        self.id = self.json['fact']['id']
        self.text = self.json['fact']['text']
        return self

class Saying:
    def __init__(self, data):
        self.json = data
        self.saying = None
        self.author = None
        self.id = None
        self.text = None

    @property
    def Saying(self):
        self.saying = self.json['saying']
        self.author = self.json['saying']['author']
        self.id = self.json['saying']['id']
        self.text = self.json['saying']['text']
        return self