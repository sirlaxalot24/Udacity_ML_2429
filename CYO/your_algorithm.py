#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

features_train, labels_train, features_test, labels_test = makeTerrainData()


# the training data (features_train, labels_train) have both "fast" and "slow"
# points mixed together--separate them so we can give them different colors
# in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


# initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
#plt.show()

# your code here!  name your classifier object clf if you want the
# visualization code (prettyPicture) to show you the decision boundary

clf = KNeighborsClassifier(n_neighbors=10)
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
acc1 = accuracy_score(pred, labels_test)

prettyPicture(clf, features_test, labels_test)

clf1 = AdaBoostClassifier(n_estimators=100)
clf1.fit(features_train, labels_train)
pred = clf1.predict(features_test)
acc2 = accuracy_score(pred, labels_test)

prettyPicture(clf1, features_test, labels_test)

clf2 = RandomForestClassifier()
clf2.fit(features_train, labels_train)
pred = clf2.predict(features_test)
acc3 = accuracy_score(pred, labels_test)
prettyPicture(clf2, features_test, labels_test)

scores = {'Knearest': acc1, 'AdaBoost': acc2, 'Random Forest': acc3}
print scores