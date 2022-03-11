
def kthTerm(n,k):
    a=[0]
    for i in range(0,10):
        #print(i)
        for z in range(len(a)):
            x=(n**i)+a[z]
            a.append(x)
            # print("list===",a)
            if(z==5):
                break
    a.remove(0)
    print(a)
    for i in range(len(a)):
        if((i+1)==k):
            return a[i]
            break

print(kthTerm(30, 100))