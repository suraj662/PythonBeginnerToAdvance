# Create class Student that takes 3 marks and has a method average().

class stud:
    def __init__ (self , name , listOfMarks):
        self.name = name
        self.listOfMarks = listOfMarks

    def average(self):
        sum=0
        for each in self.listOfMarks:
            sum = sum +each
        avg = sum/len(self.listOfMarks)
        print("the average",avg)


student3 = stud("suraj" , [20,30,80])
student3.average()