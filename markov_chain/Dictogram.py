import random

class Dictogram(dict):
    def __init__(self, iterable = None):
        super(Dictogram, self).__init__()
        self.types  = 0 
        self.tokens = 0
        if iterable:
            self.update(iterable)
    
    def update(self, iterable):
        for item in iterable:
            if item in self:
                self[item]  += 1
                self.tokens += 1
            else: 
                self[item] = 1
                self.types +=1 
                self.tokens += 1

    def count(self, item):
        if item in self:
            return self[item]
        return 0

    def return_random_word(self):
        random_key = random.sample(self, 1)
        return random_key[0]

    def return_weighted_random_word(self):
        words = []
        for key in self:
            words.extend([key for i in range(self[key])]) 
        return random.choice(words)
