# Write a function that adds two objects
def add_obj():
    pass

# Write a function that turns an integer into a string
def to_string():
    pass

# Write a function that turns a string into an integer
def to_int():
    pass

# Write a function that prints every other object in a list
# starting with the 0 index

# Once you write this function, modify it to also print the
# index of the element you are printing on the same line
def print_list():
    pass

# Write a function that detects if a string has an even number
# of characters
def is_even():
    pass

# Write a function that simply returns the string "bear"
# This function should accept an optional variable called big_bear
# big_bear should default to False, and if True is passed in
# it should return "BEAR"
def bear():
    pass

# Write a function that adds every other object in a list together
# Use the funtion you made previously to do this.

# Once you have made this function, modify it to accept
# a second argument, a keyword argument called 'even'
# this keyword argument should default to True and if
# set to False it should add the odd-numbered indices of
# the list
def list_sum():
    pass

# Write a function that accepts a list of integers. It should
# first check that every element of the list IS an integer, and
# if not it should raise a ValueError.
# Next, it should combine each even-indexed number with the next
# odd-indexed number into a single number in a new list
# (e.g. [1,2, 3, 4] becomes [12, 34]), for lists with an odd number
# of elements, it should put the final number unchanged into the new
# list.
# Next, it should sum these new numbers.
def combined_sum():
    pass


def main():
    # Run your functions here using these variables as input
    even_list = [6,5,3,7,9,0,2,3,6,0]
    odd_list = [4,3,1,2,5,0,9,6,2,9,0,8,4,5,7,4,5,6,8,7,4]
    even_string = "walupp"
    odd_string = "gromp"


if __name__ == "__main__":
    main()
