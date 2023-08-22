#swapping
 
num1=10
num2=20
print(f"value b4 swapping num1={num1} num2={num2}") #num1=10 , #num2=20

# logic 1
# temp=num1
# num1=num2
# num2=temp

#  logic 2
# (num1,num2)=(num2,num1)

# logic 3
num1=num1+num2
num2=num1-num2
num1=num2-num1


print(f"value after swapping num1={num1} num2={num2}") #num1=20 , #num2=10