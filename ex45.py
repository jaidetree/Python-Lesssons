## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Has a name 
        self.name = name

## Cat is a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Has a name 
        self.name = name

## Person is a object
class Person(object);

    def __init__(self, name):
        ## Has a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is a person
class Employee(Person):

    def __init(self, name, salary):
        ## Class the person's constructor
        super(Employee, self).__init__(name)

        ## Employee has a salary
        self.salaery = salary

## Fish is a object
class Fish(object);
    pass

## Salmon is a Fish
class Salmon(Fish):
    pass

## Halibut is a Fish
class Halibut(Fish):
    pass

rover = Dog("Rover")

## Satan is a Cat (Object)
satan = Cat("Satan")

## Mary is a Person (Object)
mary = Person("Mary")

## Mary has a Cat (Object)
mary.pet = satan

## Frank is a Employee (Object)
frank = Employee("Frank", 120000)

## Frank has a pet (Object)
frank.pet = rover

## Flipper is a fish
flipper = Fish()

## Crouse is a Salmon
crouse = Salmon()

## Harry is a Halibut
harry = Halibut()

