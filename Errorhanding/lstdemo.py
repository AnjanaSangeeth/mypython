lst=[10,20,30,40,50]

c6=["hari","ram","vijay","vinu","vipin","dibin"]

location=int(input("enter location to fetch value from list"))
try:
    print(lst[location])
except Exception as e:
    location=int(input("enter location to fetch value from list"))
    print(e.args)
    print(lst[location])
finally:
    print("dbcommit")
    print("file read")