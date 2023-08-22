# try except finally
# try:
# except:
# finally:


num1=int(input("enter valuue for number1"))
num2=int(input("enter value for num2"))
try:
    res=num1/num2
    print("result",res)

except Exception as e:
    print("exception occured")

print("db commit1")
print("db commit2")
