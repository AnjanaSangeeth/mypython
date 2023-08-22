# lst=[1,3,4,6,]
# find least +ve missing from given list

lst=[1,2,4,5,8]

for i in range(0,len(lst)):
    elem1=lst[i]
    elem2=lst[i+1]

    if(elem2-elem1!=1):
        print(elem1+1,"is missing")
        break
    else:
        elem1=lst[i]
        elem2=lst[i+1]
        if(elem2-elem1!=1):
            print(elem1+1,"is missing")
            break

# lst=[2,3,4,4,5,5,6,7]
# find duplicate element from list

# lst=[2,3,4,4,5,5,6,7]

# for i in range(0,len(lst)):
