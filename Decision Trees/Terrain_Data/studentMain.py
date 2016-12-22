

""" lecture and example code for decision tree unit """

# import sys
from class_vis import prettyPicture, output_image
from prep_terrain_data import makeTerrainData
# import matplotlib.pyplot as plt
# import numpy as np
# import pylab as pl
from sklearn.metrics import accuracy_score
from sklearn import tree


def classify1(features, labels):
    clf = tree.DecisionTreeClassifier(min_samples_split=2)
    clf.fit(features, labels)
    pred = clf.predict(features_test)

    return clf, pred


def classify2(features, labels):
    clf = tree.DecisionTreeClassifier(min_samples_split=50)
    clf.fit(features, labels)
    pred = clf.predict(features_test)

    return clf, pred

features_train, labels_train, features_test, labels_test = makeTerrainData()

# the classify() function in classifyDT is where the magic
# happens--fill in this function in the file 'classifyDT.py'!
clf1, pred1 = classify1(features_train, labels_train)
acc1 = accuracy_score(pred1, labels_test)

clf2, pred2 = classify2(features_train, labels_train)
acc2 = accuracy_score(pred2, labels_test)

print acc1, acc2

prettyPicture(clf2, features_test, labels_test)
output_image("test.png", "png", open("test.png", "rb").read())




