class Employee:
    def __init__(self,firstname, lastname, salary):
        self.firstname=firstname
        self.lastname=lastname
        self.salary=salary
    @classmethod
    def from_string(cls,arg):
        elem=arg.split("-")
        fistname=elem[0]
        lastname=elem[1]
        salary=int(elem[2])
        atr=cls(fistname,lastname,salary)
        return atr
emp1=Employee("Mary","Sue",60000)
emp2=Employee.from_string("John-Smith-55000")

print(emp1.firstname)
print(emp1.salary)
print(emp2.firstname)