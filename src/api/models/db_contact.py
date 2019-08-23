from api.models.db import Base, Session
from sqlalchemy import Column, String, Integer
from api import util

class DBContact(Base):
    __tablename__ = 'contact'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    pwd = Column(String)
    phone = Column(String)

    def __init__(self, username, first_name, last_name, email, pwd, phone):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.pwd = pwd
        self.phone = phone

    @classmethod
    def from_dict(cls, dikt) -> 'Contact':
        return util.deserialize_model(dikt, cls)