#3.Write a script that receives two strings and prints the number of occurrences of the first string in the second.
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
count = 0
index = string1.find(string2)
while index != -1:
        count += 1
        index = string1.find(string2, index + 1)
print(count)