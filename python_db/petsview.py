from get_connection import db_connect
class PetsView:

    def connect (sefl):
        db=db_connect (password="Password@123",database="animal")
        return db
    
    def grt (sefl):
        db=sefl.connect()
        cursor=db.cursor()
        query="select * from pest"
        cursor.execute(query)
        qs=cursor.fetchall()
        return qs
    
pv=PetsView()
print(pv.get())
    
