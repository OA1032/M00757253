value = input('''Welcome to the menu. Options are listed blelow!: 
\n\t 1. Roll 
\n\t 2. Sweep 
\n\t 3. Scrool \n 
Type the number of your choice and press Enter.''')

v = input()

#print ("The value you input is:", value)
#print (f'it is of the type, {type(value)}.')

def roll(val):
    return val**val
def sweep(val):
    return val*val
def scrool(val):
    return val+val
1
while True:
    if value.isdigit() == True: #.. is digit
        value = int(value)
        '''print("The converted is :", value)
        print ("The value you input is:", value)
        print (f'it is of the type, {type(value)}.')'''
        break ## on correct datatype: exit the loop 
    else: 
        value = input("Invalid input, please provide an integer:")
    print("Input the value you want to roll")
    if v != int:
        print("please enter an integer")
v = int(v)
print ("The converted is:", value)
print(f'it is of type {type(value)}.')

if value == 1:
    print(roll(v))
elif value == 2:
    print(sweep(v))
elif value == 3:
    print(scrool(v))

if value > 3 or value < 1: 
    print("Invalid input ")