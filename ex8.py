# initializes a variable 'formatter' as a string with four escape sequences to embed variables
formatter = "{} {} {} {}"

# replaces the escape sequences with the values specified by the format function and prints them
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Hippity!",
    "Hoppity!",
    "Your hard-earned income is now...",
    "my property! - The IRS"
))
