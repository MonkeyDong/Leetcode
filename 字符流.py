from collections import defaultdict
from functools import reduce

class StreamChecker(object):

    def __init__(self, words):
        T = lambda: defaultdict(T)
        self.trie = T()#一个defaultdict字典
        for w in words: reduce(dict.__getitem__, w, self.trie)['#'] = True#按每一个词建立一个defaultdict
        self.waiting = []

    def query(self, letter):
        self.waiting = [node[letter] for node in self.waiting + [self.trie] if letter in node]
        return any("#" in node for node in self.waiting)


