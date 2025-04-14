"""
Module: preprocess.py
Preprocesses telemetry data: normalization, log transformation, windowing, etc.
"""

from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd

def normalize_data(df):
    scaler = StandardScaler()
    scaled = scaler.fit_transform(df)
    return pd.DataFrame(scaled, columns=df.columns)
