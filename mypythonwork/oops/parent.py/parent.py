class Parent:

    def Vehicles(self):
        self.context=["passionpro","swift"]
        return self.context
    
class child(Parent):
    def Vehicles(self):
        self.context=super().Vehicles()
        self.context.append("hunter")
        return self.context




c=child()
print(c.Vehicles())
        