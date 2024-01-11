from pydantic import BaseModel

class Number(BaseModel):
    number: int
    save: str

class Password(BaseModel):
    password: str

class Ask(BaseModel):
    prediction: str
    question: str

class Stat(BaseModel):
    count: int
    lucky: int

class Ticket(BaseModel):
    ticket: int
    lucky: bool
    stat: Stat

class Fact(BaseModel):
    id: int
    text: str

class Saying:
    id: int
    text: str
    author: str