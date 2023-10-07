#4.Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.
input_str ="UpperCamelCase"
x = ""
for char in input_str:
    if char.isupper():
        if x: #ca sa nu adaug _ la inceput
            x += "_"
        x += char.lower()
    else:
        x += char
print(x)
