import sqlite3
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class School(Base):
    __tablename__ = 'schools'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

class Class(Base):
    __tablename__ = 'classes'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    school_id = Column(Integer, ForeignKey('schools.id'), nullable=False)
    school = relationship('School', back_populates='classes')

School.classes = relationship('Class', order_by=Class.id, back_populates='school')

engine = create_engine('sqlite:///timetable.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()