import random

print("\nGuessing game")
target_number = random.randint(1,10)
guess = ''

while guess != target_number:
    try: 
        guess = int(input("Enter a number between 1 to 10: "))
    except ValueError:
        print("That is not a valid number")
        continue
    
    if guess < target_number:
        print("Your guess is lower than the number")  
        
    elif guess > target_number:
        print("Your number is higher than the number")  
        
print(f"Congratutions, {guess} is the correct number!")        