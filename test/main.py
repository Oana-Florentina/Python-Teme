# Write a class Vocabulary that can we used to construct for operations on a specific vocabulary.
# - class can be instantiated with a string. ex: Vocab("Some input string")
# will generate in the background a vocabulary with the known words "some"
# , "input" and "string" and the known symbols : "S", "s", "o" ...
# - a method statistics can be called to get the current counts for the known words and symbols
# - a method update can be called with a string in order to update the
# current vocabulary and known symbols
# - a method to_string can be called to retun a string with all the
# known words in the vocab concatenated with spaces
# - a method compare can be called with another Vocabulary object as
# a parameter and the words and symbols that apper in both vocabularies will be printed.

import string


class Vocabulary:
    def __init__(self, input_string):
        self.words = set(input_string.lower().split())
        self.symbols = set(c for c in input_string.lower() if c.isalpha() or c.isspace())

    def statistics(self):
        return len(self.words), len(self.symbols)

    def update(self, new_string):
        self.words.update(new_string.lower().split())
        self.symbols.update(c for c in new_string.lower() if c.isalpha() or c.isspace())

    def to_string(self):
        return ' '.join(self.words)

    def compare(self, vocab_2):
        common_words = self.words.intersection(vocab_2.words)
        print("Words in common: ", common_words)


vocab1 = Vocabulary("ana are mere")
print("Statistics:", vocab1.statistics())

vocab1.update("Ana nu mai are mere")
print("Updated statistics:", vocab1.statistics())

print("Vocabulary as string:", vocab1.to_string())




