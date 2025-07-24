# Define a function that takes two arguments and returns their sum

value = 0

def add_number(a,b):
    value = int(a) + int(b)
    return value

a = input("provide first number:")
b = input("provide second number:")
total = add_number(a,b)
print(f"The sum of the two numbers are: {total}")
