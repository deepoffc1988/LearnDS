s1 = "Deepak"
s2 = 'Arijith'
s3 = """Avyukth"""
s4 = '''I am learning Python 
    - Basics from Geeks For geeks'''
print(s1)
print(s2)
print(s3)
print(s4)

s5="GeeksForGeeks"

#Accessing first character F
print(s5[5])

#Accessing the char in negative index

print(s5[-9])

print(s5[5:8])

print(s5[:4])
print(s5[8:])

s6 = "g" + s5[1:]
print (s6)

del s6
#Updating a string

s6 = "Hello " + s5
print(s6)

s7 = s6.replace("Hello", "Welcome")
print(s7)

s = "   Gfg   "

# Removes spaces from both ends
print(s.strip())    

s = "Python is fun"

# Replaces 'fun' with 'awesome'
print(s.replace("fun", "awesome"))

#Concat
s, s1 = "Hello ", "world"

s2 = s + " " + s1
print(s2)

#Repeat a string

print (s * 10 + " ")