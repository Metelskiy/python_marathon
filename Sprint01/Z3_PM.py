
def isPalindrome(str):
    revA = "".join(reversed(str))
    if(revA==str):
        return True
    else:
        count=0
        palin=0
        f=""
        for i in range(len(str)):
            l=[]
            count=0
            f=str[i]
            for z in range(len(str)):
                if(str[z]==f):
                    count+=1
            if(count==1):
                palin+=1
        if(count==3):
            return False
        elif(palin<=1):
            return True
        else:
            return False

b="abcab"
print(isPalindrome(b))

