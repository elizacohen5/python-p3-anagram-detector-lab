# your code goes here!
class Anagram:
    def __init__(self, word):
        self._word = word
    
    def match(self, word_list):
        sorted_word = ''.join(sorted(self._word))
        anagram_list = []
        for word in word_list:
            if sorted_word == ''.join(sorted(word)):
                anagram_list.append(word)
        return anagram_list
    

listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))