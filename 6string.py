word1 = "i love "
word2 = "python"

#length--
print(len(word1))

# concat--
print(word1+ word2)

# indexing--
print(word1[2])

# word[2] = 'h' this is not possible since it is immutable 

for i in range(len(word1)):
    print(word1[i])

# slicing
word =  " I love Apna College"
a= word2[1:4]
print(a)
print(word[3:len(word)])
print(word[-7:-1])

# --------------formating--------------------

# ---- > normal formating 
b = 10 
c = 20 
e = 40
d = b+c+e 
print ("sum of {} and {}is{}".format(b,c,d))


# ---- > indexbased formating
print ("sum of {2} {0} and {1} is{3}".format(b,c,e,d))

# -----> USING f String 

print(f"Summ of {b} {c} and {e} = {d}")


# ================ List =============
marks = [34,45,664,64]

print(len(marks))
print(marks[4])

# --- All string concepts work with list slicing, indexing etc 