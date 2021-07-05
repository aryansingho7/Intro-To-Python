## Sort list of dictionaries by values in Python – Using itemgetter

# Using itemgetter
from operator import itemgetter

lis = [{ "name" : "Nandini", "age" : 20}, 
{ "name" : "Manjeet", "age" : 20 },
{ "name" : "Nikhil" , "age" : 19 }]

# using sorted and itemgetter to print list sorted by age 
print(sorted(lis, key=itemgetter('age')))

# using sorted and itemgetter to print list sorted by both age and name
print(sorted(lis, key=itemgetter('age', 'name')))

# using sorted and itemgetter to print list sorted by age in descending order
print(sorted(lis, key=itemgetter('age'), reverse = True))


# Using lambda function
lis = [{ "name" : "Nandini", "age" : 20},
{ "name" : "Manjeet", "age" : 20 },
{ "name" : "Nikhil" , "age" : 19 }]

print(sorted(lis, key = lambda i : i['age']))
print("\r")
print(sorted(lis, key = lambda i: (i['age'],i['name'])))
print("\r")
print(sorted(lis, key = lambda i: i['age'], reverse = True))
