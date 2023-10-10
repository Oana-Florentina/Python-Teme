def is_palindrome(x):
    cx=x
    ogl=0
    while x!=0:
        ogl=ogl*10+x%10
        x=x//10 #int
    if cx==ogl:
        return 1
    else:
        return 0

def find_palindromes(numbers):
    palindromes = [num for num in numbers if is_palindrome(num)]
    
    num_of_palindromes = len(palindromes)
    greatest_palindrome = max(palindromes, default=None)
    
    return (num_of_palindromes, greatest_palindrome)


number_list = [123, 121, 1331, 45654, 78987, 42, 555]
result = find_palindromes(number_list)
print(result)
