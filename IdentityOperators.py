

# Identity Operators

# Python program to illustrate the use
# of 'is' identity operator
num1 = 5
num2 = 7
num3 = num2
num4 = num2
print(num4 is num2)
print(num1 is num2)
print(num3 is num1)

lst1 = [1, 2, 3]
lst2 = [1, 4, 3]
lst3 = lst1
lst4 = lst2
lst5 = lst4
print(lst1 is lst2)
print(lst3 is lst1)
print(lst4 is not lst5)

str1 = "hello world"
str2 = "hello world"

print(str1 is str2)

# using 'is' identity operator on different datatypes
'''print(num1 is num2)
print(lst1 is lst2)
print(lst3 is lst1)
print(str1 is str2)

print (lst1 is not lst2)
print(num1 is not num2)
'''