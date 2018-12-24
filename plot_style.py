#!/usr/bin/env python

"""plot_style cycles through all of the available matplotlib styles."""

import matplotlib.pyplot as plt

import pandas as pd
from pandas.plotting import scatter_matrix

from sklearn import datasets

IRIS = datasets.load_iris()
X = IRIS.data
Y = IRIS.target
DF = pd.DataFrame(X, columns=IRIS.feature_names)

try:
    for style in plt.style.available:
        print style
        plt.style.use(style)
        scatter_matrix(DF, c=Y, s=50)
        plt.show()
except KeyboardInterrupt:
    pass
