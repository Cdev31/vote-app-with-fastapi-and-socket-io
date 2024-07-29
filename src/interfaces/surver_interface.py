from abc import ABC, abstractmethod
from typing import List, Any


class SurverInterface( ABC ):

    @abstractmethod
    def find( self ):
        pass

    @abstractmethod
    def findOne( self, id: int ):
        pass

    @abstractmethod
    def create( self, data: Any ):
        pass

    @abstractmethod
    def update( self, data: Any, id: int ):
        pass
    
    @abstractmethod
    def deactivate( self, id: int ):
        pass

    @abstractmethod
    def activate ( self, id: int ):
        pass

    @abstractmethod
    def pause ( self, id: int ):
        pass

    @abstractmethod
    def delete ( self, id: int):
        pass