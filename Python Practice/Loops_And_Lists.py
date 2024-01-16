# while loops 
i = 1 
while i <= 5:
    print(i)
    i += 1


# For loops 
numberList = [1, 2, 3, 4]

#iterating over each item in an array/list
for item in numberList:
    print(item)

my_name = "Eithan"
# iterating over indexes of a string and printing element at that index
for i in range(len(my_name)):
    print(my_name[i])
    
#iterating over characters in a string
for my_char in my_name:
    print(my_char)

# range function
print(range(0, 5)) # gets numbers 0 to 4 

# Lists []

names = ["eithan", "Kav", "Andrew"]
print(names) # prints list of names

# getting individual elements of a list 
print(names[0]) #prints Eithan

# can use negative indexes within python
print(names[-1]) #prints Andrew

print(names[0:1]) # prints names from indexes 0 to 1 

# List Methods
numbers = [1, 2, 3, 4, 5, 6]
numbers.append(7) # appends 7 to the end of the list
print(numbers)
numbers.insert(-4, 1) #inserts number to list at an index (index, value)
print(numbers)
numbers.clear() # empties a list
print(numbers)

print(1 in numbers) # checking to see if the number is in the list 

# len function
print(len(numbers)) # len returns the number of elements in the list


# Tuples: immutable cannot change them once we create them ()
tuple_num = (1, 2 , 3)
tuple_num.count(1) # creturns number of occurrences of an element
tuple_num.count(2) # returns index of element in tuple

