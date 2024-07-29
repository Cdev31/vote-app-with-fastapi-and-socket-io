from sqlalchemy import Column, INTEGER, TIME, DATE, TIMESTAMP, func, VARCHAR, ForeignKey, TEXT
from sqlalchemy.dialects.mysql import ENUM, TINYINT
from sqlalchemy.orm import relationship
from datetime import time, date
from ..libs import Base

class SurveyModel( Base ):
    __tablename__ = 'surveys'

    id: Column = Column(
        INTEGER,
        primary_key=True,
        autoincrement=True
    )

    title: Column[str] = Column( "title", VARCHAR(100), nullable=False )

    startHour: Column[time] = Column( "start_hour", TIME( timezone=True ), nullable=False )

    startDate: Column[date] = Column( "start_date", DATE, nullable=False )

    endHour: Column[time] = Column( "end_hour", TIME( timezone=True ), nullable=False )

    endDate: Column[date] = Column( "end_date", DATE, nullable=False )

    status: Column[str] = Column( "status", ENUM(["Active", "Ending", "Paused", 'Inactive'], ), nullable=False )

    description: Column[str] = Column( "description", TEXT, nullable=False )

    active: Column[int] = Column( "active", TINYINT , nullable=False, default=0 )

    userId: Column = Column( "user_id", INTEGER, ForeignKey("users.id"), nullable=False )

    user = relationship( "UserModel", back_populates="surveys" )

    options = relationship( "SurveyOption", back_populates="survey" )