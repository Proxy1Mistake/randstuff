class ObjectNumber:
    def __init__(self, data):
        self.json = data
        self.number = None
        self.save = None

    @property
    def object_number(self):
        try:
            self.number = self.json['number']
            self.save = self.json['save']
        except(KeyError, TypeError): pass
        return self

class ObjectPassword:
    def __init__(self, data):
        self.json = data
        self.password = None

    @property
    def object_password(self):
        try:
            self.password = self.json['password']
        except(KeyError, TypeError): pass
        return self

class ObjectAsk:
    def __init__(self, data):
        self.json = data
        self.ask = None
        self.question = None

    @property
    def object_ask(self):
        try: self.ask = self.json['ask']['prediction']
        except(KeyError, TypeError): pass
        try: self.question = self.json['ask']['question']
        except(KeyError, TypeError): pass
        return self

class ObjectTicket:
    def __init__(self, data):
        self.json = data
        self.ticket = None
        self.lucky = None
        self.stat = None
        self.count = None
        self.countLucky = None

    @property
    def object_ticket(self):
        try:
            self.ticket = self.json['ticket']
            self.lucky = self.json['lucky']
            self.stat = self.json['stat']
            self.count = self.json['stat']['count']
            self.countLucky = self.json['stat']['lucky']
        except(KeyError, TypeError): pass
        return self

class ObjectFact:
    def __init__(self, data):
        self.json = data
        self.fact = None
        self.id = None
        self.text = None

    @property
    def object_fact(self):
        try:
            self.fact = self.json['fact']
            self.id = self.json['fact']['id']
            self.text = self.json['fact']['text']
        except(KeyError, TypeError): pass
        return self

class ObjectSaying:
    def __init__(self, data):
        self.json = data
        self.saying = None
        self.author = None
        self.id = None
        self.text = None

    @property
    def object_saying(self):
        try:
            self.saying = self.json['saying']
            self.author = self.json['saying']['author']
            self.id = self.json['saying']['id']
            self.text = self.json['saying']['text']
        except(KeyError, TypeError): pass
        return self