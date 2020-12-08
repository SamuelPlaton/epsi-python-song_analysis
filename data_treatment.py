from flask import request, Flask, jsonify
from flask_restplus import Api, Resource, fields
from werkzeug.contrib.fixers import ProxyFix

import json
import string
import csv
import pandas as pd  # pip3 install pandas
import spacy  # pip3 install spacy ET python3 -m spacy download en_core_web_md
import nltk  # pip3 install nltk
import lyricsgenius # pip3 install lyricsgenius
from gensim.corpora import Dictionary  # pip3 install gensim
from gensim.utils import simple_preprocess
from gensim.models import LdaModel

# Retrieve and pretreat data
class getDatas(Resource):
    genius = lyricsgenius.Genius("cBFptPjIfCWpvKjqgMgXmOW24-D-Xfx9A4wa11p_GJ2JeM82HBsJidIAJCx4NbMs")
    def get(self):
        # Loading our stopwords
        nlp = spacy.load("fr_core_news_sm")  # loading the french model || en_core_web_md for the english one
        spacy_stopwords = spacy.lang.fr.stop_words.STOP_WORDS # spacy.leng.en for english one
        # Getting back our datas
        data = self.getData()
        # Pretreatment of the text
        elements = []
        sentences = data.split('\n') #Travel  sentences
        for sentence in sentences:
            words = sentence.split(" ")
            for word in words: #Travel words
                element = self.pretraitement(word, nlp, spacy_stopwords) # Treat word to get lemma
                for a in element:
                    if a not in '!,...?":;0123456789&[]\\\n':  # if it's not a punctuation
                        elements.append(a)
        return elements

    # Pretreatment of our data (lemme and stopwords)
    def pretraitement(self, words, nlp, spacy_stopwords):
        tokens = [word.lemma_.lower() for word in nlp(words) if word.text.lower() not in spacy_stopwords]
        return tokens

    # Get our datas
    def getData(self):
        # Searching our song
        data = self.genius.search_song("ninho rose")
        # Return our lyrics
        return data.lyrics

    # Get the x most common terms excepted the stopwords
    def getMostCommonData(self, number):
        data = self.get()
        # Getting the most common words of our data
        freq = nltk.FreqDist(data)
        return freq.most_common(number)

data = getDatas()
#lyrics = data.getData()
#print(lyrics)

#goodData = data.get()
#print(goodData)

mostCommon = data.getMostCommonData(10)
print(mostCommon)