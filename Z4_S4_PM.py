class Testpaper:
    def __init__(self,subject, markscheme,pass_mark):
        self.subject=subject
        self.markscheme=markscheme
        self.pass_mark=pass_mark

class Student:
    def __init__(self,tests_taken="No tests taken"):
        self.tests_taken=tests_taken
    def take_test(self,paper, s_marks):
        if(isinstance(self.tests_taken, dict)==False):
            self.tests_taken={}
        counter=0
        for i in s_marks:
            for c in paper.markscheme:
                if(i==c):
                    counter+=1
        #is test taken:
        res=(counter*100)/len(paper.markscheme)
        if(res>=int(paper.pass_mark[:-1])):
            self.tests_taken[paper.subject]=f"Passed! ({round(res)}%)"
        else:
            self.tests_taken[paper.subject] = f"Failed! ({round(res)}%)"
        return  self.tests_taken

paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
paper2 = Testpaper("Chemistry", ["1C", "2C", "3D", "4A"], "75%")
paper3 = Testpaper("Computing", ["1D", "2C", "3C", "4B", "5D", "6C", "7A"], "75%")

student1 = Student()
student2 = Student()
print(student1.tests_taken) #"No tests taken"
student1.take_test(paper1, ["1A", "2D", "3D", "4A", "5A"])
print(student1.tests_taken) #{"Maths" : "Passed! (80%)"}

student2.take_test(paper2, ["1C", "2D", "3A", "4C"])
student2.take_test(paper3, ["1A", "2C", "3A", "4C", "5D", "6C", "7B"])
print(student2.tests_taken) #{"Chemistry" : "Failed! (25%)", "Computing" : "Failed! (43%)"}

