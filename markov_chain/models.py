from Dictogram import Dictogram

def make_markov_model(data):
    markov_model = dict()
    for i in range(0, len(data)-1):
        if data[i] in markov_model:
            markov_model[data[i]].update([data[i+1]])
        else:
            markov_model[data[i]] = Dictogram([data[i+1]])
    return markov_model

def update_markov_model(model, data):
    for i in range(0, len(data)-1):
        if data[i] in model:
            model[data[i]].update([data[i+1]])
        else:
            model[data[i]] = Dictogram([data[i+1]])