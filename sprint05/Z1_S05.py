def check_positive(number):
    try:
        if(float(number)>0):
            return (f"You input positive number: {float(number)}")
        elif(float(number)<0):
            return (f"You input negative number: {float(number)}. Try again.")
    except:
         return ("Error type: ValueError!")



print(check_positive("abs"))
print(check_positive("45"))
print(check_positive("-235"))