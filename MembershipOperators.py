import operator
# Membership Operators

# initialized some sequences
list1 = [1, 2, 3, 4, 5]
str1 = "Hello World"
set1 = {1, 2, 3, 4, 5}
dict1 = {1: "Geeks", 2:"for", 3:"geeks"}
tup1 = (1, 2, 3, 4, 5)

# using membership 'in' operator
# checking an integer in a list
print(2 not in list1) #False

# checking a character in a string
print('O' not in str1) #True

# checking an integer in aset
print(6 in set1) #False

# checking for a key in a dictionary
print(3 in dict1) #True

# checking for an integer in a tuple
print(9 in tup1) #False

print(operator.contains({1, 2, 3, 4, 5},2))

# Python program to illustrate the use
# of 'is' and '==' operators
a = [1, 2, 3]
b = [1, 4, 3]
c= a

# using 'is' and '==' operators
print(a is b)
print(c is a)
print(a != b)