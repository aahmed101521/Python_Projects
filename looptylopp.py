# Loop-ty-loop      
print("Generating numbers with for loop")
# For Loop
#
print('#########')
for johannes in range(11):
    print(johannes) 
    
print('#########')
for i in range(1,11,2):
    print(i) 
    
print('#########')

transfer_targets = ['Viktor','Nico','Garcia','Zubi']

for transfer in transfer_targets:
    print(transfer)

    
print("###########") 

i = 0

while i < 5:
    i += 1
    print(i)
    
passwd = ''    

while passwd != 'NusratKamal':
    passwd = str(input('Please enter password: '))
    if passwd != 'NusratKamal':
        print("Access Denied. Try again")

print("Access Granted!")