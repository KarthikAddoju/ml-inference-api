import numpy as np
from sklearn.linear_model import LogisticRegression

def load_model():
    """
    Trains and returns a simple Logistic Regression model.
    This simulates a trained ML model used for inference.
    """

    X = np.array([[0], [1], [2], [3], [4]])
    y = np.array([0, 0, 0, 1, 1])

    model = LogisticRegression()
    model.fit(X, y)

    return model
