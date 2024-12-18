#TEST

def my_decorators(func): 
    def wrapper():
        print("BEFORE")
        func()
        print("AFTER")
        return wrapper
    
@my_decorators
def say_hello():
    print("MIDDLE")    

say_hello()