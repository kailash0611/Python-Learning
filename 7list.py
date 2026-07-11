# list is in [values]
# tuple is in (values)
# dictionary is in {key:value}
# set is in {values} 

marks = [34,45,664,64]

print(len(marks))
print(marks[3])

# --- All string concepts work with list slicing, indexing, etc 

# fuction in list
l = ["apple", "mango", 'banana', "lemon"]
l.append("val") 
print(l)

l.insert(2, "chicoo")
print(l)

l.sort()
print(l)

l.reverse()
print(l)
# -------------------------------------------------------

nums = [32, 43, 23, 54 ,25 ,23]
nums.sort()
print(nums)
# ------------------------------

num = [32, 43, 23, 54 ,25 ,23]

target = 23 
idx = 0

for val in num:
    if(val == target):
        print(idx)
        break
    idx += 1
      
# ------------------Tuple----------------
# -- Tuple are similar to list but they are immutable 

tup = (21,32,43,54,65,43,32,76) #type will be tuple
tup1 = (10)     # will conside it as int only
tup2 = (10,)    # , is need to make it conside it as tuple


print(type(tup))
print(len(tup))
print(type(tup1))
print(type(tup2))

# ---------------------------------

print(tup[3])       # can acces using index value 
#tup[3] = 43         #cant modify using indexes 
print (tup[2:4])    # slicing is possible just like sting excluding 2 and including 4 

# -- tuple methods--

print(tup.index(32))       #gives indes of first occurence of value 
print(tup.count(43))       #gives indes of first occurence of value
