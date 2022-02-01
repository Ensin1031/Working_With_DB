'''
Работа с данными, хранение данных, получение данных
'''

from sqlalchemy import create_engine, Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

engine = create_engine("postgresql+psycopg2://postgres:12345@127.0.0.1/learns", echo=True, future=True)
Base = declarative_base()


class Goods(Base):
    """Describe the products table"""
    __tablename__ = 'goods'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(250), nullable=False)
    price = Column('price', Integer, nullable=False)
    count = Column('count', Integer, nullable=False)


connection = engine.connect()
Base.metadata.create_all(engine)


def create_goods_from_list(list_of_goods):
    """A function that creates products from a list of products."""
    session = Session(bind=engine)

    for good in list_of_goods:
        good = Goods(
            name=good['name'],
            price=good['price'],
            count=good['count']
        )
        session.add(good)

    session.commit()


def delete_goods_from_list(list_of_goods):
    """Removing a product from the list by name."""
    session = Session(bind=engine)

    for good in list_of_goods:
        good = Goods(
            name=good['name'],
            price=good['price'],
            count=good['count']
        )
        session.add(good)

    session.commit()


def max_min_goods_on_the_list(list_of_goods):
    """A function that returns an object with max. and min. at the price."""
    session = Session(bind=engine)

    for good in list_of_goods:
        good = Goods(
            name=good['name'],
            price=good['price'],
            count=good['count']
        )
        session.add(good)

    session.commit()
