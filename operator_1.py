print("Please provide two inputs!")
input_1 = input("Enter first input: ")
input_2 = input("Enter second input: ")

int_1 = int(input_1)
int_2 = int(input_2)

input_oper = input("Enter '+','-','*' or '/': ")
int_oper = str(input_oper)

if int_oper == '+':
    result = int_1 + int_2
elif int_oper == '-':
    result = int_1 - int_2
elif int_oper == '*':
    result = int_1 * int_2
elif int_oper == '/':
    if int_2 != 0:
        result = int_1 + int_2  
    else:
        result = "Zero Error"      
else:
    result = "Provide the operator properly"
    
print(result)



