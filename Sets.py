#Time Complexity: O(1)
#Auxiliary Space: O(1)

var = { "Learn", "python ", "masterit"}

print(type(var))

lists = [ 4,5,6,8,]
print(type(lists))

var1 = set(lists)
print(type(var1))

var1.add(9)
print(var1)

# Python program to demonstrate that
# a set cannot have duplicate values 
# and we cannot change its items

# a set cannot have duplicate values
myset = {"Geeks", "for", "Geeks"}
print(myset)

# values of a set cannot be changed
#myset[1] = "Hello"
print(myset)

#FrozenSet

froze = frozenset({2,3,4,5,6})
froze1 = frozenset([5,6,7,8,9])
#froze.insert(5)
print(froze)
print ("Union", froze.union(froze1))

print ("Intersection", froze.intersection(froze1))

print ("Difference", froze.difference(froze1))

print ("symmetric Difference", froze.symmetric_difference(froze1))


# A Python program to
# demonstrate adding elements
# in a set

# Creating a Set
people = {"Jay", "Idrish", "Archi"}

print("People:", end = " ")
print(people)

# This will add Daxit
# in the set
people.add("Daxit")

# Adding elements to the
# set using iterator
for i in range(1, 6):
    people.add(i)

print("\nSet after adding element:", end = " ")
print(people)


