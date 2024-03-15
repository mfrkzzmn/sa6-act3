def find_maximum(number, compare):
    # Initialize the max number with first element. 
    max_num = number[0]
    # Using loop 
    for i in number[1:]:
        max_num = compare(max_num, i)
    return max_num

# Lambda function to compare two number for max number. 
compare_highest = lambda x, y: x if x > y else y

# Given the list number are: 
lst = [5, 6, 7, 8, 9, 1, 2]

Finding_max_num = find_maximum(lst, compare_highest)

# outcomes:
print(f"The maximum number in the list is  {Finding_max_num}")