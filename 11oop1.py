# # -------Object Oriented Programming-------
# Class :
# - blueprint of an object 

# creating a class

class Student:
    # constructors

    # this is a default constructor,
    # def __init__(self): 
    # we cannnot have multiple constructor in python like java and C++
    # even if there are multiple ctr then the last one gets considered

        

    def __init__(self, subject, college, year):    # 'self' is like 'this'
        self.subject = subject
        self.college = college
        self.year = year

s1 = Student("Mathematics", "Harvard", 2026)
s2 = Student("Python", "Rait", 2023)

print(s1.subject, s1.college, s1.year)
print(s2.subject, s2.college, s2.year)

# --------- Object :
# - Instance of Object

# ---------- Attributes 
# there are 2 types of attributes 
# 1. class attributes - belong to class - common for all object 
# 2. instance attributes - belong to object - unique for for different object

class Classmate:
    college_name = "Dy" # class attribute

    def __init__(self, name, cgpa):  #instance attribute
        self.name = name                   
        self.cgpa = cgpa

c1 = Classmate("Kailash", 8.32)
c2 = Classmate("Aayush", 7.5)

print(Classmate.college_name, c1.name, c1.cgpa)
print(Classmate.college_name, c2.name, c2.cgpa)
