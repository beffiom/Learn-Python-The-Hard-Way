# initializes a variable 'cars' and sets it to an integer 100
cars = 100
# initializes a variable 'space_in_a_card" and sets it to floating point 4.0
space_in_a_car = 4.0
# initializes a variable 'drivers' and sets it to an integer 30
drivers = 30
# initializes a variable 'passengers' and sets it to an integer 90
passengers = 90
# initializes a variable 'cars_not_driven' and sets it to the difference between the cars and drivers variables
cars_not_driven = cars - drivers
# initializes a variable 'cars_driven' and sets it to the variable drivers
cars_driven = drivers
# initializes a variable 'carpool_capacity' and sets it to the product of the variables cars_driven and space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
# initializes a variable 'average_passengers_per_car' and sets it to the quoitent of the variables passengers and cars_driven
average_passengers_per_car = passengers / cars_driven

# prints the value of the cars variable
print("There are", cars, "cars available.")
# prints the value of the drivers variable
print("There are only", drivers, "drivers available.")
# prints the value of the cars_not_driven variable
print("There will be", cars_not_driven, "empty cars today.")
# prints the value of the carpool_capacity variable
print("We can transport", carpool_capacity, "people today.")
# prints the value of the passengers variable
print("We have", passengers, "to carpool today.")
# prints the value of the average_passengers_per_car variable
print("We need to put about", average_passengers_per_car, "in each car.")

# using a floating point number for space_in_car was not necessary
# '=' is not an operation, but a keyword used to store values into a variable
# '==' is the comparison operator to compare two values
# syntax errors in the names of variables are important to notice, you cannot call a variable that has yet to be created


