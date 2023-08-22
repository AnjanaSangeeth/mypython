data=[
        {"id":1,"username":"jhon","email":"jhon@gmail.com","password":"password@123"},
        {"id":2,"username":"hari","email":"hari@gmail.com","password":"password@123"},
        {"id":3,"username":"ravi","email":"ravi@gmail.com","password":"password@123"},
        {"id":4,"username":"vijay","email":"vijay@gmail.com","password":"password@123"},
        {"id":5,"username":"vinu","email":"vinu@gmail.com","password":"password@123"},
        {"id":6,"username":"tom","email":"tom@gmail.com","password":"password@123"},
    ]




def retrieve (self,id):
    return[u for u in self.data if u.get("id")==id]

def destroy(self,id):
    obj=[u for ]

def put(self,id,value):
    obj=[u for u in self.data if u.get("id")==id][0]


    pos=self.data.index(obj)
    self.data[pos]=value[0]

obj=Users()
print(obj.retrieve (5))
payload={"id":5,"username":"vinu","email":"vinus@gmail.com","password":"password@123"},

print(obj.retrieve(5))

