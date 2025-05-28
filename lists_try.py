#Create lists

numbers = [10, 25, 5, 40, 15, 30]
for number in numbers:
    print(number)

total_sum = sum(numbers)
print(f"The total sum is {total_sum}")

average = sum(numbers)/len(numbers)
print(f"The average is {average}")

numbers.append(50)
print(numbers)

numbers.remove(25)
print(numbers)

if len(numbers) > 1:
    removed_element = numbers.pop(1)
    print(removed_element)
    print(numbers)
else:
    print("Not enough numbers")    
    
    
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)