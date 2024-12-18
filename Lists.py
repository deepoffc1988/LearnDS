
a = [1,2,3,4]
print("Lists: ",  type(a))
str1 = ['apple', 'banana', "cherry"]
print("String: ", str1)
mixstr = [ 1, 2.3, True, 'cat']
print("Mixed String: ", mixstr)

b = list((112,3,43, "banana", 6.3))
print(b)


#List with repeated elements 

c = [5] * 9
d = [4] * 3

print("Repeated elements in list: ", c, d)

#ACcessing elements in lists

e = [20,40,50,45,90]

print(e[-2])
print(e[0])

e.append(10)
print("After appending", e)
e.insert(2,30)
print("after inserting at index 2", e)
e.extend([25,35,45])
print("AFter Extending", e)

e.remove(30)
print("After removing ", e)
e.pop(2)
print("after popping at index 2", e)

del e[4]
print("AFter Deleting",e)


for item in e :
    print (item)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access element at row 2, column 3
print(matrix[2][1]) 

