'''
Работа с данными, хранение данных, получение данных
'''

from sqlalchemy import create_engine, Integer, String, Column, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from body.list_goods import list_goods


def primary_data():
    """The function creates a file with initial data and enters them into the database."""
    with open('body/goods.info', 'w', encoding='utf-8') as goods:
        for line in list_goods:
            goods.write(line)
    with open('body/goods.info', 'r', encoding='utf-8') as goods:
        for line in goods.readlines():
            list_good = line.split(':')
            list_good[1], list_good[2] = int(list_good[1]), int(list_good[2])
            create_good_from_list(list_good)


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


def create_good_from_list(list_of_good):
    """A function that creates products from a list."""
    session = Session(bind=engine)

    session.add(Goods(name=list_of_good[0], price=list_of_good[1], count=list_of_good[2]))
    session.commit()


def delete_goods_from_list(name_to_delete):
    """Function to remove a product from the list by name."""
    session = Session(bind=engine)
    try:
        query_for_delete = session.query(Goods).filter(Goods.name == name_to_delete).all()
    except Exception as e_:
        return f'INFO. Error. product named "{name_to_delete}" is not listed.\n{e_}'
    else:
        for i in query_for_delete:
            session.delete(i)
        session.commit()
        return f'INFO. product named "{name_to_delete}" was successfully removed from the list'


def max_min_goods_on_the_list():
    """A function that returns an object with max. and min. at the price."""
    session = Session(bind=engine)

    max_quary = session.query(func.max(Goods.price)).all()
    min_quary = session.query(func.min(Goods.price)).all()

    return f'price min.: {min_quary[0][0]}, price max.: {max_quary[0][0]}'


def show_the_entire_list():
    """Function to show the entire list."""
    session = Session(bind=engine)

    all_quary = session.query(Goods).all()
    return all_quary
