def findPermutation(n, p, q):
    r = []
    for i in range(n):
        for c in range(n):
            if(q[i]==p[c]):
                c+=1
                r.append(c)
    return r



n=3
z=[3,1,2]
x=[2,1,3]
print(findPermutation(n,z,x))