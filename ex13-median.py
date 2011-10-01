from sys import argv

script, num1, num2, num3, num4 = argv
median = ( int(num1) + int(num2) + int(num3) + int(num4) ) / 4.0

print "You've entered {}, {}, {}, and {} into {}. The median is: {}.".format( num1, num2, num3, num4, script, median )
