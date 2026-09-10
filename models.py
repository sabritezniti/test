from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Class(Base):
    __tablename__ = 'classes'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=False)
    teacher = relationship('Teacher', back_populates='classes')

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    classes = relationship('Class', back_populates='teacher')

class Room(Base):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    classes = relationship('Class', back_populates='room')

Class.room = relationship('Room', back_populates='classes')

engine = create_engine('sqlite:///timetable.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()