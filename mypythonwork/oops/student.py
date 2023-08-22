class student:
    rolno:int
    name:str
    course:str

    def __init__(self,**kwargs):
        self.rolno=kwargs.get("rolno")
        self.name=kwargs.get("name")
        self.course=kwargs.get("course")

    def get_student(self):
        print(self.rolno,self.name,self.course)

    
obj=student(rolno=1000,name="vijay",course="django")
obj.get_student()
