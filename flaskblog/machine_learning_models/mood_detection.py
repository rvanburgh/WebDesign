import json
import pandas as pd
from flask import Flask, request, abort, Response
from keras.preprocessing.sequence import pad_sequences
from keras import backend
from keras.models import model_from_json
import pickle
import os
import re


class SentimentService(object):
    model1 = None
    tokenizer = None

    @classmethod
    def load_deep_model(self, model):
        json_file = open('./flaskblog/machine_learning_models/mood-saved-models/' + model + '.json', 'r')
        loaded_model_json = json_file.read()
        loaded_model = model_from_json(loaded_model_json)

        loaded_model.load_weights('./flaskblog/machine_learning_models/mood-saved-models/' + model + ".h5")

        # loaded_model._make_predict_function()
        return loaded_model

    @classmethod
    def get_model1(self):
        if self.model1 is None:
            self.model1 = self.load_deep_model('model5_ver1')
        return self.model1

    @classmethod
    def load_tokenizer(self):
        print(os.getcwd())
        if self.tokenizer is None:
            with open('./flaskblog/machine_learning_models/mood-saved-models/tokenizer.pickle', 'rb') as handle:
                self.tokenizer = pickle.load(handle)
        return self.tokenizer


class TextPreprocessing(object):


    def __init__(self):
        self.FLAGS = re.MULTILINE | re.DOTALL

    def hashtag(self,text):
        text = text.group()
        hashtag_body = text[1:]
        if hashtag_body.isupper():
            result = " {} ".format(hashtag_body.lower())
        else:
            result = " ".join([""] + [re.sub(r"([A-Z])",r" \1", hashtag_body, flags=self.FLAGS)])
        return result

    def allcaps(self,text):
        text = text.group()
        return text.lower() + " "

    def re_sub(self,pattern, repl,text):
            return re.sub(pattern, repl, text, flags=self.FLAGS)

    def text_preprocessing(self,text):
        eyes = r"[8:=;]"
        nose = r"['`-]?"

        def re_sub(pattern, repl):
            return re.sub(pattern, repl, text, flags=self.FLAGS)

        text = re_sub(r"https?:\/\/\S+\b|www\.(\w+\.)+\S*", " ")
        text = re_sub(r"@\w+", "user")
        text = re_sub(r"{}{}[)dD]+|[)dD]+{}{}".format(eyes, nose, nose, eyes), "smile")
        text = re_sub(r"{}{}p+".format(eyes, nose), "laugh")
        text = re_sub(r"{}{}\(+|\)+{}{}".format(eyes, nose, nose, eyes), "sad")
        text = re_sub(r"{}{}[\/|l*]".format(eyes, nose), "neutral")
        text = re_sub(r"/"," / ")
        text = re_sub(r"<3","love")
        text = re_sub(r"[-+]?[.\d]*[\d]+[:,.\d]*", " ")
        text = re_sub(r"#\S+", self.hashtag)
        text = re_sub(r"([!?.]){2,}", r"\1 repeat")
        text = re_sub(r"\b(\S*?)(.)\2{2,}\b", r"\1\2 <elong>")
        text = re_sub(r"([A-Z]){2,}", self.allcaps)

        return text.lower()


def predict_mood(text):

    # if not request.json or not 'text' in request.json:
    #     abort(400)

    tp = TextPreprocessing()

    sent = pd.Series(text)
    new_sent = [tp.text_preprocessing(i) for i in sent]

    seq = SentimentService.load_tokenizer().texts_to_sequences(pd.Series(''.join(new_sent)))
    test = pad_sequences(seq, maxlen=256)

    
    model = SentimentService.get_model1()

    res = model.predict(test,batch_size=32, verbose=0)

    lab_list = ['anger', 'disgust', 'fear', 'guilt', 'joy', 'sadness', 'shame']
    moods = {}
    for actual, probabilities in zip(lab_list, res[0]):
        moods[actual] = 100*probabilities

    return moods
