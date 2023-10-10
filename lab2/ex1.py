def fibo(n):
    i=2
    a=1
    b=1
    fibList = []
    fibList.append(a)
    fibList.append(b)
    while i<n:
        c=a+b
        fibList.append(c)  
        a=b
        b=c
        i=i+1
    return fibList
print(fibo(5))

        
        
        