#!/usr/bin/python

import pickle
import matplotlib.pyplot as plt
from feature_format import featureFormat, targetFeatureSplit
from pprint import pprint as pp
import numpy as np
from sklearn.linear_model import LinearRegression
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
dataDF = pd.DataFrame(data_dict)
dataDF = dataDF.transpose().reset_index()
dataDF = dataDF[['index', 'salary', 'bonus']].sort_values(by='salary',\
                                                                           ascending=False)
print dataDF

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
