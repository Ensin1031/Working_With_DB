# coding=UTF-8
from sqlalchemy import create_engine, Integer, String, Column, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
import json
import logging

logger = logging.getLogger('main.' + __name__)

# engine = create_engine("postgresql+psycopg2://postgres:12345@127.0.0.1/learns", echo=True, future=True, max_overflow=20)
engine = create_engine("postgresql+psycopg2://postgres:12345@127.0.0.1/learns", future=True, max_overflow=20)
Base = declarative_base()


class Goods(Base):
    """Describe the products table"""
    __tablename__ = 'goods'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(250), nullable=False)
    price = Column('price', Integer, nullable=False)
    count = Column('count', Integer, nullable=False)

    logger.info(f'Table "{__tablename__}" is create')


connection = engine.connect()
Base.metadata.create_all(engine)


def create_good_from_list(list_of_good):
    """A function that creates products from a list."""
    session = Session(bind=engine)

    query = session.query(Goods).filter(Goods.name == list_of_good[0]).all()
    if query:
        logger.info(f'Error. An entry with the name "{list_of_good[0]}" already exists in the database.')
    else:
        session.add(Goods(name=list_of_good[0], price=list_of_good[1], count=list_of_good[2]))
        session.commit()
        logger.info(f'An entry named "{list_of_good[0]}" has been added in DB.')


def delete_goods_from_list(name_to_delete):
    """Function to remove a product from the list by name."""
    session = Session(bind=engine)

    query_for_delete = session.query(Goods).filter(Goods.name == name_to_delete).all()
    if query_for_delete:
        for row in query_for_delete:
            session.delete(row)
        session.commit()
        logger.info(f'Product named "{name_to_delete}" was successfully removed from the list')
        return True
    else:
        logger.info(f'Error. product named "{name_to_delete}" is not listed.')
        return False


def max_min_goods_on_the_list():
    """A function that returns an object with max. and min. at the price."""
    session = Session(bind=engine)

    max_quary_value = session.query(func.max(Goods.price)).all()
    max_quary = session.query(Goods).filter(Goods.price == max_quary_value[0][0]).all()
    min_quary_value = session.query(func.min(Goods.price)).all()
    min_quary = session.query(Goods).filter(Goods.price == min_quary_value[0][0]).all()

    result_list = []

    for row in max_quary:
        result_list.append([row.name, row.price, row.count])

    for row in min_quary:
        result_list.append([row.name, row.price, row.count])

    logger.info("Была запущена функция мах-мин")
    return [max_quary_value[0][0], min_quary_value[0][0], result_list]


def show_the_entire_list():
    """Function to show the entire list."""
    session = Session(bind=engine)

    all_quary = session.query(Goods).all()

    result_list = []

    for row in all_quary:
        result_list.append([row.name, row.price, row.count])

    logger.debug("Show to the entire list.")
    return result_list


def clean_db():
    """Function of complete cleaning of the database"""
    for row in show_the_entire_list():
        delete_goods_from_list(row[0])
    logger.debug('function "clean_db" worked')


def db_in_json(file_way):
    """Function of outputting data from the database to a file in JSON format"""
    data_json = show_the_entire_list()
    pre_json_list = []
    for row in data_json:
        pre_json_list.append({
            "Good":
                {
                    "name": row[0],
                    "price": row[1],
                    "count": row[2]
                }
        })
    with open(file_way, 'w', encoding="utf-8") as file:
        json.dump(pre_json_list, file, indent=4, ensure_ascii=False)
    logger.debug('function db_in_json worked')
