def check_odd_even (number):
    try:
        if(number%2==0):
            return "Entered number is even"
        elif(number%2!=0):
            return "Entered number is odd"
    except:
        return "You entered not a number."
print(check_odd_even("12"))