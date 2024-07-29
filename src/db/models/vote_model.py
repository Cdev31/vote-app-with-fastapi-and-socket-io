from sqlalchemy import INTEGER, ForeignKey, TIMESTAMP, func, Column
from sqlalchemy.orm import relationship
from datetime import datetime
from ..libs import Base

class VotesModel ( Base ):
    __tablename__ = 'votes'

    id: Column = Column( 
        INTEGER,
        primary_key=True,
        autoincrement=True
    )
    
    surveyOptionId: Column = Column( "surveys_option_id", ForeignKey("surverys_option.id"), nullable=False )

    voteriId: Column = Column( "voter_id", ForeignKey("voters.id"), nullable=False )

    voteDate: Column[datetime] = Column( "vote_date", TIMESTAMP( timezone=True ), nullable=False, default=func.now())

    optionSurvey = relationship( "SurveyOptionModel", back_populates="" )
    
    voter = relationship( "VoterModel", back_populates="votes" )