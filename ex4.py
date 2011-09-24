# There are 100 cars
cars = 100

# Theres only 4 seats in a car.
space_in_a_car = 4.0

# 30 Drivers
drivers = 30

# 30 Passengers
passengers = 90

# Calculate how many cars wont be driven.
cars_not_driven = cars - drivers

# There is only 1 driver per car.
cars_driven = drivers

# How many groups of people do we have?
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

