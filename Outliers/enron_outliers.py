#!/usr/bin/python

import pickle
import matplotlib.pyplot as plt
from feature_format import featureFormat, targetFeatureSplit
# from pprint import pprint as pp
import numpy as np
# from sklearn.linear_model import LinearRegression
import pandas as pd

pd.set_option("expand_frame_repr", False)
pd.set_option("display.max_rows", 1000)
np.set_printoptions(precision=4, suppress=True)

pklFilePath = r"C:\Users\japau\Google Drive\Udacity\Udacity_ML_2429"
pklFile = r"\final_project_dataset.pkl"

# read in data dictionary, convert to numpy array
data_dict = pickle.load(open(pklFilePath + pklFile, "r"))
data_dict.pop("TOTAL", None)
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


# I added this pandas dataframe to explore the dataset
# this was completely unnecessary as part of the mini project but made it slightly easier
johnP = {'index': 'Paukovits John', 'salary': 200000, 'bonus': 10, 'exercised_stock_options': 1000000}

dataDF = pd.DataFrame(data_dict)
dataDF = dataDF.transpose().reset_index()
dataDF = dataDF[dataDF['salary'] != 'NaN']
dataDF = dataDF[dataDF['exercised_stock_options'] != 'NaN']
dataDF = dataDF.append(johnP, ignore_index=True)
dataDF = dataDF[['index', 'salary', 'bonus', 'exercised_stock_options']].sort_values(by='salary',
                                                                                     ascending=False).reset_index()

dataDF['scaledSal'] = (dataDF['salary'].astype(float)
                       - float(dataDF['salary'].min()))\
                      / (float(dataDF['salary'].max(skipna=True))
                         - float(dataDF['salary'].min()))

dataDF['scaledStock'] = (dataDF['exercised_stock_options'].astype(float)
                           - float(dataDF['exercised_stock_options'].min()))\
                           / (float(dataDF['exercised_stock_options'].max(skipna=True))
                           - float(dataDF['exercised_stock_options'].min()))

print dataDF, type(dataDF['salary'][0])

# Ploting Begins
for point in data:
    salary = point[0]
    bonus = point[1]
    plt.scatter(salary, bonus)

ax = plt.gca()
ax.get_xaxis().get_major_formatter().set_scientific(False)
ax.get_yaxis().get_major_formatter().set_scientific(False)
plt.xlabel("salary")
plt.ylabel("bonus")
# plt.show()
