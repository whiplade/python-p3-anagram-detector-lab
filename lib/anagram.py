class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = sorted(self.word)
    
    def match(self, anagrams):
        matches = []
        for anagram in anagrams:
            if self.word != anagram.lower() and self.sorted_word == sorted(anagram.lower()):
                matches.append(anagram)
        return matches
    
listen = Anagram("listen")
result = listen.match(['enlists', 'google', 'inlets', 'banana'])
print(result)