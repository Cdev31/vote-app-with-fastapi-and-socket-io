from abc import ABC, abstractmethod
from typing import Any

class AuthInterface( ABC ):

    @abstractmethod
    def user_register( self, data: Any ):
        pass

    @abstractmethod
    def voter_register( self, data: Any ):
        pass

    @abstractmethod
    def voter_login( self, data: Any ):
        pass

    @abstractmethod
    def user_login( self, data: Any ):
        pass