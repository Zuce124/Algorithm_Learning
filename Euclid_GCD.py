def GCD(a,b):
    c = 1
    if a % b == 0:
        return a
    elif a>b:
        while c != 0:
            c = a%b
            a = b
            b = c
        return a
    else:
        while c != 0:
            c = b%a
            b = a
            a = c
        return b

d = 'Y'

while  d == 'Y':
    a,b = input('Enter two numbers: ').split()
    c = GCD(int(a),int(b))
    print('Your greatest common denominator is: ', c)

    d = input("Do you want to try again(Y/N)?: ")