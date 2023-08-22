f=open("C:\\Users\\anjna\\OneDrive\\Desktop\\mypythoncode\\mypythonwork\\users\\data.text","r")

users=[]

for line in f:

   text=line.rstrip("\n")
   name,followers,followings=text.split(",")
   print(name,followers,followings)

