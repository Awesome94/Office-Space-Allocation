import os
import sys
import sqlalchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


class PersonModel(Base):
    """create a person table"""
    __tablename__ = 'person'
    person_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String, nullable=False)
    designation = Column(Boolean, nullable=False)
    # wants_accomodation = Column(Boolean, unique=True, default=False)

class RoomModel(Base):
    """Create the rooms table
    """
    __tablename__ = 'room'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), nullable=False)
    rtype = Column(String(32), nullable=False)
    # capacity = Column(Integer, nullable=False)


class OfficeSpaces(Base):
    """Store office allocations"""
    __tablename__ = "office_spaces"
    id = Column(Integer, primary_key=True, autoincrement=True)
    room_name = Column(String(32), nullable=False)
    members = Column(String(250))


class LivingSpaces(Base):
    """Store living space allocations"""
    __tablename__ = "living_spaces"
    id = Column(Integer, primary_key=True, autoincrement=True)
    room_name = Column(String(32), nullable=False)
    members = Column(String(250))


class DatabaseCreator(object):
    """creating database connection to object"""
    def __init__(self, db_name=None):
        self.db_name = db_name + '.sqlite'
        self.engine = create_engine('sqlite:///' + self.db_name)
        Base.metadata.create_all(self.engine)
        session_maker = sessionmaker(bind=self.engine)
        self.session = session_maker()
