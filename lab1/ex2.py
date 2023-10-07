#2.Write a script that calculates how many vowels are in a string.
vowels = "AEIOUaeiou"
word = "Ana are mere verzi"
count = 0
for char in word:
        if char in vowels:
            count += 1
print(count)