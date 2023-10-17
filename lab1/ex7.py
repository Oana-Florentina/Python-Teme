#7. Write a function that extract a number from a text (for example if the text is "An apple is 123 USD", this function will return 123, or if the text is "abc123abc" the 
#function will extract 123). The function will extract only the first number that is found.
def extract_first_number(text):
    num = ""
    found_number = False

    for char in text:
        if char.isdigit():
            num += char
            found_number = True
        elif found_number:
            break

    if num:
        return int(num)
    else:
        return None


text1 = "An apple is 4x5 USD"
text2 = "abc123ab5c"

number1 = extract_first_number(text1)
number2 = extract_first_number(text2)

if number1 is not None:
    print(f"Number in text1: {number1}")
else:
    print("No number found in text1")

if number2 is not None:
    print(f"Number in text2: {number2}")
else:
    print("No number found in text2")
