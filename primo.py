import math

def isPrime(number):
    if number <= 1 or (number%2) == 0:
        return False
    for check in range(3, int(math.sqrt(number))):
        if number % check == 0:
            return False
    return True

def check(n):
    print ("isPrime(" + str(n) + ") = " + str(isPrime(n)))

#check(2)
#check(9)

def isPrime2(num):
    if num <2:
        return False
    if num ==2:
        return True

    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def check2(n):
    print ("isPrime2(" + str(n) + ") = " + str(isPrime2(n)))

check2(2)
check2(3)
check2(5)
check2(7)
check2(9)


def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

#print(es_primo(9))