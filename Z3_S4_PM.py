class Employee:
    spysok=[]
    def __init__(self,str,name="",lastname="", salary="",height="",nationality="",subordinates=[]):
        self.str=str
        self.salary=salary
        self.height=height
        self.nationality=nationality
        elem=str.split(" ")
        self.name=elem[0]
        self.lastname=elem[1]
        self.subordinates=subordinates
        Employee.spysok.append(subordinates)


john = Employee('John Doe')
print(john.lastname)
mary = Employee('Mary Major', salary=120000)
print(mary.salary)
richard = Employee('Richard Roe', salary=110000, height=178)
print(richard.salary)
print(richard.height)
giancarlo = Employee('Giancarlo Rossi', salary=115000, height=182, nationality='Italian')
print(giancarlo.name)
print(giancarlo.nationality)
peng = Employee('Peng Zhu', salary=500000, height=185, nationality='Chinese', subordinates=[i.lastname for i in (john, mary, richard, giancarlo)])
print(peng.subordinates)