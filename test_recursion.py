
def countdown(x):
    if x == 0:

        print(x,"...\ndone!")
        return
    else:
        print(x,"...")
        countdown(x-1)

def factorial(x):
    if x == 0:
        return 1
    else:
        return x*factorial(x-1)

def exponent(x,y):
    if y == 0:
        return 1
    else:
        return x*exponent(x,y-1)


#countdown(4)
print(factorial(4))
print(exponent(2,5))