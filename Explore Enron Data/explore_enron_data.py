#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import pandas as pd
from pprint import pprint

pd.set_option("expand_frame_repr", False)
pd.set_option("display.max_rows", 1000)

enron_data = pickle.load(open(r'final_project_dataset.pkl', "r"))
mailDF = pd.DataFrame(enron_data).T

pprint(enron_data["SKILLING JEFFREY K"])

# print mailDF

# names = pd.DataFrame.from_csv('poi_names.txt', )
# print names
# print names.shape