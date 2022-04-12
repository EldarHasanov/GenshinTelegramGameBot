# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
from dotenv import load_dotenv
#from sqlalchemy import create_engine
#import TelegramUser
#import ElementDatabase
#from sqlalchemy.orm import mapper
#from sqlalchemy import *
#from sqlalchemy.orm import create_session
#from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sq
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session

import DatabaseConnectClass

load_dotenv()

#Base = declarative_base()
#engine = create_engine(os.getenv("SQL_DATA_BASE"))
#metadata = MetaData(bind=engine)

Base = declarative_base()



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def show_query_result(rest):
    for element in rest:
        print(element.name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')



    engine = sq.create_engine(os.getenv("SQL_DATA_BASE"), echo=False)
    Base.metadata.create_all(engine)
    s = Session(engine)

    q = s.query(DatabaseConnectClass.Elements)
    num = q.count()
    print(num)
    print(q[num-1].beauty_name)
    for a_rec in q:
        print(a_rec.beauty_name)
    #connection = engine.connect()
    #metadata = sq.MetaData()

    #TelegramUser.insert().values(usr_name='@lol', element='geo')
    #rest = select(ElementDatabase.select())
    #show_query_result(rest)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
