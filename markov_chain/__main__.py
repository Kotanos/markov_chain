import random
import models 
import json
from collections import deque
import re

#Use this to get fisrt word from model 
def generate_random_start(model, seed = "START"):
    return model[seed].return_weighted_random_word()
#    return random.choice(model.keys())

def generate_random_sentence(length, markov_model):
    current_word = generate_random_start(markov_model)
    sentence = [current_word]
    for i in range(0, length):
        current_dictogram = markov_model[current_word]
        random_weighted_word = current_dictogram.return_weighted_random_word() 
        if random_weighted_word == 'END':
            break    
        current_word = random_weighted_word
        sentence.append(current_word)
    sentence[0] = sentence[0].capitalize()
    return ' '.join(sentence) + '.'

def get_data(path):
    with open(path, 'r', encoding = 'utf') as f:
        return json.load(f)

def build_model(ls):
    items = []
    for ob in ls:
        words = []
        words = ob.split(' ')
        words.append('END')
        words.insert(0,'START')
        items.append(words)
    model = None
    for item in items:
        if model:
            models.update_markov_model(model, item)
        else:
            model = models.make_markov_model(item) 
    return model        

def getModel():
    with open('model.json','r', encoding = 'utf') as f:
        model = json.load(f)
    for key in model:
        model[key]=models.Dictogram(model[key])    
    return model

if __name__ == "__main__":
    ls = []
#    with open("data\\angldata.txt", 'r') as f:
#        ls = f.read().split('.')
    with open("data\\data3.json", 'r', encoding='utf') as f:
        for ob in json.load(f):
            ls.append(ob['commentText'])
    model = build_model(ls)
    
    results = []
    for i in range(400):
        results.append(generate_random_sentence(5, model))
    with open('res.txt','w', encoding='utf') as f: 
        for ob in results:
            f.write(ob+'\n')