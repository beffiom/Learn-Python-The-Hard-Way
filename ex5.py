# initializes a variable 'name' and stores a string into it
name = 'Benjamin J. Effiom'
# initializes a variable 'age' and stores an integer into it
age = 22
# initializes a variable 'height' and stores an integer into it
height_imperial = 72 # inches
# initializes a variable 'height_metric' to convert inches to cm
height_metric = round(height_imperial * 2.54) # cm
# initializes a variable 'weight' and stores and integer into it
weight_imperial = 160 # lbs
# initializes a variable 'weight_metric' to convert lbs to kg
weight_metric = round(weight_imperial / 2.2046) #kg
# initializes a variable 'eyes' and stores a string into it
eyes = 'Brown'
# initalizes a variable 'teeth' and stores a string into it
teeth = 'White'
# initializes a variable 'hair' and stores a string into it
hair = 'Brown'

# prints a formatted string with the {} escape sequence to embed the value of a variable
print(f"Let's talk about {name}.")
print(f"He's {height_imperial} inches ({height_metric} cm) tall.")
print(f"He's {weight_imperial} pounds ({weight_metric} kg) heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the tea.")

# this line is tricky, try to get it exactly right
# initializes a variable and sets it to the sum of the age, height, and weight variables
total = age + height_imperial + weight_imperial
print(f"If I add {age}, {height_imperial}, and {weight_imperial} I get {total}.")
