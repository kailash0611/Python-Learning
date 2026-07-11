# -----------SET------------
# -- Contains all unique elements no duplicates
# -- Mutable and unordered 
# -- empty set create a dictionary - bcoz {} are used in both set and dictionary 
# -- to create an empty set the syntax is diff 


s = {1,2,2,2,3,3,4,5,} 

print(s)
print(type(s))
print(len(s))

empty_set = {}                  # this acts as a dictionary
print(type(empty_set))

emptySet = set()                # this is how u define empty set 
print(type(emptySet))
print(emptySet)

# --------Set Methods-----------

# s.add()
# s.remove()
# s.clear()
# s.pop()
# s1.union(s2)
# s1.intersection(s2)

s.add(6)                # takes only one arg at a time
print(s)

s.remove(3)             # this also takes only one 
print(s)

s.clear()               # clears whole set and makes it empty 
print(s)

s1 = {3,3,4,2,3,4}  
s2 = {2,5,6,4,7,8}

print(s1.union(s2))             # gives all elments from s1 and s2 
print(s1.intersection(s2))      # gives common elements from s1 and s2

print(s1.pop())
print(s1.pop())
print(s2.pop())