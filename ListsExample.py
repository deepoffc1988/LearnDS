#SWap 2 elements in a list

a = [1,3,2,4]
print("before", a)
a[1],a[2] = a[2],a[1]
print("after", a)

b = [9,7,8,6]

temp = b[1]
b[1] = b[2]
b[2] = temp

print(b)