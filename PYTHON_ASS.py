#1
def func(a, b):
 return b if a == 0 else func(b % a, a)
print(func(30, 75))

#2
numbers = (4, 7, 19, 2, 89, 45, 72, 22)
sorted_numbers = sorted(numbers)
even = lambda a: a % 2 == 0
even_numbers = filter(even, sorted_numbers)
print(type(even_numbers))

#3
def my_function(*args):
    print(type(args))

my_function(1)

#4

""" set1 = {14, 3, 55}
set2 = {82, 49, 62}
set3={99,22,17}
print(len(set1 + set2 + set3)) """

#5
print(4**3 + (7 + 5)**(1 + 1))

#6
captains = {
 "Enterprise": "Picard",
 "Voyager": "Janeway",
 "Defiant": "Sisko",
}

for ship, captain in captains.items():
 print(ship, captain)

for ship in captains:
 print(ship, captains[ship])

for ship in captains:
 print(ship, captains)

#7
#captains = {dict}
#type(captains)
#captains.dict()
captains = {}
captains["Enterprise"] = "Picard"
captains["Voyager"] = "Janeway"
captains["Defiant"] = "Sisko"
print(captains)

#8
captains = {
 "Enterprise": "Picard",
 "Voyager": "Janeway",
 "Defiant": "Sisko",
 "Discovery": "unknown",
}

for ship, captain in captains.items():
 print(f"The {ship} is captained by {captain}.")

del captains["Discovery"]
print(captains)
