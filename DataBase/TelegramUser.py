from sqlalchemy import *
from sqlalchemy.orm import create_session
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv
load_dotenv()
Base = declarative_base()
#engine = create_engine(os.getenv("SQL_DATA_BASE"))
#metadata = MetaData(bind=engine)

class TelegramUser(table):
    __tablename__ = 'telegram_users'

    usr_name = Column(String, primary_key=True)
    element = Column(ForeignKey('ElementDatabase.name'))


