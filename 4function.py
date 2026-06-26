# ---- Function defination----
def printer():
    print(hello)

def sum (a,b):
    s = a+b
    return s 

# ----Lambda func definiton------

avg = lambda a,b,c : (a+b+c)/3

# ------ Funtion Call-----
ans = sum(5,6)
print(ans)
print(avg(10,30,50))

# WAF to print factorial of 'n'-------

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact

inp = int(input("enter n: "))
print(factorial(inp))