
import sys
# import matplotlib.pyplot as plt
# import numpy as np
from email_preprocess import preprocess
from sklearn.metrics import accuracy_score
from sklearn import tree

features_train, features_test, labels_train, labels_test = preprocess()

clf = tree.DecisionTreeClassifier(min_samples_split=40)
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
acc2 = accuracy_score(pred, labels_test)

print len(features_train[0])
print acc2
