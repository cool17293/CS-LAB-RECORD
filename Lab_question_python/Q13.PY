

my_list = []

# Adding elements to the list
my_list.append(5)
my_list.append(10)
my_list.append(15)
print("List after adding elements:", my_list)

# Inserting an element at a specific index
my_list.insert(1, 7)  # Insert 7 at index 1
print("List after inserting 7 at index 1:", my_list)

# Accessing elements
print("First element:", my_list[0])
print("Last element:", my_list[-1])

# Removing an element by value
my_list.remove(10)  # Remove the first occurrence of 10
print("List after removing 10:", my_list)

# Popping an element from a specific index
popped_element = my_list.pop(1)  # Pop the element at index 1
print("List after popping element at index 1:", my_list)
print("Popped element:", popped_element)

# Sorting the list
my_list.sort()
print("List after sorting:", my_list)

# Reversing the list
my_list.reverse()
print("List after reversing:", my_list)

# Getting the length of the list
print("Length of the list:", len(my_list))

# Clearing all elements from the list
my_list.clear()
print("List after clearing all elements:", my_list)