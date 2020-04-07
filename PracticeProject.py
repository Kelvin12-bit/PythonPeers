# This program takes input from a user and finds the collatz sequence
def collatz(number):
    if number %2 == 0:
        return number//2
        
        
    elif number %2 == 1:
        return 3* number+1
        
print('THE COLLATZ SEQUENCE')

value= int(input('Enter a value: '))   # Takes input from the user

print('The collatz sequence is:') # The output for the sequence

# Condtions for the loop
while value != 1:
    newValue = collatz(value)
    print(int(collatz(value)))
    value = newValue





