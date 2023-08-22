import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="animal"
)


cursor=db.cursor()
query="""insert  into pets(age,gender,breed,location,price) valuse(2,"male","breed1","ekm",25000)"""

cursor.execute(query)
db.commit()       #save changes
