from abc import ABC, abstractmethod
from typing import Any

class VoterInterface( ABC ):

    @abstractmethod
    def find( self ):
        pass

    @abstractmethod
    def findById( self, id: int ):
        pass

    @abstractmethod
    def findOne( self, term: Any ):
        pass