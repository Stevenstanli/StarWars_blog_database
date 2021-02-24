import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Planets(Base):
    __tablename__ = 'planets'
    # Notice that each column is also a normal Python instance attribute. 
    id = Column(Integer, primary_key=True)
    Name = Column(String(50), nullable=False)
    Diameter = Column(String(50), nullable=False)
    Rotation_period = Column(String(50), nullable=False)
    Orbital_period = Column(String(50), nullable=False)
    Gravity = Column(String(50), nullable=False)
    Population = Column(String(50), nullable=False)
    Climate = Column(String(50), nullable=False)
    Terrain = Column(String(50), nullable=False)
    Surface_water = Column(String(50), nullable=False)
    Created = Column(String(50), nullable=False)
    Edited = Column(String(50), nullable=False)
    Url = Column(String(250), nullable=False)
    Description = Column(String(250), nullable=False)

class People(Base):
    __tablename__ = 'people'
    # Notice that each column is also a normal Python instance attribute. 
    id = Column(Integer, primary_key=True)
    Name = Column(String(50), nullable=False)
    Height = Column(String(50), nullable=False)
    Mass = Column(String(50), nullable=False)
    Hair_color = Column(String(50), nullable=False)
    Skin_color = Column(String(50), nullable=False)
    Eye_color = Column(String(50), nullable=False)
    Birth_year = Column(String(50), nullable=False)
    Gender = Column(String(50), nullable=False)
    Created = Column(String(50), nullable=False)
    Edited = Column(String(50), nullable=False)
    Id_Homeworld = Column(Integer, ForeignKey('planets.Id'), nullable=False)
    Url = Column(String(250), nullable=False)
    Description = Column(String(250), nullable=False)
    PeopleId = relationship('planets')

class Species(Base):
    __tablename__ = 'species'
    # Notice that each column is also a normal Python instance attribute. 
    id = Column(Integer, primary_key=True)
    Name = Column(String(50), nullable=False)
    Classification = Column(String(50), nullable=False)
    Designation = Column(String(50), nullable=False)
    Average_height = Column(String(50), nullable=False)
    Average_lifespan = Column(String(50), nullable=False)
    Hair_colors = Column(String(50), nullable=False)
    Skin_colors = Column(String(50), nullable=False)
    Eye_colors = Column(String(50), nullable=False)
    Id_Homeworld = Column(Integer, ForeignKey('planets.Id'), nullable=False)
    Language = Column(String(50), nullable=False)
    Id_People = Column(Integer, ForeignKey('people.Id'), nullable=False)
    Created = Column(String(50), nullable=False)
    Edited = Column(String(50), nullable=False)
    Url = Column(String(250), nullable=False)
    Description = Column(String(250), nullable=False)
    PeopleId = relationship('people')
    PeopleId = relationship('planets')

class Starships(Base):
    __tablename__ = 'starships'
    # Notice that each column is also a normal Python instance attribute. 
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    starship_class = Column(String(50), nullable=False)
    manufacturer = Column(String(50), nullable=False)
    cost_in_credits = Column(String(50), nullable=False)
    length = Column(String(50), nullable=False)
    crew = Column(String(50), nullable=False)
    passengers = Column(String(50), nullable=False)
    max_atmosphering_speed = Column(String(50), nullable=False)
    hyperdrive_rating = Column(String(50), nullable=False)
    MGLT = Column(String(50), nullable=False)
    cargo_capacity = Column(String(50), nullable=False)
    consumables = Column(String(50), nullable=False)
    created = Column(String(50), nullable=False)
    edited = Column(String(50), nullable=False)
    url = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Notice that each column is also a normal Python instance attribute. 
    id = Column(Integer, primary_key=True)
    Name = Column(String(50), nullable=False)
    Model = Column(String(50), nullable=False)
    Vehicle_class = Column(String(50), nullable=False)
    Manufacturer = Column(String(50), nullable=False)
    Cost_in_credits = Column(String(50), nullable=False)
    Length = Column(String(50), nullable=False)
    Crew = Column(String(50), nullable=False)
    Passengers = Column(String(50), nullable=False)
    Max_atmosphering_speed = Column(String(50), nullable=False)
    Cargo_capacity = Column(String(50), nullable=False)
    Consumables = Column(String(50), nullable=False)
    Created = Column(String(50), nullable=False)
    Edited = Column(String(50), nullable=False)
    Url = Column(String(250), nullable=False)
    Description = Column(String(250), nullable=False)

class Films(Base):
    __tablename__ = 'films'
    # Notice that each column is also a normal Python instance attribute. 
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    created = Column(String(100), nullable=False)
    edited = Column(String(100), nullable=False)
    producer = Column(String(100), nullable=False)
    episode_id = Column(Integer, nullable=False)
    director = Column(String(100), nullable=False)
    release_date = Column(String(250), nullable=False)
    opening_crawl = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    Id_People = Column(Integer, ForeignKey('people.Id'), nullable=False)
    Id_Planets = Column(Integer, ForeignKey('planets.Id'), nullable=False)
    Id_starships = Column(Integer, ForeignKey('starships.Id'), nullable=False)
    Id_vehicles = Column(Integer, ForeignKey('vehicles.Id'), nullable=False)
    Id_species = Column(Integer, ForeignKey('species.Id'), nullable=False)
    PeopleId = relationship('people')
    PeopleId = relationship('planets')
    PeopleId = relationship('starships')
    PeopleId = relationship('vehicles')
    PeopleId = relationship('species')

class User(Base):
    __tablename__ = 'user'
    # Notice that each column is also a normal Python instance attribute. 
    id = Column(Integer, primary_key=True)
    Name = Column(String(50), unique = True, nullable=False)
    Last_Name = Column(String(50), nullable=False)
    UserName = Column(String(50), nullable=False)
    Id_Login = Column(Integer, ForeignKey('login.Id'), nullable=False)
    LoginId = relationship('login')

class Login(Base):
    __tablename__ = 'login'
    # Notice that each column is also a normal Python instance attribute. 
    id = Column(Integer, primary_key=True)
    Password = Column(String(500), nullable=False)
    Pepeer = Column(String(500), nullable=False)
    salt = Column(String(500), nullable=False)

class Type (Base):
    __tablename__ = 'type'
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    Id_favorite = Column(Integer, nullable=False)
    UserId = relationship('user')
    PeopleId = relationship('people')
    PlanetsId = relationship('planets')
    StarshipsId = relationship('starships')
    VehiclesId = relationship('vehicles')
    SpeciesId = relationship('species')

class Favorites(Base):
    __tablename__ = 'favorites'
    # Notice that each column is also a normal Python instance attribute. 
    id = Column(Integer, primary_key=True)
    UserName = Column(Integer, ForeignKey('User.Id'), nullable=False)
    Id_Type = Column(Integer, ForeignKey('User.Id'), nullable=False)
    PeopleId = relationship('user')
    TypeId = relationship('type')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram1.png')