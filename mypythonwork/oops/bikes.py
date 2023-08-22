from abc import ABC,abstractmethod
from typing import Any
class Bilke(ABC):
    name:str
    modle:str
    fule_type:str
    def __init__(self,name,modle,fule_type):

        self.name=name
        self.modle=modle
        self.fule_type=fule_type

    @abstractmethod
    def start(self):
        pass

class Hunter(Bilke):
    def __init__(self,name,modle,fule_type):
        super().__init__(name,modle,fule_type)
    def start(self):
        print(f"{self.name}starting modle{self.modle} fule{self.fule_type}")

hun=Hunter("hunter dapper grer","2023","petrol")
hun.start()