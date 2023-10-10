#6. Write a function that validates if a number is a palindrome.
x=int(input("x: "))
cx=x
ogl=0
while x!=0:
    ogl=ogl*10+x%10
    x=x//10 #int
if cx==ogl:
    print(cx, "is palindrome")
else:
    print(cx, "is not palindrome")
