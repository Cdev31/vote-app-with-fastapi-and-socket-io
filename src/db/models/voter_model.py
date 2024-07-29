from sqlalchemy import INTEGER, VARCHAR, CHAR, TIMESTAMP, func, Column
from sqlalchemy.orm import relationship
from datetime import datetime
from ..libs import Base

class VoterModel ( Base ):
    __tablename__ = 'voters'

    id: Column = Column( 
        INTEGER,
        primary_key=True,
        autoincrement=True
    )

    name: Column[str] = Column( "name", VARCHAR(30), nullable=False )

    email: Column[str] = Column( "email", VARCHAR(255), nullable=False, unique=True )

    dui: Column[str] = Column( "dui", CHAR(12), nullable=False, unique=True )

    createdAt: Column[datetime] = Column( "created_at", TIMESTAMP( timezone=True ), nullable=False, default=func.now())

    votes = relationship( "VotesModel", back_populates="voter" )