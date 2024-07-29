from sqlalchemy import Column, INTEGER, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship
from ..libs import Base

class SurveyOptionModel( Base ):
    __tablename__ = 'surveys_option'

    id: Column = Column(
        INTEGER,
        primary_key=True,
        autoincrement=True
    )

    title: Column[str] = Column( "title", VARCHAR(50), nullable=False )

    surveyId: Column = Column( "survey_id", ForeignKey("surveys.id"), nullable=False )
    
    survey = relationship( "SurveyModel" , back_populates="options" )

    votes = relationship( "VotesModel", back_populates="optionSurvey" )
    
    