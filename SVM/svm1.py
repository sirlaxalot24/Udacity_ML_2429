import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import copy
import numpy as np
import pylab as pl
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

features_train, labels_train, features_test, labels_test = makeTerrainData()

clf = SVC(kernel="linear")
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)


# now your job is to fit the classifier
# using the training features/labels, and to
# make a set of predictions on the test data

# store your predictions in a list named pred

acc = accuracy_score(pred, labels_test)


def submitAccuracy():
    print acc
    return acc

if __name__=='__main__':
    submitAccuracy()
    prettyPicture(clf, features_test, labels_test)