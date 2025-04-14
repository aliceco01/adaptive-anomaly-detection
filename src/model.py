"""
Module: model.py
Runs basic anomaly detection using unsupervised ML (e.g. Isolation Forest).
"""

from sklearn.ensemble import IsolationForest

def train_model(X):
    model = IsolationForest(contamination=0.05)
    model.fit(X)
    return model

def predict(model, X):
    return model.predict(X), model.decision_function(X)
