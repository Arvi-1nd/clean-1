names = {'name':'arvind','point':20}  #declaring key pairs
print(names['name'])   #key name
print(names['point'])   #key point

#looping through dictionaries
for name,value in names.items():
    print(f"{name} is having {value} points") 
