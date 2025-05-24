# Conditional Statement

input_num = int(input("Please enter your grade: "))

if input_num < 0:
    print("Enter valid numbers.")                   
else: 
    if 90 <= input_num <= 100:
        print("A")
    elif 80 <= input_num < 90:
        print("B")
    elif 70 <= input_num < 80:
        print("C")
    elif 60 <= input_num < 70:
        print("A")
    else:
        print("F")         