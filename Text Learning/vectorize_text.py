#!/usr/bin/python

import os
import pickle
# import re
from pprint import pprint as pp
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk import word_tokenize
from parse_out_email_text import parseOutText

"""
    Starter code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification.

    The list of all the emails from Sara are in the from_sara list
    likewise for emails from Chris (from_chris)

    The actual documents are in the Enron email dataset, which
    you downloaded/unpacked in Part 0 of the first mini-project. If you have
    not obtained the Enron email corpus, run startup.py in the tools folder.

    The data is stored in lists and packed away in pickle files at the end.
"""

from_sara = open("from_sara.txt", "r")
from_chris = open("from_chris.txt", "r")

from_data = []
word_data = []

# temp_counter is a way to speed up the development--there are
# thousands of emails from Sara and Chris, so running over all of them
# can take a long time
# temp_counter helps you only look at the first 200 emails in the list so you
# can iterate your modifications quicker
temp_counter = 0
unwanted = ["sara", "shackleton", "chris", "germani"]

for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    for path in from_person:
        # only look at first 200 emails when developing
        # once everything is working, remove this line to run over full dataset
        # temp_counter += 1
        # if True:  # temp_counter < 200
        path = os.path.join(r'C:\Users\japau\Documents\Large Docs/', path[:-1])
        email = open(path, "r")

        # use parseOutText to extract the text from the opened email
        text_list = parseOutText(email)
        # print type(text_list)
        # text_list = text_list.split()

        # use str.replace() to remove any instances of the words
        ''' not good way to do this
        sList = ["sara", "shackleton", "chris", "germani"]
        quickList = []
        for s in text_list:
            if s not in sList:
                quickList.append(s)
        '''

        for word_u in unwanted:
            text_list = text_list.replace(word_u, "")

        # print text_list
        word_data.append("".join(text_list))
        # append the text to word_data
        from_data.append(0 if name == 'sara' else 1)
        # append a 0 to from_data if email is from Sara, and 1 if email is from Chris
        email.close()

# print "emails processed"
from_sara.close()
from_chris.close()
print word_data

if True:
    pickle.dump(word_data, open("your_word_data.pkl", "w"))
    pickle.dump(from_data, open("your_email_authors.pkl", "w"))

'''
def tokenize(text):
    tokens = word_tokenize(text)
    return tokens
'''


tfidf = TfidfVectorizer(stop_words='english')
tfidf.fit_transform(word_data)
vocab_list = tfidf.get_feature_names()
print len(vocab_list)



