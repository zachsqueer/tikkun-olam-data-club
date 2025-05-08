"""
Create a copy of this file and test.csv and place them in your folder in the repository.
When you write a function, be sure to use type annotations.
"""

test_1 = "4357.120439.54362.0149.7389"

# Excercise 1: Extract the integers from between the dots in the string above using
# only the .split() string method.

# Exercise 2: Repeat the above, but this time write it as a function without using
# the .split() method. You may only use string methods and slicing, and the return
# value must be the same as the split method above.

test_2 = "lorem | ipsum | dolor | sit | amet"

# Exercise 3: Extend the function you wrote in exercise 2 to accept an optional
# second argument to use as the delimiter, and use it to turn the string above
# into a list

# Exercise 4: Write a new function that accepts two lists as arguments and returns
# a dictionary whose keys are the first list and whose values are from the second
# list. Within the function, check if the values passed as keys are strings, and
# if they are, title case them. Pass in test_2 as the keys and test_1 as the values
# to this function.

# Exercise 5: Read in the file test.csv in the same folder as this one and use your
# function to turn it into a list of rows, and then use it again to turn it into
# a list of lists where each value is one word. Hint: the invisible newline character
# separating each row is represented by \n
