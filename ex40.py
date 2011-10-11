cities = { 'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville' }

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap, state):
    if state in themap:
        return themap[state]
    else:
        return "Not found."

# ok pay attention!
cities['_find'] = find_city

while True:
    print "State? (ENTER to quite)",
    state = raw_input("> ")

    if not state: break

    # this line is the most important ever! study!
    city_found = cities['_find'](cities, state)
    print city_found

for code, city in cities.iteritems():
    if type(city) != str:
        continue
    print code + ": " + str(city)
