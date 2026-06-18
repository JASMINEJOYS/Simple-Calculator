# class Student:
#     def greet(self):
#         print("Hello")
#     def student_details(self,name):
#         self.student_name=name
#         print(self.student_name)
# stu=Student()
# stu.greet()
# stu.student_details("Jas")


# class addition:
#     def add(self,a,b):
#         return a+b

# adding=addition()
# val=adding.add(5,6)
# print(val)


class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
           
    def add(self):
        return self.a+self.b
            
    def sub(self):
        return self.a-self.b
    
    def mul(self):
        return self.a*self.b
    def div(self):
        if self.b==0:
            print("Can't divisible by zero")
        else:
            return self.a/self.b
    
cal=Calculator(55,0)
print(cal.add())
print(cal.sub())
print(cal.mul())
print(cal.div())






    
