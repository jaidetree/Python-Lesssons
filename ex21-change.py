def add(a, b):
    print "ADDING {} * {}".format(a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING {} - {}".format(a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING {} * {}".format(a, b)
    return a * b

def divide(a, b):
    print "DIVIDING {} / {}".format(a, b)
    return a / b

print "Enter total amount:"
total = money = float(raw_input("$ ") ) * 100

quarters = 0;
dimes = 0;
nickels = 0;
pennies = 0;

quarters = int(money / 25)
money -= quarters * 25

dimes = int(money / 10)
money -= dimes * 10

nickels = int(money / 5)
money -= nickels * 5

pennies = int(money)

print "You have {} quarters, {} dimes, {} nickels, and {} pennies.".format(quarters, dimes, nickels, pennies)
