import numpy as np
import pandas as pd
import joblib


def predict_price(df, paths):
    """ xxx """
    price = None

    transformer = joblib.load(paths["transformer"])
    scaler = joblib.load(paths["scaler"])
    model = joblib.load(paths["model"])
    
    X_predict = df.to_numpy()
    X_predict = transformer.transform(X_predict)
    X_predict = scaler.transform(X_predict)

    prediction = (model.predict(X_predict)).tolist()
    price = round(prediction[0]/1000)*1000

    return price