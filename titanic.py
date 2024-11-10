# -*- coding: utf-8 -*-
"""Titanic.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14m2b0r90CtIbdMELUwxVjrrDqPgYdqYS
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('titanic')

df.head()

df.shape

df.columns

df=df.loc[:,['survived', 'pclass', 'sibsp', 'parch']]
df.head()

df.isnull().sum()

X=df.iloc[:, 1:6]
Y=df.iloc[:, 0]

X.head()

Y.head()

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=1)

X_train

Y_train

from sklearn.linear_model import LogisticRegression

clf=LogisticRegression()
clf.fit(X_train, Y_train)

Pred=clf.predict(X_test)

Pred

Y_test

from sklearn.metrics import accuracy_score
accuracy_score(Y_test, Pred)