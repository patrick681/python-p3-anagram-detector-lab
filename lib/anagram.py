# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = sorted(self.word)

    def match(self, word_list):
        matches = []
        for w in word_list:
            if w.lower() != self.word and sorted(w.lower()) == self.sorted_word:
                matches.append(w)
        return matches
class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = sorted(self.word)

    def match(self, word_list):
        matches = []
        for w in word_list:
            if w.lower() != self.word and sorted(w.lower()) == self.sorted_word:
                matches.append(w)
        return matches
