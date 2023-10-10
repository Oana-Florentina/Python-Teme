def checkPrime(n):
    if n<2:
        return 0
    if n%2==0 and n!=2:
        return 0
    else:
        for index in range (3,n//2):
            if(n%index==0):
                return 0
    return 1
def primes(*list_numbers):
    list_primes=[]
    for num in list_numbers:
        if(checkPrime(num)==1):
            list_primes.append(num)
    return list_primes
print(primes(12,7,11,32,5))
