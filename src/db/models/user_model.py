from sqlalchemy import INTEGER, VARCHAR, TIMESTAMP, Column, CHAR, func
from sqlalchemy.orm import relationship
from datetime import datetime
from ..libs import Base

class UserModel( Base ):
    __tablename__ = 'users'

    id: Column = Column( 
        INTEGER,
        primary_key=True,
        autoincrement=True
     )

    name: Column[str] = Column( "name", VARCHAR(30), nullable=False )

    email: Column[str] = Column( "email", VARCHAR(255), nullable=False, unique=True)

    password: Column[str] = Column( "Password", VARCHAR(255), nullable=False, unique=True )

    phoneNumber: Column[str] = Column( "phone_number", VARCHAR(12), nullable=False )

    dui: Column[str] = Column( "dui", CHAR(12), nullable=False, unique=True )

    createdAt: Column[datetime] = Column( "created_at", TIMESTAMP( timezone=True ), nullable=False, default=func.now() )

    surveys = relationship( "SurveyModel", back_populates="user" )