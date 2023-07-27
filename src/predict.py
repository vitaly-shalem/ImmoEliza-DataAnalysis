import numpy as np
import pandas as pd
import joblib


def predict_price(df, paths):
    """ xxx """
    price = None

    transformer = joblib.load(paths["transformer"])
    scaler = joblib.load(paths["scaler"])
    model = joblib.load(paths["model"])
    
    X = df.to_numpy()
    X = transformer.transform(X)
    X = scaler.transform(X)

    prediction = (model.predict(X)).tolist()
    price = prediction[0]

    return price