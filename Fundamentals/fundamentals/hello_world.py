# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Monique"
print("Hello", name)	# with a comma
print("Hello " + name)	# with a +
# 3. print "Hello 42!" with the number in a variable
num = 23
print("Hello", num)	# with a comma
print("Hello " + str(num))	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "baba ghanouj"
fave_food2 = "lasagna"
print("I love to eat " + str(fave_food1) + " and " + str(fave_food2) + ".") # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}.") # with an f string