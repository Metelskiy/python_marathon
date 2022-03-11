def studying_hours(a):
    z=0
    stric=[]
    for i in range(len(a)-1):
        if(a[i]<a[i+1] or a[i]==a[i+1]):
            z+=1
            stric.append(z + 1)
        elif(a[i]>a[i+1]):
                #stric.append(z+1)
                z=0
    x=max(stric)
    return x
a=[2,2,1,3,4,1]
print(studying_hours(a))