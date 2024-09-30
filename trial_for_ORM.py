from sqlalchemy import Table, Column, Integer, Numeric, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import CheckConstraint

Base = declarative_base()


class Cookie(Base):
    __tablename__ = 'cookies'
    __table_args__ = (CheckConstraint('unit_cost >= 0.00', 
                                       name = 'unit_cost_positive'))

    cookie_id = Column(Integer(), primary_key = True)
    cookie_name = Column(String(50), index = True)
    cookie_recipe_url = Column(String(225))
    cookie_sku = Column(String(55))
    quantity = Column(Integer())
    unit_cost = Column(Numeric(12, 2)) # Here the two arguments mean it is 11 digits long and has two decimal places.


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer(), primary_key = True)
    username = Column(String(15), nullable = False, unique = True)
    email_address = Column(String(255), nullable = True)
    phone = Column(String(25), nullable = False) # nullable = False 即此column不可为空
    password = Column(String(25), nullable = False)
    created_on = Column(DateTime(), default = datetime.now) # default 即默认设此栏为填表时的时间
    updated_on = Column(DateTime(), default = datetime.now, onupdate = datetime.now) # onupdate 即可在表更新时记录当时时间。虽然两个都是datetime.now但表现会不同。
