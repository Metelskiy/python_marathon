def Cipher_Zeroes(N):
    z=0
    for i in range(len(N)):
        if(N[i]=="0" or N[i]=="6" or N[i]=="9"):
            z+=1
        elif(N[i]=="8"):
            z+=2
    if(z%2==0 and z>0):
        z-=1
    elif(z%2!=0):
        z+=1
    dv=format(z,"b")
    return dv
print(Cipher_Zeroes("588"))
