arr=[2,3,4]
op=[]
#step 1 = find total sum of array
#step 2 sub each element with total = sum
arr_total=sum(arr)
# print(arr_total)
for i in arr:
    # print(arr_total-i)
    res=arr_total-i
    op.append(res)
print(op)