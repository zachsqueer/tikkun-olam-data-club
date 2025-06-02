"""
Built in functions in Python
==================================================================
Python has numerous functions built into the language. Remember that
everything in python is an object, i.e. an instance of a class,
and that classes have methods (functions that act on an individual
instance of an object) and attributes (variables associated with an
individual instance object). Most of these built in functions act on
the methods and attributes of the object to give you data about them.
For instance, the len() method simply accesses an attribute called
__len__ within the object and returns it. It's up to the object
to make sure that the value of __len__ is always correct, the built
in function just reads it how the object has determined it. If an
object doesn't implement a __len__ attribute, then Python will throw
an exception, so it's up to you to know and reference what objects
implement it.

A few important built-in functions are:

len(): The number of elements in an object
float(): Converts an object to a floating point (decimal) number
int(): Converts an object to an integer number
str(): Converts an object to a string representation
isinstance(): Returns True if an object is an instance of a given
    class, and False otherwise
type(): Returns a string representation of an object's class
enumerate(): Used in iterators, returns the object as well as
    its index in the iterator as a tuple
print(): You know this one, but under the hood it's actually
    calling either the __str__() method or the __repr__() method
    implemented by the class to get a string to print

Casting functions like float(), int(), and str() work by implementing
instructions within the class that allow them to be converted into the
given type. Without those instructions they do not work. The int class
implements instructions to convert to float and vice versa, but when
you write a class yourself it is also possible to write a method to instruct
the int() funtion, for example, to convert an object of your class into
an integer.

=================================================================
Defined functions
=================================================================
When you define a function yourself you are essentially creating a tool
that you'll want to use more than once. A given function should be very
direct and should only do one thing, even if that thing is just calling
several other functions to define a specific workflow. For instance you
might write a function that stages a dataframe in a database as its own
table, then another function that queries a subset of a larger table into
a temporary table, another to merge the tables you just created, another
to bring the resultant table into the original table, and finally a function
that calls all of those functions in sequence to create a workflow. The
"thing" that a function does can be abstracted out to mean "do all of
these other things" but as long as each of those other things is encapsulated
in another function and the function you've created has a distinct purpose
it's still a valid aplication of the principle.

In its simplest form a function is just a reusable code block. You give it
some information, it runs off and does what it's been made to do, and then
it comes back with the result of that task. The information you give it can
come in two forms: positional arguments and keyword arguments. Let's use the
function definition below as an example and examine it piece by piece:
"""

def my_func(my_var: int, var_2: str, kw_var: None | int = None, kw_2: str = "default"):
    pass

"""
Note that the pass keyword does nothing and just allows for placeholders like
this. The def keyword is what tells python you are about to create a function.
Any function, whether or not it takes arguments, must have opening and closing
parentheses after it before the colon that ends the function definition.

Positional arguments are placed inside the parentheses at the beginning of the
list of arguments. They are required for every run and cannot be given any
default value. They must be provided to the function in the order they are
defined. Above, my_var and var_2 are positional arguments. If you attempt to
call this function without providing at least those 2 arguments, Python will
throw an exception.

Keyword arguments come after all positional arguments. Their value comes in
the ability to set default values for them to allow them to be ommitted in
runs where they are not important. Above, kw_var and kw_2 are keyword arguments.
If you make the call my_func(3, "my_string"), it will still run, and the
variables within the function kw_var and kw_2 will assume the default values
of None and "default" respectively. However you could also make the function
call my_func(4, "another_str", kw_2="keyword_str"), in this case kw_2 would
assume the value of "keyword_str" but kw_var, since it was still ommitted,
would have the value of None.
"""
# Write a function that adds two objects



# Write a function that turns an integer into a string



# Write a function that turns a string into an integer



# Write a function to reverse the order of a list using a for loop



# Write a function that determines if all elements of a list
# are integers. Should return Trus if all elements are integers
# and False otherwise



# Write a function that prints every other object in a list
# starting with the 0 index

# Once you write this function, modify it to also print the
# index of the element you are printing on the same line



# Write a function that detects if a string has an even number
# of characters



# Write a function that simply returns the string "bear"
# This function should accept an optional variable called big_bear
# big_bear should default to False, and if True is passed in
# it should return "BEAR"



# Write a function that adds every other object in a list together
# Use the funtion you made previously to do this.

# Once you have made this function, modify it to accept
# a second argument, a keyword argument called 'even'
# this keyword argument should default to True and if
# set to False it should add the odd-numbered indices of
# the list



# Write a function that accepts a list of integers. It should
# first check that every element of the list IS an integer, and
# if not it should raise a ValueError.
# Next, it should combine each even-indexed number with the next
# odd-indexed number into a single number in a new list
# (e.g. [1,2, 3, 4] becomes [12, 34]), for lists with an odd number
# of elements, it should put the final number unchanged into the new
# list.
# Next, it should sum these new numbers.




def main():
    # Run your functions here using these variables as input
    even_sized_list = [6,5,3,7,9,0,2,3,6,0]
    odd_sized_list = [4,3,1,2,5,0,9,6,2,9,0,8,4,5,7,4,5,6,8,7,4]

    even_sized_string = "walupp"
    odd_sized_string = "gromp"




if __name__ == "__main__":
    main()
