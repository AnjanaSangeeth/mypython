import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="animal"
)


cursor=db.cursor()
# creat a table buffalo
# id age wegiht bread image
query= """create table pets(id int not null primary key,
age int not null,
gender varchar(200) not null,
breed varchar(200) not null,
loaction varchar(200) not null,
price int not null)
"""

cursor.execute(query)