# liner 
# lst=[2,3,4,5,6,7,8]
"""
elem=8
is_found=False

for i in range(0,len(lst)):
    if(elem==lst[i]):
        is_found=True
        break
print("found"if is_found==True else "not found")
"""
# binary
lst=[2,3,4,5,6,7,8]

elem=2
is_found=False

low=0
upp=len(lst)-1
while(low<= upp):
    mid=(low+upp)//2
    if elem==lst[mid]:
        is_found=True
        break
    elif(elem > lst[mid]):
        low+=1
    elif(elem < lst[mid]):
        upp-=1
print("element found" if is_found==True else"element not found")



        