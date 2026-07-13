class Student:
    school = "xyz college"

    def __init__ (self , name):
        self.name = name   #current attribute
        print(self.name)
        # print("whenever a new object created I am automatically called")
        # print(self)




#init called automatically
student1 = Student("suraj")
student2 = Student("pawan")

