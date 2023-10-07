#9. Write a functions that determine the most common letter in a string.
# For example if the string is "an apple is not a tomato", then the most common character is "a" (4 times). 
#Only letters (A-Z or a-z) are to be considered. 
#Casing should not be considered "A" and "a" represent the same character.
def most_common_letter(s):
   
    letter_count = {}
    
    for char in s:
        if char.isalpha(): 
            letter_count[char] = letter_count.get(char, 0) + 1#daca nu il gasesc, in adaug

   
    most_common = max(letter_count, key=letter_count.get)
    
    return most_common, letter_count[most_common]
text = "an apple is not Aa tomato"
common_letter, count = most_common_letter(text)
print(f"The most common letter is '{common_letter}' with {count} occurrences.")
