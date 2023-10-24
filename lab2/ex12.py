#  12. Write a function that will receive a list of words
#  as parameter and will return a list of lists of words, grouped by rhyme.
#  Two words rhyme if both of them end with the same 2 letters.


def group_by_rhyme(words):
    rhymes = {}

    for word in words:
        ending = word[-2:]

        if ending not in rhymes:
            rhymes[ending] = []

        rhymes[ending].append(word)

    grouped_by_rhyme = list(rhymes.values())

    return grouped_by_rhyme

words = ['ana', 'banana', 'aana', 'carte', 'arme', 'parte']
result = group_by_rhyme(words)
print(result)
