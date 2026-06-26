# Key:Value Pair 
# -- Keys are mutable, no duplicate keys are allowed
# -- values are unordered

info  = {
    "name" : "kailash",
    "cgpa" : 8.32,
    "subjects" : ["math","science", "coding", "dsa", "sql"],
    3.14 :"PI"
}
print(info)

info["cgpa"] = 9.32
print(info)

# -- dictionary methods

# dict.keys()
# dict.values()
# dict.get(key)
# dict.items()
# dict.update()

dict_keys= list(info.keys())        # method to print only keys 
print(dict_keys)

dict_values =list(info.values())   # method to print only values
print(dict_values)
print(info.values())
# --------------------------

print(info.get("name"))             # method to print value for a key here we can use info[key] but it will give error 
print(info.get("rollno"))           # for value that r not present, info.items() will return 'None' for missing values

print(info.items())
print(info.pop("name"))             # removes key value pairs from the the dict for the given key

info.update({                 # add new key:calue pair in the dictnry
    "city" : "Mumbai"
})
print(info)

