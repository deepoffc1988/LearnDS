a,b,c = True, False, True

if a and c:
    print("A is true and B is false")

if not b:
    print("B is true")

if b or c:
    print("Either b or c is true")

a,b,c = 10,10,-10

if (a<0) or (b>0):
    print("numbers are greater than 0")
if(a>0) and b>0 and c>0:
    print("Numbers are greater than 0")
else:  
    print("Atleast one number is not greater than 0")

a = 10

if not a:
    print("Boolean value of a is True")
if not (a % 3 == 0 or a % 5 == 0):
    print("10 is not divisible by either 3 or 5")
else:
    print("10 is divisible by either 3 or 5")

def order(x):
    print("Method called for value:", x)
    return True if x > 0 else False


a = order
b = order
c = order
if a(-1) or b(5) or c(5):
    print("Atleast one of the number is positive")