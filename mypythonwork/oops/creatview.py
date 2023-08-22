from abc import ABC,abstractmethod

class Creatview(ABC):
    model:str
    template_name:str
    form_class:str

    def __init__(self,model,template_name,form_class):
        self.model=model
        self.template_name=template_name
        self.form_class=form_class
    @abstractmethod
    def create(self):
        pass
class EmployeeCreate(Creatview):
    def __init__(self, model, template_name, form_class):
        super().__init__(model, template_name, form_class)
    def create(self):
        print("funtionaliy for creating employee")

emp=EmployeeCreate("employee","employe.html","empform")
emp.create()