name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth
print "This is what %%x does: %x" % ( weight )
print "This is how strings should be formatted {}".format( name )
print "{} inches = {} centimeters".format(  height, height * 2.54 )
print "{} lbs = {} kg".format( weight, weight * 0.45359237 )

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % ( age, height, weight, age + height + weight )
