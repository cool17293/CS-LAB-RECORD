sample_string = "Hello,world!"

#  capitalize() - Capitalizes the first character of the string
print("capitalize():", sample_string.capitalize())

#  upper() - Converts all characters to uppercase
print("upper():", sample_string.upper())

#  lower() - Converts all characters to lowercase
print("lower():", sample_string.lower())


# replace() - Replaces a substring within the string
print("replace('Hello', 'Hi'):", sample_string.replace("Hello", "Hi"))


#  count() - Counts occurrences of a substring
print("count('e'):", sample_string.count("e"))

# split() - Splits the string into a list
print("split():", sample_string.split())

#  join() - Joins elements of a list into a single string
words = ["Python", "is", "awesome"]
print("join():", " ".join(words))


# startswith() - Checks if the string starts with a specific substring
print("startswith('Hello'):", sample_string.strip().startswith("Hello"))

# 16. endswith() - Checks if the string ends with a specific substring
print("endswith('ChatGPT!'):", sample_string.strip().endswith("ChatGPT!"))

# 17. len() - Returns the length of the string
print("len():", len(sample_string))