from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def drew(self):
        pass

class rectangle(Shape):
    def drew(self):
        print("drawing rectangle")

class square(Shape):
    def drew(self):
        print("drawing square")


rec=rectangle()
rec.drew()

squ=square()
squ.drew()