class books:
    name=str
    author=str
    price=int
    pages=int

    def __init__(self,**kwargs):
           self.name=kwargs.get("name")
           self.author=kwargs.get("author")
           self.price=kwargs.get("price")
           self.pages=kwargs.get("pages")

    def __str__(self):
        return self.name


obj=books(name="randamoozam",author="mt",price=560,pages=500)
print(obj)



# __init__()=> constuctor
# __str__()=>string




