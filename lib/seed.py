from sqlalchemy import Column, Integer, String, ForeignKey,MetaData
from sqlalchemy.orm import relationship,session
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)


Base = declarative_base(metadata=metadata)

class Book(Base):
    __tablename__='books'
    id =Column(Integer(), primary_key=True)
    name=Column(String())
    price=Column(Integer())
    gonrer=Column(String)

class Library(Base):
    __tablename__='libraries'
    id =Column(Integer(),primary_key=True)
    name=Column(Integer())
    
