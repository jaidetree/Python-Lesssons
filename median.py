from sys import exit
from sys import argv

def collect_data():
    """Get all the data from an input statement."""
    
    loop = True
    numbers = []
    i = 1

    print "Enter a set of numbers then enter \"stop\" when you want the averages."

    while loop:
        answer = raw_input("Enter number ({}): ".format(i))

        if answer == answer.upper():
            numbers.append(float(answer))
            i += 1
        elif answer == "stop":
            loop = False

    return numbers

def read_data(filename):
    """"Read data from file."""
    
    numbers = []

    if not filename:
        print "No file specified in read_data."
        exit(0)

    file = open(filename)
    numbers = file.readlines()

    file.close()

    return numbers

def calc_average(numbers):
    """Calculate the average of all the numbers"""

    if not isinstance(numbers, list):
        print "The numbers is not of a list type. Try again"
        exit()

    total = 0
    average = 0

    for number in numbers:
        total += float(number)

    average = total / len(numbers)

    return average

if len(argv):
    numbers = read_data(argv[1])
else:
    numbers = collect_data

average = calc_average(numbers)

print "The average is: {}".format(round(average,1))

