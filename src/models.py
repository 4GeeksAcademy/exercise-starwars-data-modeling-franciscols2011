import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, unique=True, nullable=False)
    suscription = Column(DateTime)


class Profile(Base):

    __tablename__ = 'profile'

    profileId = Column(Integer, primary_key=True)
    firstName = Column(String(30), nullable=False)
    lastName = Column(String(30), nullable=False)
    nick = Column(String(30), nullable=False)
    userId = Column(Integer, ForeignKey('user.id'), unique=True)

    users = relationship(User)

    def to_dict(self):
        return {}


class Characters (Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(250))
    homeworld = Column(String(250))
    url = Column(String(250))


class Planets(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(Integer)
    population = Column(Integer)
    climate = Column(String(250))
    terrain = Column(String(250))
    surface_water = Column(Integer)
    url = Column(String(250))


class FavoritesCharacters (Base):
    __tablename__ = 'favoritesCharacters'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    characters_id = Column(Integer, ForeignKey('characters.id'))
    users = relationship(User)
    characters = relationship(Characters)


class FavortiesPlanets (Base):
    __tablename__ = 'favortiesPlanets'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    users = relationship(User)
    planets = relationship(Planets)
    
# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
