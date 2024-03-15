# The given string are: 
strings = ['Math', 'Computer', 'Biology', 'Chemistry', 'Physics']

# Sorting the list by lambda function.
Sorting_list = sorted(strings, key = lambda x: (len(x), x))

# outcomes: 
print(Sorting_list)