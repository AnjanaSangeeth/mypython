from abc import ABC,abstractmethod
class Ide(ABC):
    @abstractmethod
    def debug (self):
        pass

class pycharm(Ide):
        def debug(self):
            print("pycharm debug method")

class Eclipse(Ide):
    def debug(self):
        print("eclipse debug method ")


pyc=pycharm()
pyc.debug()

    

    
    