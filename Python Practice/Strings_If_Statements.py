course = "Calculus for Dummies"

print(course.upper()) # prints string in uppercase 
print(course)

# using find method to get index of a character or part of a string
print(course.find("u")) # gives us 4 for the first instance of u 
print(course.replace('C', 'A')) #replaces C with A in a new string, does not edit the current
# string, but returns a new string 

print('Calculus' in course) # using in allows us to ask if an element is in a variable
# returns true 


# and or not 
# both one not both

# If Statements

temperature = 35

if temperature > 30: 
    print("it's really hot")
elif temperature < 10:
    print("it's so cold")
else:
    print("super mid day")
    
    