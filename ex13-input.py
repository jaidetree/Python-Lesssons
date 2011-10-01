from sys import argv

script,initial = argv
total = int(initial)

number = raw_input("Enter a number: ")
total += int(number)

print "The grand total is {}".format( total )
