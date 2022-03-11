def filterBible(scripture,book,chapter):
    #libr = ["01001001", "01001002", "01002001", "01002002", "01002003", "02001001", "02001002", "02001003"]
    zxc = []
    for i in range(len(scripture)):
        if(scripture[i].find(book)==False and scripture[i].find(chapter)==2):
                zxc.append(scripture[i])
    return zxc

#num1=input(str("Enter book"))
#num2=input(str("Enter chapter"))
num1="01"
num2="001"
johns = ["01001001", "01001002", "01002001", "01002002", "01002003", "02001001", "02001002", "02001003"]
print(filterBible(johns,num1,num2))