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
mailDF = mailDF.reset_index()

salDF = mailDF[['index', 'total_payments']][mailDF['total_payments'] == "NaN"]
salDF['Split Name'] = salDF['index'].str.split()
salDF["Full Name"] = ""
# salDF = salDF.reindex()

for row in salDF.index:
    salDF['Full Name'][row] = salDF['Split Name'][row][0] + " " + salDF['Split Name'][row][1]

print len(mailDF['poi'][mailDF['poi'] == True])


names = pd.read_csv('poi_names.txt', header=None, delim_whitespace=True, names=("Y/N", "Last Name", "First Name"))
names['Full Name'] = names['Last Name'] + "" + names["First Name"]
names['Full Name'] = names['Full Name'].str.replace(",", " ")
poi = names['Full Name'].str.upper()

print poi

poiSal = salDF.isin(poi)

print poiSal

# print names.shape, names.columns