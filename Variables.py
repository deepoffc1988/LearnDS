#Variables
x = 10 #Integer
y = 3.14 #FLoat
name = "Deepak" #String
lists = [1,2,3,4,5] # list are mutable (modifiable)
#Packing
tupless = ["apple", "cat", "dog"] # tuples are not mutable and more memory efficient than list

#Unpacking
fruit1, animal1, animal2 = tupless
print (lists, tupless, x * y, tupless[1], animal2)

for fruit in tupless:
    print (fruit) 


for lis in lists:
    print(lis)

#Dictionary - store data in key value pairs- ordered, changeable and do not allow duplicates

student = {
    "name" : "Deepak",
    "age" : 24,
    "major" : "Computer Science"
}

print(student["major"])

student["age"]=36 

print("after modifying student age", student["age"])

for key, value in student.items():
    print(key, ":", value)

del student["major"]

#VARIABLE NAMES CAN BE DIFFERENT


#CamelCase
myVarName = "Deepak"

#PascalCase
MyVarName = 'Deepak'

#SnakeCase
my_var_name = "Deepak"