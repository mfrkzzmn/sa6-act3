# The given lists are:
lst_1 = [3, 4, 5, 8, 6]
lst_2 = [1, 2, 3, 4, 5]

# Finding intersection using by filter function and lambda function.
intersection = list(filter(lambda x: x in lst_1, lst_2))

print(intersection)
