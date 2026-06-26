def calc_salary():
    salary = int(input("Enter your salary...?"))

    if (salary < 30000):
        tax_rate = salary*5/100
    elif(salary >= 30000 and salary <= 70000):
        tax_rate = salary*15/100
    else:
        tax_rate = salary*25/100

    print(f"Tax Rate is : {tax_rate}")

def print1_100d_by3():
    for i in  range(1,100+1):
        if(i%3 == 0 and i%5 == 0):
            print(i)

# print1_100d_by3()

