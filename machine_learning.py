# -*- coding: utf-8 -*-
"""machine_learning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MDlbMpNXM8bxZzAFzAg3VajbQuh8Hntb
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from scipy.stats import pearsonr
import numpy as np
import matplotlib.pyplot as plt


# question 5 machine learning
def train_and_evaluate_model(df, features, target):
    '''
    Return the accuracy and mean square error of
    popularity of songs, predicting through song features.
    Plot and calculate the correlation between Predicted
    Popularity and Actual Popularity
    '''

    X = df[features]
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size=0.2,
                                                        random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error (MSE): {mse:.2f}")

    correlation, _ = pearsonr(np.array(y_test['popularity']), y_pred.flatten())
    print(f"Correlation of Predicted Actual Popularity: {correlation:.2f}")

    plt.scatter(y_test, y_pred)
    plt.xlabel("Actual Popularity")
    plt.ylabel("Predicted Popularity")
    plt.title("Actual Popularity vs. Predicted Popularity")
    plt.show()


if __name__ == '__main__':
    df = pd.read_csv('/content/top50MusicFrom2010-2019.csv')
    # machine learning
    features = ['duration', 'danceability', 'energy', 'loudness',
                'speechiness', 'acousticness',
                'liveness', 'valence', 'tempo']
    target = ['popularity']

    train_and_evaluate_model(df, features, target)
