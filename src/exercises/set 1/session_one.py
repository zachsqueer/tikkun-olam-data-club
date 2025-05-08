from pathlib import Path
from typing import Any
import sys

x = "one"
y = x
z = [x, y]
i = [1, 2]
j = {"strings": z, "numbers": i}

d, u = i

print(len(i))
print(i, str(i))

for number in i:
    print(number)


################# Lists ####################
this = Path(__file__)
that = Path(sys.argv[0])

my_list = [this, that]

other_list = [1, that]

nested_list = [my_list, other_list]

test = other_list[0]

print(test)

numbers = [3, 7, 1, 8, 4, 7, 2, 8]

sorted(numbers)

print(numbers)

test = sorted(numbers)

print(test)

more_numbers = numbers.copy()

print(more_numbers.sort())

more_numbers = numbers
more_numbers.sort()

print(numbers)


################# Dictionaries ####################

test_dict = {(1, 2): "tuple"}
# test_dict = {[1, 2]: "list"}  # This will cause a TypeError

print(test_dict[(1, 2)])

test_dict[(3, 4)] = "also a tuple"
temp_dict = {(5, 6): "tuple 3: still tuplin'"}
test_dict.update(temp_dict)
test_dict["oops"] = [7, 8]

print(test_dict.keys())
print(test_dict.values())
print(test_dict.items())

for key, value in test_dict.items():
    print(key)
    print(value)
print(test_dict.get("oops"))
print(test_dict.get("big_oops"))
print(test_dict.get((2, 7), "whew"))


################# Nesting ####################


one = [1, 2, 3]
two = [4, 5, 6]
three = [7, 8, 9]

list_2d = [one, two, three]

print(list_2d[1][2])

three = {"one": 1, "two": 2, "three": 3}

mixed_nest = [one, two, three]
print(mixed_nest[2]["two"])


test_dict = {"one": 1, "two": 1, "three": 3}

test_one = [1, 2]
test_two = [1, 2]
if test_one is test_two:
    print("success")
elif test_one == test_two:
    print("partial_success")
else:
    print("failure")


while True:
    print("I can't stop")
    check = input()
    if check == "stop":
        break

for i in range(1, 11):
    print(f"this is loop number {i}")


class MyFirstClass:
    def __init__(self, input: str):
        self.my_attribute = input
        self.another_attribute = "also an attribute"
        self.filler_attribute = "this is an attribute"
        self.attrs = {}

    def print_all_attrs(self):
        print(self.my_attribute, self.another_attribute, self.filler_attribute)

    def set_attr(self, input_key: Any, input_val: Any):
        self.attrs[input_key] = input_val


my_object = MyFirstClass("this is my attribute")
my_object.print_all_attrs()

my_object.set_attr("my key", "my value")

print(my_object.attrs["my key"])
