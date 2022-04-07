# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
from dotenv import load_dotenv
#from sqlalchemy import create_engine
import User
import Element
from sqlalchemy.orm import mapper

from sqlalchemy import *
from sqlalchemy.orm import create_session
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

Base = declarative_base()
engine = create_engine(os.getenv("SQL_DATA_BASE"))
metadata = MetaData(bind=engine)



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def show_query_result(rest):
    for element in rest:
        print(element.name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    session = create_session(bind=engine)

    session.begin()
    session.add(User(usr_name='Derek', element='geo'))
    session.commit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
