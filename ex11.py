# prompts the user for a response and stores that response in a variable using the input function
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

# returns a statement based on user response
print(f"So, you're {age} years old, {height} tall and {weight} heavy.")
