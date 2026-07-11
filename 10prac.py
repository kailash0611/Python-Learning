info = [
    ("Alice","Math"),
    ("Kailash","English"),
    ("Bob","Science"),
    ("Alice","History"),
    ("Charlie","Science"),
    ("Duke","Math"),
]
print(info)

# q1. list all the unique course
courses_set = set()

for tup in info:
    courses_set.add(tup[1])

print(courses_set)

# q2. list students enrolled in English

for name, course in info:
    if course == "English":
        print(course)

# q3. Crete dictionary (student,set of courses)

dict ={}
for key, value in info:
    if(dict.get(key)== None):
        dict.update({key:set()})
        dict[key].add(value)
    else:
        dict[key].add(value)

print(dict)
