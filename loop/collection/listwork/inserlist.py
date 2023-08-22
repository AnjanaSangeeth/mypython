# lst=[2,3,4,5]
# lst.append(6)
# print(lst)



# # insert-to add to a particular position in a list 
# lst.insert(0,1) #listName. insert (postion of list , value to be added to list)
# print(lst)


#creating empty list
# emplst=[]
# print(emplst)

#get size of list from user , and get each of a list  from user,than add to list

# length=int(input ("enter size of list:"))
# for i in range(length):
#     num=int(input(f"enter {i}th position element:"))
#     emplst.append(num)
# print(emplst)


#a)create an empty list and access all the element from the user 
#b)add new element to 2nd position of list .which should the maxmum od list added by 10

# emplst=[]


# length=int(input ("enter size of list:"))
# for i in range(length):
#     num=int(input(f"enter {i}th position element:"))
    
#     emplst.append(num)
# maxim=max(emplst)
# emplst.insert(2,maxim+10)
# print(emplst)



#create a  list of student name,then check for a particular name in the list give by 
#the user if name is present then change that name to "Anamika" if that particular
#name is not presnt add "amal" to list position

# student_name=["laya","anjana","adheen","helen"]
# print(student_name)
# users=input("enter the name that u want to be search")
# for s in student_name:
#     if()
    
student_name=[]
lenght=int(input("enter the size of list:"))
for i in range(lenght):
    name=input(f"enter{i}th name:")
    student_name.append(name)
    #print(student_name)
ch_name=input("enter a name:")
for s in range(lenght):
    if(student_name[s]==ch_name):
        student_name[s]="Anamika"
        break
    elif(s==lenght-1):
        student_name.insert(1,"amal")
    print(student_name)
    


    #assignment : if duplicate values are present how the value will be changed if a match found or not
#i/p=>[a,b,c] =>ch_name=a,o/p=>[anamika,b,c,anamika]





    

