num1 = 42 # variable declaration
num2 = 2.3 # variable declaration
boolean = True # data type = primitive = boolean
string = 'Hello World' # data type = primitive = string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # data types = composite = list = initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # data types = composite = dictionary = initialize
fruit = ('blueberry', 'strawberry', 'banana') # data types = composite = tuples = initialize
print(type(fruit)) # type check
print(pizza_toppings[1]) # log statement; data types = composite = list = access value
pizza_toppings.append('Mushrooms') # data types = composite = list = add value
print(person['name']) # data types = composite = dictionary = access value
person['name'] = 'George' # data types = composite = dictionary = change value
person['eye_color'] = 'blue' # data types = composite = dictionary = change value
print(fruit[2]) # log statement; data types = tuples = access value

if num1 > 45: # conditional = if
    print("It's greater") # log statement
else: # conditional = else
    print("It's lower") # log statement

if len(string) < 5: # conditional = if
    print("It's a short word!") # log statement
elif len(string) > 15: # conditional = else if (elif)
    print("It's a long word!") # log statement
else: # conditional = else
    print("Just right!") # log statement

for x in range(5): # conditional = for loop = start
    print(x) # log statement
for x in range(2,5): # conditional = for loop = start
    print(x) # log statement
for x in range(2,10,3): # conditional = for loop = start
    print(x) # log statement
x = 0 #variable declaration ?
while(x < 5): # while loop = start
    print(x) #log statement
    x += 1 # while loop = increment

pizza_toppings.pop() # data types = composite = list = delete value
pizza_toppings.pop(1) # data types = composite = list = return deleted value (add value?)

print(person) # log statement
person.pop('eye_color') # data types = composite = dictionary = delete value
print(person) # log statement

# log statement; deleting value; log statement again

for topping in pizza_toppings: # for loop = start
    if topping == 'Pepperoni': # for loop = if
        continue # for loop = continue
    print('After 1st if statement') # log statement
    if topping == 'Olives': # for loop = if
        break # for loop = break

def print_hello_ten_times(): # function = parameter
    for num in range(10): # function = argument; for loop
        print('Hello') # function = return; log statement

print_hello_ten_times() # function call (?)

def print_hello_x_times(x): # function = parameter
    for num in range(x): # function = argument; for loop
        print('Hello') # function = return; log statement

print_hello_x_times(4) # function call (?)

def print_hello_x_or_ten_times(x = 10): # function = parameter
    for num in range(x): # function = argument; for loop
        print('Hello') # function = return; log statement

print_hello_x_or_ten_times() # function call (?)
print_hello_x_or_ten_times(4) # function call (?)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)