def order(a):
    q=0
    b=0
    issorted=0
    for i in range(len(a)-1):
        #print(a[i])
        if(a[i]<a[i+1]):
            q+=1
        elif(a[i]>a[i+1]):
            b+=1
    if (q==len(a)-1):
        return "ascending"
    elif(b==len(a)-1):
        return "descending"
    else:
        return "not sorted"


z=[1,2,3,4,5,6]
b=[4,3,2]
c=[5,3,6,4,5,6,7,8]
print(order(b))