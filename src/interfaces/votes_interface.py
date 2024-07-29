from abc import ABC, abstractmethod
from typing import Any

class VotesInterface( ABC ):

    @abstractmethod
    def vote( self, optionId: int ):
        pass

    @abstractmethod
    def deleteVote ( self, id: int ):
        pass

    @abstractmethod
    def updateOption( self, data: Any, optionId: int ):
        pass

    @abstractmethod
    def deleteOption( self, id: int ):
        pass