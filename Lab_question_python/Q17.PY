
my_tuple = (5, 10, 15, 10, 20)
print("Original tuple:", my_tuple)

# Accessing elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Slicing a tuple
print("Elements from index 1 to 3:", my_tuple[1:4])

# Counting occurrences of an element
count_10 = my_tuple.count(10)
print("Number of times 10 appears:", count_10)

# Finding the index of an element
index_15 = my_tuple.index(15)
print("Index of 15:", index_15)

# Checking if an element exists in the tuple
if 20 in my_tuple:
    print("20 is in the tuple")
else:
    print("20 is not in the tuple")

# Concatenating two tuples
another_tuple = (25, 30)
concatenated_tuple = my_tuple + another_tuple
print("Concatenated tuple:", concatenated_tuple)

# Finding the length of the tuple
print("Length of the tuple:", len(my_tuple))