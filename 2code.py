# Avg of 2 nums 
# a = int(input("Enter 1st no : "))
# b = int(input("Enter 2nd no : "))

# avg = (a+b) / 2

# print(avg)
# -----------------------------------
# a = input("What is your name ?")
# b = input('what is uour age ?')

# print('Hello' ,a ,', you are ',b,' years old !')

# -----------------------------------
# a = int(input("Enter 1st no : "))
# b = int(input("Enter 2nd no : "))

# print('sum : ', a+b )
# print('Diff : ', a-b )
# print('quotient  : ', a/b )
# print('product : ', a*b )

# -------------------------------------
# Ask for inputs
# num1 = int(input("Enter first integer: "))
# num2 = int(input("Enter second integer: "))
# num3 = float(input("Enter a float: "))

# # Convert all to floats
# val1 = float(num1)
# val2 = float(num2)
# val3 = float(num3)

# # Calculate and print average
# average = (val1 + val2 + val3) / 3
# print(f"The average is: {average}")

# # ----------------------------

# string = input('Enter a num :')

# num1 = int(string)
# num2 = float(string)
# num3 = string

# print(f"integer {num1}" ,type(num1))
# print(f"integer {num2}" ,type(num2))
# print(f"integer {num3}" ,type(num3))

# # ------------------------------------

# num1 = int(input("Enter first integer: "))
# num2 = int(input("Enter second integer: "))

# temp = num1
# num1 = num2
# num2 = temp

# print(num1, num2)
# ---------------------------------------

num = float(input("Enter a decimal number: "))

# Extract the integer part
integer_part = int(num)

# Extract the fractional part
fractional_part = num - integer_part

# Print the results
print(f"integer part: {integer_part}")
print(f"fractional part: {round(fractional_part, 2)}")