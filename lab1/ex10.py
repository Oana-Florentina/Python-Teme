#Write a function that counts how many words exists in a text.
# A text is considered to be form out of words that are separated 
#by only ONE space. For example: "I have Python exam" has 4 words.

def count_spaces(text):
    word_count=0
    x=''
    if text[0]== ' ':
        word_count=word_count-1
    n=len(text)
    if text[n-1]== ' ':
        word_count=word_count-1
    for char in text:
        if char == ' ' and x!= ' ':
            word_count=word_count+1
        x=char
    return word_count+1

    
text = "  I have   Python exam  "
word_count= count_spaces(text)

print(f"The text contains {word_count} words")
