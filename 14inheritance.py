# - Inheritance
# Types of Inheritance 
# 1. Single Inheritance
# 2. Multilevel Inhetitance 
# 3. Multiple Inheritance
# 4. 
class Employee:
    start_time = "10am"
    end_time = "6pm"   # protected : will be accessible into subclass

    def __init__(self):
        pass

class Teacher(Employee):        #syntax to inherit parent  -single inheritance
    def __init__(self,name,subject):
        self.name = name
        self.subject = subject


class AdminStaff(Employee):
    def __init__(self, name, role):
        self.name = name
        self.role = role

class Accountant(AdminStaff):   #multiple inheritance
    def __init__(self,salary):
        self.salary = salary

e1 = Teacher("Kailash" , "Maths")
e2 = AdminStaff("deep" , "admin")

print(e1.name, e1.subject, e1.start_time, e1.end_time)
# print(e2.name,e2.role, e2.start_time, e2._end_time)

# ---------------------------------------------------------------
class Emp:
    def __init__(self,salary):
        self.salary = salary


class Student: 
    def __init__(self,gpa):
        self.gpa = gpa

class TA(Emp,Student):
    def __init__(self, salary, gpa ,name):
        # 2 ways of accessing parent class attributes
        super().__init__(salary)    # using super - here we don't have to use self
        Student.__init__(self, gpa) # using className - here we have to use self as a parameter
        self.name = name 

ta1 = TA(45000, 4.32, "kailash")
print(ta1.gpa, ta1.name, ta1.salary)