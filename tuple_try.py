# 1. Create a tuple
my_tuple = (1,"Python", 3.14)

# 2. Print the tuple
print(my_tuple)

# Access and print at index 1
my_tuple_index = my_tuple[1]
print(my_tuple_index)

try:
    my_tuple[0] = 5
except TypeError as e:
    print("\nAn attempt to modify the tuple raised an error.")
    print("Error message:", e)
    print("This demonstrates that tuples are immutable.")