# initializing a variable 'types_of_people' as an integer
types_of_people = 10
# initializing a variable 'x' as a formatted string with an embedded variable
x = f"There are {types_of_people} types of people."

# initializing a variable 'binary' as a string
binary = "binary"
# initializing a variable 'do_not' as a string
do_not = "don't"
# initializing a variable 'y' as a formatted string with two embedded variables
y = f"Those who know {binary} and those who {do_not}."

# printing x
print(x)
# printing y
print(y)

# printing a formatted string with embedded variable x
print(f"I said: {x}")
# printing a formatted string with embedded variable y
print(f"I also said: '{y}'")

# initializing a variable 'hilarious' as binary value False
hilarious = False
# initializing a variable 'joke_evualation' as a string
joke_evaluation = "Isn't that joke so funny?! {}"

# printing joke_evaluation formatted with hilarious as an embedded variable
print(joke_evaluation.format(hilarious))

# initializing a variable 'w' as a string
w = "This is the left side of..."
# initializing a variable 'e' as a string
e = "a string with a right side."

# printing a concatenated string combining 'w' and 'e'
print(w+e)
