import numpy as np
import matplotlib.pyplot as plt

class TrieNode:
    def __init__(self, c=""):
        self.c = c
        self.children = {}
        self.end = False

    def set_inorder(self, val = [0]):
        children = list(self.children.values())
        mid = len(children)//2
        for i in range(mid):
            children[i].set_inorder(val)
        self.x = val[0]
        val[0] += 1
        for i in range(mid, len(children)):
            children[i].set_inorder(val)
    
    def plot(self, y = 0):
        x1, y1 = self.x, y
        sz = 40
        c = 'k'
        if self.end:
            sz = 100
            c = 'r'
        plt.scatter(x1, y1, sz, c)
        plt.text(x1+0.3, y1+0.1, self.c)
        for c in self.children:
            x2, y2 = self.children[c].x, y-1
            plt.plot([x1, x2], [y1, y2])
            self.children[c].plot(y-1)

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add_word(self, s):
        ## TODO: Fill this in
        pass
    
    def contains_word(self, s):
        ## TODO: Fill this in
        pass
    
    def get_words(self, s):
        words = []
        ## TODO: Fill this in
        return words

    def plot(self):
        self.root.set_inorder()
        self.root.plot()
        plt.axis("off")