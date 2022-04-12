from sqlalchemy import *
from sqlalchemy.orm import create_session
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv
load_dotenv()

Base = declarative_base()


#engine = create_engine(os.getenv("SQL_DATA_BASE"))

#metadata = MetaData(bind=engine)

class Elements(Base):
    __tablename__ = 'elements'


    name = Column(String, primary_key=True)
    beauty_name = Column(String)
    pic_element_png = Column(String)

class TelegramUser(Base):
    __tablename__ = 'users'

    #def __init__(self, name, element):
    #    self.usr_name = Column(String, primary_key=True,values=name)
    #    self.element = Column(ForeignKey('elements.name'),values=element)

    usr_name = Column(String, primary_key=True)
    element = Column(ForeignKey('elements.name'))