from pydantic import BaseModel

class Number(BaseModel):
    number: int | list
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

class Saying(BaseModel):
    id: int
    text: str
    author: str